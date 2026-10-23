import os
import re
import html
import joblib
import pandas as pd
import pymupdf as fitz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model training project")
RAW_DATA_PATH = os.path.join(BASE_DIR, "Dataset", "mtsamples.csv")
FILTERED_DATA_PATH = os.path.join(MODEL_DIR, "filtered_mtsamples_8classes.csv")
UNSEEN_FOLDER = os.path.join(BASE_DIR, "unseen data")
DATASET_FOLDER = os.path.join(BASE_DIR, "Dataset")

os.makedirs(UNSEEN_FOLDER, exist_ok=True)

def sanitize_filename(name: str) -> str:
    """Sanitize specialty name for Windows filenames."""
    # Replace / and \ with -
    s = re.sub(r'[\\/]', ' - ', name)
    # Remove any other forbidden characters: : * ? " < > |
    s = re.sub(r'[:*?"<>|]', '', s)
    # Collapse multiple spaces or dashes
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'(\s*-\s*)+', ' - ', s)
    return s.strip()

def clean_transcription_text(raw_text: str) -> str:
    """
    Format clinical transcription cleanly for PDF layout.
    Preserves all clinical terminology, diagnoses, and details while
    cleaning MTSamples scraping comma artifacts.
    """
    if not isinstance(raw_text, str):
        return ""
    text = raw_text.strip()
    
    # 1. Normalize line breaks and comma sequences from scraping
    text = re.sub(r' ,(?= )', '', text)
    text = re.sub(r', ,', '\n\n', text)
    
    # 2. Add line breaks before common uppercase clinical section headers if preceded by comma
    text = re.sub(r',\s*([A-Z\s/]{3,}:)', r'\n\n\1', text)
    
    # 3. Clean multiple trailing or leading commas on lines
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        l = line.strip()
        # Remove leading/trailing stray commas
        l = re.sub(r'^,\s*', '', l)
        l = re.sub(r',\s*$', '', l)
        cleaned_lines.append(l)
        
    return '\n'.join(cleaned_lines).strip()

def generate_pdf_from_transcription(transcription_text: str, output_path: str):
    """
    Creates a clean, multi-page PDF document containing ONLY the clinical transcription.
    Uses PyMuPDF Story with elegant typography and auto-pagination.
    """
    cleaned_text = clean_transcription_text(transcription_text)
    
    # Convert text to HTML paragraphs for Story layout
    paragraphs = []
    for block in cleaned_text.split('\n'):
        block_clean = block.strip()
        if not block_clean:
            paragraphs.append("<div style='height: 6pt;'></div>")
        else:
            # Check if block looks like a section header (e.g. "HISTORY:", "PROCEDURE PERFORMED:")
            is_header = bool(re.match(r'^[A-Z0-9\s/()-]{3,}:', block_clean))
            escaped_block = html.escape(block_clean)
            if is_header:
                paragraphs.append(f"<p style='margin: 10pt 0 4pt 0; font-weight: bold; color: #111827; font-size: 10.5pt;'>{escaped_block}</p>")
            else:
                paragraphs.append(f"<p style='margin: 0 0 6pt 0; line-height: 1.45; text-align: justify; color: #1f2937;'>{escaped_block}</p>")
                
    body_content = "".join(paragraphs)
    html_doc = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        body {{
          font-family: Arial, Helvetica, sans-serif;
          font-size: 10pt;
          line-height: 1.45;
          color: #1f2937;
        }}
      </style>
    </head>
    <body>
      {body_content}
    </body>
    </html>
    """
    
    story = fitz.Story(html=html_doc)
    writer = fitz.DocumentWriter(output_path)
    # A4 page dimensions in points: 595.3 x 841.9
    mediabox = fitz.Rect(0, 0, 595, 842)
    # 54pt margins (0.75 inch)
    content_rect = fitz.Rect(54, 54, 595 - 54, 842 - 54)
    
    more = 1
    while more:
        dev = writer.begin_page(mediabox)
        more, _ = story.place(content_rect)
        story.draw(dev)
        writer.end_page()
    writer.close()

def main():
    print("=" * 80)
    print("GENERATING UNSEEN CLINICAL TRANSCRIPTION DATASET & PDF ARCHIVE")
    print("=" * 80)
    
    # 1. Load Filtered 8-Class Dataset and held-out test split
    df_filtered = pd.read_csv(FILTERED_DATA_PATH)
    y_test_saved = joblib.load(os.path.join(MODEL_DIR, "y_test.pkl"))
    test_indices = list(y_test_saved.index)
    test_df = df_filtered.loc[test_indices].copy()
    test_df["medical_specialty"] = test_df["medical_specialty"].str.strip()
    test_df["word_count"] = test_df["transcription"].astype(str).str.split().str.len()
    
    # 2. Load Raw MTSamples for Out-of-Domain Open-Set evaluation
    df_raw = pd.read_csv(RAW_DATA_PATH)
    df_raw = df_raw.dropna(subset=['transcription', 'medical_specialty']).copy()
    df_raw["medical_specialty"] = df_raw["medical_specialty"].str.strip()
    df_raw["word_count"] = df_raw["transcription"].astype(str).str.split().str.len()
    
    # Filter raw to rows NEVER included in the 8-class filtered dataset
    raw_indices_used = set(df_filtered['Unnamed: 0'])
    df_raw_ood = df_raw[~df_raw['Unnamed: 0'].isin(raw_indices_used)].copy()
    
    # 3. Select 10 diverse, high-quality test samples for each of the 8 Core Specialties (80 PDFs)
    target_specialties = [
        'Cardiovascular / Pulmonary',
        'Orthopedic',
        'Gastroenterology',
        'Neurology',
        'Urology',
        'Obstetrics / Gynecology',
        'ENT - Otolaryngology',
        'Ophthalmology'
    ]
    
    selected_pdf_samples = []
    
    for spec in target_specialties:
        spec_df = test_df[test_df["medical_specialty"] == spec].copy()
        # Filter for good clinical richness (>= 50 words)
        rich_samples = spec_df[spec_df["word_count"] >= 50].sort_values(by="word_count", ascending=False)
        # Select top 10
        chosen = rich_samples.head(10).copy()
        chosen["category_type"] = "Core 8-Class Specialty"
        chosen["is_out_of_domain"] = False
        selected_pdf_samples.append(chosen)
        
    # 4. Select 2 samples each from 5 distinct Out-of-Domain specialties (10 PDFs)
    ood_specialties = [
        'Dermatology',
        'Pediatrics - Neonatal',
        'Psychiatry / Psychology',
        'Radiology',
        'Allergy / Immunology'
    ]
    for ood_spec in ood_specialties:
        ood_subset = df_raw_ood[df_raw_ood["medical_specialty"] == ood_spec].copy()
        rich_ood = ood_subset[ood_subset["word_count"] >= 50].sort_values(by="word_count", ascending=False)
        chosen = rich_ood.head(2).copy()
        chosen["category_type"] = "Out-of-Domain Open-Set"
        chosen["is_out_of_domain"] = True
        selected_pdf_samples.append(chosen)
        
    pdf_samples_df = pd.concat(selected_pdf_samples, ignore_index=True)
    print(f"Total samples designated for PDF generation: {len(pdf_samples_df)} (80 Core + 10 Open-Set OOD)")
    
    # 5. Generate PDFs
    print("\nGenerating PDF documents in 'unseen data/' ...")
    generated_pdf_records = []
    specialty_counters = {}
    
    for idx, row in pdf_samples_df.iterrows():
        spec = row["medical_specialty"]
        clean_spec = sanitize_filename(spec)
        
        counter = specialty_counters.get(clean_spec, 0) + 1
        specialty_counters[clean_spec] = counter
        
        pdf_filename = f"{clean_spec} - {counter:02d}.pdf"
        pdf_path = os.path.join(UNSEEN_FOLDER, pdf_filename)
        
        transcription_text = str(row["transcription"])
        generate_pdf_from_transcription(transcription_text, pdf_path)
        
        # Verify generated PDF
        doc = fitz.open(pdf_path)
        page_cnt = len(doc)
        text_len = sum(len(page.get_text()) for page in doc)
        doc.close()
        
        row_dict = row.to_dict()
        row_dict["pdf_filename"] = pdf_filename
        row_dict["pdf_page_count"] = page_cnt
        row_dict["has_pdf"] = True
        generated_pdf_records.append(row_dict)
        
        if counter == 1:
            print(f"  -> {pdf_filename:<36} ({page_cnt} pages, {row['word_count']} words)")
            
    print(f"\nAll {len(pdf_samples_df)} PDFs successfully generated and verified in:\n  {UNSEEN_FOLDER}")
    
    # 6. Build the Complete Unseen Dataset
    # Incorporates:
    # A) All 333 held-out test samples (from the trained ML pipeline's test split)
    # B) The 10 Out-of-Domain open-set samples
    print("\nBuilding comprehensive 'unseen_dataset.csv'...")
    all_unseen_records = []
    
    pdf_filenames_map = {r["Unnamed: 0"]: r["pdf_filename"] for r in generated_pdf_records}
    
    sample_id = 1
    # Add all 333 held-out test samples
    for _, row in test_df.iterrows():
        raw_id = row["Unnamed: 0"]
        pdf_fname = pdf_filenames_map.get(raw_id, "")
        all_unseen_records.append({
            "sample_id": f"UNSEEN_{sample_id:04d}",
            "original_record_id": int(raw_id),
            "medical_specialty": row["medical_specialty"],
            "category_type": "Core 8-Class Specialty",
            "is_out_of_domain": False,
            "sample_name": str(row.get("sample_name", "")).strip(),
            "description": str(row.get("description", "")).strip(),
            "word_count": int(row["word_count"]),
            "char_count": len(str(row["transcription"])),
            "has_pdf": bool(pdf_fname != ""),
            "pdf_filename": pdf_fname,
            "transcription": str(row["transcription"]).strip()
        })
        sample_id += 1
        
    # Add the 10 Out-of-domain open-set samples
    for r in generated_pdf_records:
        if r["is_out_of_domain"]:
            all_unseen_records.append({
                "sample_id": f"UNSEEN_{sample_id:04d}",
                "original_record_id": int(r["Unnamed: 0"]),
                "medical_specialty": r["medical_specialty"],
                "category_type": "Out-of-Domain Open-Set",
                "is_out_of_domain": True,
                "sample_name": str(r.get("sample_name", "")).strip(),
                "description": str(r.get("description", "")).strip(),
                "word_count": int(r["word_count"]),
                "char_count": len(str(r["transcription"])),
                "has_pdf": True,
                "pdf_filename": r["pdf_filename"],
                "transcription": str(r["transcription"]).strip()
            })
            sample_id += 1
            
    df_all_unseen = pd.DataFrame(all_unseen_records)
    
    # Save CSV files:
    # 1. In 'unseen data/unseen_dataset.csv'
    csv_unseen_folder = os.path.join(UNSEEN_FOLDER, "unseen_dataset.csv")
    df_all_unseen.to_csv(csv_unseen_folder, index=False)
    print(f"Saved: {csv_unseen_folder}")
    
    # 2. In 'Dataset/unseen_dataset.csv'
    csv_dataset_folder = os.path.join(DATASET_FOLDER, "unseen_dataset.csv")
    df_all_unseen.to_csv(csv_dataset_folder, index=False)
    print(f"Saved: {csv_dataset_folder}")
    
    # 3. Also save a dedicated PDF-only dataset index 'unseen data/pdf_dataset_index.csv'
    df_pdf_only = df_all_unseen[df_all_unseen["has_pdf"]].copy()
    pdf_index_path = os.path.join(UNSEEN_FOLDER, "pdf_dataset_index.csv")
    df_pdf_only.to_csv(pdf_index_path, index=False)
    print(f"Saved: {pdf_index_path}")
    
    print("\n" + "=" * 60)
    print("UNSEEN DATA SUMMARY:")
    print("=" * 60)
    print(f"Total Records in Unseen Dataset : {len(df_all_unseen)}")
    print(f"Total Generated PDFs           : {len(df_pdf_only)} (Minimum 50 required)")
    print(f"Core 8-Class Specialty PDFs    : 80 (10 per specialty)")
    print(f"Out-of-Domain Open-Set PDFs    : 10 (2 per specialty)")
    print(f"PDF Location                   : {UNSEEN_FOLDER}")
    print("=" * 60)

if __name__ == "__main__":
    main()
