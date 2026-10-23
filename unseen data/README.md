# Unseen Clinical Transcription Dataset & PDF Evaluation Archive

**Project:** Medical Specialty Classification Using TF-IDF & Ensemble Machine Learning  
**Author:** Jiphin George (MAC25MCA-2033) | **Course:** S3 MCA Mini Project  
**Repository Directory:** `unseen data/`

---

## 1. Overview

This folder contains **held-out unseen medical transcription data** specifically created for independent model evaluation, clinical testing, and web interface demonstration:

1. **90 Unseen Clinical PDFs** (exceeding the 50-file minimum requirement):
   - **80 Core Specialty PDFs**: Exactly 10 documents per department for all 8 trained specialties (`Cardiovascular / Pulmonary`, `Orthopedic`, `Gastroenterology`, `Neurology`, `Urology`, `Obstetrics / Gynecology`, `ENT - Otolaryngology`, `Ophthalmology`).
   - **10 Out-of-Domain Open-Set PDFs**: 2 documents each for 5 outside specialties (`Dermatology`, `Pediatrics - Neonatal`, `Psychiatry / Psychology`, `Radiology`, `Allergy / Immunology`) to demonstrate the **9-class open-set rejection / "Other" triage engine**.
2. **Strict Document Specification**:
   - Every PDF is named according to its clinical specialty: e.g., `Cardiovascular - Pulmonary - 01.pdf`, `Neurology - 01.pdf`.
   - Each PDF contains **exclusively the medical transcription text** (no document headers, patient tags, or department labels) to ensure authentic testing.
3. **Separate Unseen Datasets**:
   - `unseen_dataset.csv`: Comprehensive tabular dataset containing **343 unseen records** (all 333 held-out test samples + 10 out-of-domain open-set samples).
   - `pdf_dataset_index.csv`: Index of the 90 generated PDF files with associated word counts, page counts, and metadata.
   - Also mirrored in `Dataset/unseen_dataset.csv` for pipeline integration.

---

## 2. Directory Structure

```text
unseen data/
├── Allergy - Immunology - 01.pdf to 02.pdf          (2 PDFs)
├── Cardiovascular - Pulmonary - 01.pdf to 10.pdf    (10 PDFs)
├── Dermatology - 01.pdf to 02.pdf                   (2 PDFs)
├── ENT - Otolaryngology - 01.pdf to 10.pdf          (10 PDFs)
├── Gastroenterology - 01.pdf to 10.pdf              (10 PDFs)
├── Neurology - 01.pdf to 10.pdf                     (10 PDFs)
├── Obstetrics - Gynecology - 01.pdf to 10.pdf       (10 PDFs)
├── Ophthalmology - 01.pdf to 10.pdf                 (10 PDFs)
├── Orthopedic - 01.pdf to 10.pdf                    (10 PDFs)
├── Pediatrics - Neonatal - 01.pdf to 02.pdf         (2 PDFs)
├── Psychiatry - Psychology - 01.pdf to 02.pdf       (2 PDFs)
├── Radiology - 01.pdf to 02.pdf                     (2 PDFs)
├── Urology - 01.pdf to 10.pdf                       (10 PDFs)
├── pdf_dataset_index.csv                            (90 rows)
├── unseen_dataset.csv                               (343 rows)
└── README.md                                        (This file)
```

---

## 3. Dataset Schema (`unseen_dataset.csv`)

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `sample_id` | String | Unique identifier (`UNSEEN_0001` to `UNSEEN_0343`) |
| `original_record_id` | Integer | Original record index from the raw MTSamples corpus |
| `medical_specialty` | String | Ground-truth clinical department |
| `category_type` | String | `Core 8-Class Specialty` or `Out-of-Domain Open-Set` |
| `is_out_of_domain` | Boolean | `False` for core specialties; `True` for out-of-domain rejection testing |
| `sample_name` | String | Clinical procedure / dictation description from MTSamples |
| `description` | String | Short clinical summary |
| `word_count` | Integer | Total word count of the medical transcription |
| `char_count` | Integer | Total character count |
| `has_pdf` | Boolean | `True` if a standalone PDF was generated in `unseen data/` |
| `pdf_filename` | String | Target filename (e.g., `Neurology - 01.pdf`) or blank |
| `transcription` | Text | Exact medical transcription text |

---

## 4. How to Test in the Web Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Navigate to `http://127.0.0.1:5000/` in your browser.
3. Under the **Clinical PDF Upload** section, drag and drop or browse any PDF from the `unseen data/` folder (e.g., `Orthopedic - 01.pdf`).
4. The system will extract the transcription text using PyMuPDF and automatically run the multi-model voting ensemble inference.
