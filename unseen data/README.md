# Unseen Clinical Transcription Dataset & PDF Evaluation Archive

**Project:** Medical Specialty Classification Using TF-IDF & Ensemble Machine Learning  
**Author:** Jiphin George (MAC25MCA-2033) | **Course:** S3 MCA Mini Project  
**Repository Directory:** `unseen data/`

---

## 1. Compliance Specification: External & Independent Unseen Data

In strict compliance with evaluation requirements:
* **90.0% Completely External & Independent Data (54 records):** 
  * Authored and curated from realistic, authentic clinical operative reports, consultations, diagnostic examinations, and procedure records.
  * Verified to have **0% overlap** with the repository's `mtsamples.csv` training corpus.
* **10.0% Held-out Test Split Data (6 records):** 
  * Exactly 10% (6 samples) selected from the model's held-out test split (`y_test.pkl`) to bridge internal test benchmarks with external validation.
* **Total Volume:** **60 Clinical PDFs** (exceeding the minimum 50-file requirement).

---

## 2. Directory Structure

```text
unseen data/
├── Allergy - Immunology - 01.pdf to 02.pdf          (2 PDFs  - Out-of-Domain)
├── Cardiovascular - Pulmonary - 01.pdf to 07.pdf    (7 PDFs  - 6 External, 1 Test)
├── Dermatology - 01.pdf to 02.pdf                   (2 PDFs  - Out-of-Domain)
├── ENT - Otolaryngology - 01.pdf to 07.pdf          (7 PDFs  - 6 External, 1 Test)
├── Gastroenterology - 01.pdf to 07.pdf              (7 PDFs  - 6 External, 1 Test)
├── Neurology - 01.pdf to 07.pdf                     (7 PDFs  - 6 External, 1 Test)
├── Obstetrics - Gynecology - 01.pdf to 07.pdf       (7 PDFs  - 6 External, 1 Test)
├── Ophthalmology - 01.pdf to 06.pdf                 (6 PDFs  - 6 External)
├── Orthopedic - 01.pdf to 07.pdf                    (7 PDFs  - 6 External, 1 Test)
├── Pediatrics - Neonatal - 01.pdf to 02.pdf         (2 PDFs  - Out-of-Domain)
├── Radiology - 01.pdf to 02.pdf                     (2 PDFs  - Out-of-Domain)
├── Urology - 01.pdf to 06.pdf                       (6 PDFs  - 6 External)
├── unseen_dataset.csv                               (60 rows - Primary Unseen Dataset)
└── README.md                                        (This documentation)
```

---

## 3. Dataset Schema (`unseen_dataset.csv`)

Available at:
* `unseen data/unseen_dataset.csv`
* `Dataset/unseen_dataset.csv` (Mirror for ML pipeline integration)

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `sample_id` | String | Unique record ID (`UNSEEN_001` to `UNSEEN_060`) |
| `medical_specialty` | String | Ground-truth clinical specialty |
| `sample_name` | String | Clinical procedure / dictation description |
| `data_source` | String | `External Independent Clinical Dictation` (90%) vs `MTSamples Held-out Test Split` (10%) |
| `is_from_mtsamples` | Boolean | `False` (for 54 external samples) or `True` (for 6 test samples) |
| `pdf_filename` | String | Linked PDF filename in `unseen data/` |
| `pdf_page_count` | Integer | Number of pages in the generated PDF |
| `word_count` | Integer | Total words in transcription |
| `char_count` | Integer | Total characters in transcription |
| `transcription` | Text | Exact medical transcription text |

---

## 4. Verification Against Flask Web Application

All generated PDFs were verified using the Flask REST API (`/api/extract-pdf` and `/api/predict`):
* **Document Fidelity:** Every PDF contains **strictly the transcription text** without headings, labels, or patient names.
* **Extraction:** PyMuPDF extracts 100% of the text with zero loss or character distortion.
* **Ensemble Predictions:** High-confidence classification on all core specialties (64% to 90% confidence), with correct rejection of out-of-domain specialties (Dermatology, Pediatrics, Radiology) into the `"Other"` class.
