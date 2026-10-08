# Medical Specialty Classification Using TF-IDF and Ensemble Machine Learning

**Comprehensive Technical Summary, Methodology Report & Clinical Triage Guide**  
*Master of Computer Applications (MCA) — Semester 3 Mini Project*  
*Mar Athanasius College of Engineering, Kothamangalam*  
*Author:* Jiphin George (MAC25MCA-2033) | *Guide:* Prof. Biju Skaria  

---

## Quick Reference & Performance Highlights

| Project Attribute | Value / Specification |
| :--- | :--- |
| **Dataset** | Medical Transcriptions ([MTSamples](https://www.kaggle.com/datasets/tboyclk/medical-transcriptions)) — 4,999 raw records |
| **Curated Clinical Scope** | **8 Mutually Exclusive Clinical Departments** (1,663 records) |
| **Triage Architecture** | **9-Class Open-Set Inference Engine** (8 Core Specialties + 1 "Other" Class) |
| **NLP Feature Extraction** | Controlled **8,000-feature TF-IDF** (Unigrams + Bigrams, Sublinear Scaling, $L_2$ Norm) |
| **Core Classifiers** | Linear SVM, Logistic Regression, Random Forest, Multinomial Naive Bayes |
| **Ensemble Architecture** | **Calibrated Soft Voting Ensemble** with empirical weights **[2, 2, 1, 1]** |
| **Peak Model Accuracy** | **88.59%** (Linear SVM) \| **87.99%** (Soft Voting Ensemble) |
| **Peak Macro F1-Score** | **0.8971** (Linear SVM) \| **0.8898** (Soft Voting Ensemble) |
| **Target Requirement** | Minimum $\ge 75.0\%$ Accuracy *(Comfortably Exceeded by $+13.59\%$)* |
| **Deployment Footprint** | **11.9 MB total** (`joblib` serialized pipeline) \| **< 12 ms** CPU inference latency |

---

## Table of Contents
1. [Executive Summary & Core Milestones](#1-executive-summary--core-milestones)
2. [Initial Problem Statement & Baseline Diagnosis](#2-initial-problem-statement--baseline-diagnosis)
3. [Exploratory Data Analysis & Strategic Iterations](#3-exploratory-data-analysis--strategic-iterations)
4. [Feature Engineering & Preprocessing Architecture](#4-feature-engineering--preprocessing-architecture)
5. [Model Implementations & Ensemble Formulation](#5-model-implementations--ensemble-formulation)
6. [Comprehensive Experimental Benchmark Results](#6-comprehensive-experimental-benchmark-results)
7. [9-Class Open-Set Clinical Triage Inference Engine](#7-9-class-open-set-clinical-triage-inference-engine)
8. [Repository Deliverables & File Structure](#8-repository-deliverables--file-structure)
9. [GitHub 100MB File-Size Resolution](#9-github-100mb-file-size-resolution)
10. [Academic Timeline & Milestone Schedule](#10-academic-timeline--milestone-schedule)
11. [Viva & Project Defense Guide](#11-viva--project-defense-guide)

---

## 1. Executive Summary & Core Milestones

In this project, we resolved the severe multi-class performance bottleneck of automating clinical document classification on unstructured medical transcription data (MTSamples). Initial baseline models trained directly on the raw 40-class dataset suffered severe performance collapse (**7.85% to 27.39% accuracy**, with Macro F1 as low as **0.0348**).

Through systematic empirical diagnosis, domain-specific text filtering, feature space constraint engineering, and cost-sensitive ensemble learning, the system was transformed into a high-precision clinical decision-support pipeline:
* **Random Forest Accuracy:** Surged from $7.85\%$ to **$81.98\%$**.
* **Multinomial Naive Bayes Accuracy:** Increased from $27.09\%$ to **$77.48\%$**.
* **Logistic Regression Accuracy:** Climbed from $22.96\%$ to **$87.09\%$**.
* **Linear Support Vector Machine (Linear SVM):** Elevated from $10.67\%$ to **$88.59\%$** (Peak Individual Classifier).
* **Soft Voting Ensemble:** Combined LR, SVM, RF, and MNB with weights `[2, 2, 1, 1]`, achieving **$87.99\%$ Accuracy** and **$0.8898$ Macro F1**.
* **Open-Set 9-Class Triage:** Deployed an automated rejection filter that routes outside medical specialties (Dermatology, Psychiatry, Pediatrics) or ambiguous dictations directly to an **`"Other"`** category while preserving peak $88.59\%$ core accuracy.
* **Academic Goal Met:** Every candidate classifier and ensemble comfortably beats the MCA department's required $\ge 75.0\%$ threshold.

---

## 2. Initial Problem Statement & Baseline Diagnosis

### 2.1 The Initial 40-Class Baseline Collapse
Initial baseline experimentation on the uncurated 40-class dataset produced unacceptable diagnostic performance across all algorithms:

| Model Architecture | Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Linear SVM** | 10.67% | 0.0666 | 0.0535 | 0.0539 | 0.0972 |
| **Logistic Regression** | 22.96% | 0.0310 | 0.0441 | 0.0348 | 0.1676 |
| **Random Forest** | 7.85% | 0.0442 | 0.0324 | 0.0359 | 0.0734 |
| **Balanced SVM** | 10.07% | 0.1267 | 0.1810 | 0.1412 | 0.0953 |
| **Balanced Logistic Regression** | 27.39% | 0.2463 | 0.3711 | 0.2825 | 0.2392 |
| **Weighted Multinomial Naive Bayes** | 27.09% | 0.2849 | 0.5502 | 0.3415 | 0.2271 |

### 2.2 The Root Causes Diagnosed
Detailed empirical auditing uncovered four primary systemic failures:

1. **Catastrophic 184:1 Class Imbalance:**
   * "Surgery" alone represented 1,103 samples ($22.1\%$ of the dataset).
   * In contrast, 15+ minority categories suffered severe sample starvation: Hospice / Palliative Care ($N=6$), Allergy ($N=7$), Autopsy ($N=8$), Lab Pathology ($N=8$), Diets & Nutrition ($N=10$).
   * In an 80/20 train/test split, micro-classes had only 1 or 2 test samples. Misclassifying that single sample yields $\text{F1} = 0.0$, mathematically capping Macro F1 below $35\%$.
   * Unweighted models defaulted to the majority-class heuristic: trivially predicting "Surgery" for every document.

2. **The 310,000-Feature Sparsity Trap ($p \gg n$):**
   * Unconstrained TF-IDF vectorization with unigrams and bigrams produced **310,298 feature columns** for only 3,971 training samples (a **78:1 feature-to-sample ratio**).
   * Single-occurrence typos, dosage amounts, patient numbers, and names created extreme matrix sparsity ($99.9\%$ zeros).
   * Random Forest collapsed to $7.85\%$ because decision tree splits along $\sqrt{310,298} \approx 557$ random features almost always evaluated zero or pure noise.

3. **Administrative Document Format Contamination:**
   * Many raw labels were administrative document templates rather than clinical medical departments:
     * *SOAP / Chart / Progress Notes* (166 records)
     * *Discharge Summary* (108 records)
     * *Consult - History and Physical* (516 records)
     * *Emergency Room Reports* (75 records)
   * These administrative templates contain terms spanning all organs (heart, brain, bone), causing severe semantic collisions.

4. **Procedural Umbrella Overlap:**
   * "Surgery" is not a distinct clinical specialty; it overlaps entirely with Orthopedic surgeries, Cardiovascular bypasses, and Urology procedures.

---

## 3. Exploratory Data Analysis & Strategic Iterations

To solve these challenges, we structured development into three clear iterations:

```
[Iteration 1: 40 Raw Classes] -> Failed (7.8% - 27.4% Acc) -> Severe 184:1 skew & 310k feature explosion
               │
               ▼
[Iteration 2: 20-Class Filter] -> Improved (24% - 39.8% Acc) -> Pruned N < 50; persistent administrative noise
               │
               ▼
[Iteration 3: 8 Clinical Specialties] -> BREAKTHROUGH (88.59% SVM / 87.99% Ensemble) -> Mutually exclusive departments
```

### Iteration 3 Dataset Breakdown (The Final 8 Specialties)
By removing administrative paperwork formats and focusing on distinct anatomical hospital departments, we curated **1,663 clean clinical records**:

| # | Medical Specialty | Anatomical Focus | Sample Count | % of Dataset |
| :-: | :--- | :--- | :-: | :-: |
| 1 | **Cardiovascular / Pulmonary** | Heart, Arteries & Lungs | 371 | 22.31% |
| 2 | **Orthopedic** | Bones, Joints & Skeletal System | 355 | 21.35% |
| 3 | **Gastroenterology** | Digestive Tract, Liver & Bowel | 224 | 13.47% |
| 4 | **Neurology** | Brain, Spinal Cord & Nerves | 223 | 13.41% |
| 5 | **Urology** | Kidneys, Bladder & Urinary System | 156 | 9.38% |
| 6 | **Obstetrics / Gynecology** | Women's Reproductive & Childbirth | 155 | 9.32% |
| 7 | **ENT - Otolaryngology** | Ear, Nose & Throat | 96 | 5.77% |
| 8 | **Ophthalmology** | Eye Care & Ophthalmic Surgery | 83 | 4.99% |
| **Total** | **Curated Clinical Records** | **8 Distinct Hospital Departments** | **1,663** | **100.0%** |

---

## 4. Feature Engineering & Preprocessing Architecture

### 4.1 Clinical Text Fusion
MTSamples provides a `description` column (high-density case summary) and a `transcription` column (detailed narrative operative note). We concatenated both:
$$\text{clinical\_text} = \text{description} + \text{" "} + \text{transcription}$$
*(The `keywords` column was deliberately excluded to eliminate data scraping target leakage).*

### 4.2 Controlled TF-IDF Feature Space
We stabilized the high-dimensional feature space using `sklearn.feature_extraction.text.TfidfVectorizer`:
* `max_features = 8000`: Caps vocabulary to the top 8,000 most informative unigrams and bigrams.
* `ngram_range = (1, 2)`: Captures multi-word clinical phrases (*"coronary artery"*, *"lumbar spine"*, *"capsular bag"*).
* `sublinear_tf = True`: Replaces raw term frequency with $1 + \log(\text{TF})$, dampening terms repeated 20+ times in long operative notes.
* `min_df = 2`: Prunes one-off dictation typos and rare patient IDs.
* `max_df = 0.70`: Prunes non-discriminative ubiquitous clinical boilerplate (*"patient presented"*, *"procedure"*).
* `norm = 'l2'`: Normalizes vector length so short notes and long notes are evaluated on an equal Euclidean scale.

### 4.3 Training-Fold Resampling (SMOTE & ROS)
To address the remaining imbalance between Cardiovascular ($N=371$) and Ophthalmology ($N=83$):
* **Strict Evaluation Isolation:** All resampling was applied **strictly to the 1,330 training records**. The **333 test samples were kept completely un-augmented** to guarantee evaluation integrity.
* **Data-Level Resampling Tested:** 
  * **SMOTE ($k=3$):** Synthesized 1,046 feature vectors along nearest-neighbor lines, bringing training folds to 2,376 balanced rows.
  * **RandomOverSampler (ROS):** Exact replication of minority feature vectors.
* **Finding:** Algorithmic cost weighting (`class_weight='balanced'`) on Linear SVM produced cleaner hyperplanes without synthetic noise artifacts, driving our final models to peak performance.

---

## 5. Model Implementations & Ensemble Formulation

Four core algorithms and two voting ensemble configurations were benchmarked:

### 5.1 Linear Support Vector Machine (Linear SVM) — *Top Individual Model*
* **Config:** `LinearSVC(class_weight='balanced', C=1.0, max_iter=3000)`
* **Theory:** Casts 8,000 sparse TF-IDF features into high-dimensional space where classes become linearly separable (Cover's Theorem). Maximizes margin $\frac{2}{\|\vec{w}\|}$, yielding **$88.59\%$ Accuracy**.

### 5.2 Multinomial Logistic Regression (LR)
* **Config:** `LogisticRegression(class_weight='balanced', solver='lbfgs', max_iter=1000)`
* **Theory:** Models multi-class log-odds using softmax. Yields smooth, calibrated probabilities and **$87.09\%$ Accuracy**.

### 5.3 Random Forest Classifier (RF)
* **Config:** `RandomForestClassifier(n_estimators=100, max_depth=25, class_weight='balanced')`
* **Theory:** Ensemble of 100 decorrelated decision trees. Constraining vocabulary to 8,000 features recovered accuracy from $7.85\%$ to **$81.98\%$**.

### 5.4 Multinomial Naive Bayes (MNB)
* **Config:** `MultinomialNB(alpha=0.5)`
* **Theory:** Computes log-likelihood with Laplace smoothing ($\alpha=0.5$). Fast baseline yielding **$77.48\%$ Accuracy**.

### 5.5 Soft Voting Ensemble — *Best Calibrated Model*
* **Architecture:** Combines probability predictions from LR, Calibrated Linear SVM (Platt scaling), RF, and MNB:
  $$P(\text{class } c) = \frac{2 \cdot P_{\text{SVM}}(c) + 2 \cdot P_{\text{LR}}(c) + 1 \cdot P_{\text{RF}}(c) + 1 \cdot P_{\text{MNB}}(c)}{6}$$
* **Why Weights [2, 2, 1, 1]:** SVM ($88.6\%$) and LR ($87.1\%$) lead consensus with $66.7\%$ voting power, while RF and MNB act as regularizers to break ties and smooth overconfidence. Achieves **$87.99\%$ Accuracy** and **$0.8898$ Macro F1**.

---

## 6. Comprehensive Experimental Benchmark Results

### 6.1 Metric Evolution Across Project Iterations

```
┌──────────────────────────────────────┬────────────────────────────────┬──────────┬──────────────┬──────────┐
│ Iteration / Setup                    │ Top Model                      │ Accuracy │ Macro Recall │ Macro F1 │
├──────────────────────────────────────┼────────────────────────────────┼──────────┼──────────────┼──────────┤
│ 1. Baseline (40 Raw Classes)         │ Weighted Multinomial NB        │  27.09%  │    55.02%    │  0.3415  │
│ 2. Threshold Filter (20 Classes)     │ Balanced Logistic Regression   │  35.53%  │    49.09%    │  0.3895  │
│ 3. Final Curated (8 Specialties)     │ Support Vector Machine (SVM)   │  88.59%  │    89.02%    │  0.8971  │
│ 3. Final Curated (8 Specialties)     │ Soft Voting Ensemble           │  87.99%  │    87.95%    │  0.8898  │
└──────────────────────────────────────┴────────────────────────────────┴──────────┴──────────────┴──────────┘
```

### 6.2 Final 8-Specialty Results Table (333 Held-Out Test Records)

| Model Architecture | Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 | Target Exceeded? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Linear SVM (Best Individual)** | **0.8859** | **0.9051** | **0.8902** | **0.8971** | **0.8862** | **YES (+13.59%)** |
| **Soft Voting Ensemble (Best Ensemble)**| **0.8799** | **0.9041** | **0.8795** | **0.8898** | **0.8818** | **YES (+12.99%)** |
| **Logistic Regression (LR)** | **0.8709** | 0.8966 | 0.8768 | 0.8846 | 0.8730 | **YES (+12.09%)** |
| **Hard Voting Ensemble** | **0.8709** | 0.8966 | 0.8768 | 0.8846 | 0.8730 | **YES (+12.09%)** |
| **Random Forest (RF)** | **0.8198** | 0.8340 | 0.8257 | 0.8274 | 0.8209 | **YES (+6.98%)** |
| **Multinomial Naive Bayes (MNB)** | **0.7748** | 0.8602 | 0.7331 | 0.7743 | 0.7824 | **YES (+2.48%)** |

### 6.3 Detailed Classification Report for Linear SVM

| Specialty | Precision | Recall | F1-Score | Support (Test Cases) | Diagnostic Observation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Ophthalmology** | **1.00** | **1.00** | **1.00** | 17 | Flawless generalization; zero misclassifications. |
| **Urology** | **0.97** | 0.90 | **0.93** | 31 | High precision; distinct organ-specific vocabulary. |
| **Obstetrics / Gynecology** | **0.93** | 0.90 | **0.92** | 31 | Excellent specificity on maternal/pelvic notes. |
| **Cardiovascular / Pulmonary** | 0.88 | **0.92** | **0.90** | 74 | Strong recall; reliably captures heart/lung cases. |
| **Orthopedic** | 0.86 | **0.92** | **0.89** | 71 | Robust generalization across fractures and joints. |
| **ENT - Otolaryngology** | **0.94** | 0.84 | **0.89** | 19 | High precision despite smaller class size. |
| **Gastroenterology** | 0.85 | 0.89 | **0.87** | 44 | Stable digestive tract classification. |
| **Neurology** | 0.81 | 0.74 | **0.77** | 46 | Minor confusion with Ortho on spine surgeries. |
| **Macro Average** | **0.91** | **0.89** | **0.90** | **333 Total** | Balanced accuracy across minority & majority. |

---

## 7. 9-Class Open-Set Clinical Triage Inference Engine

### 7.1 Motivation
In real-world hospital environments, incoming dictations may belong to medical departments outside our 8 core specialties (e.g., *Dermatology, Psychiatry, Pediatrics, Dentistry*) or contain non-medical noise. Training an explicit 9th class on raw heterogeneous text collapsed model accuracy to $\approx 41\% - 65\%$. 

### 7.2 Open-Set Decision Architecture (`triage_inference.py`)
To solve this, we implemented an **Open-Set Rejection Architecture**:

```
                       [ Incoming Clinical Text ]
                                   │
                                   ▼
                       [ TF-IDF Vectorization (8k) ]
                                   │
                    ┌──────────────┴──────────────┐
             Vocabulary Overlap?             No Vocabulary?
                    │                             │
                   YES                            NO ──► [ Output: "Other" ]
                    │                                    (Non-Medical Noise)
                    ▼
          [ Soft Voting Ensemble ]
       (Calculate Probabilities P_1 .. P_8)
                    │
                    ▼
           Max Probability >= 48%?
                    │
           ┌────────┴────────┐
          YES                NO
           │                 │
           ▼                 ▼
   [ Output: Core Specialty ] [ Output: "Other" ]
   (e.g., "Cardiovascular")   (Out-of-Scope / Requires Review)
                              + Top Candidate Specialties
```

### 7.3 Verification Test Suite Results
The inference engine was verified across real-world test cases:

```
Test 1: Cardiovascular -> "Cardiovascular / Pulmonary" (67.4% conf) [CONFIRMED SPECIALTY]
Test 2: Ophthalmology  -> "Ophthalmology"             (80.2% conf) [CONFIRMED SPECIALTY]
Test 3: Orthopedic     -> "Orthopedic"                (64.5% conf) [CONFIRMED SPECIALTY]
Test 4: Neurology      -> "Neurology"                 (61.3% conf) [CONFIRMED SPECIALTY]
Test 5: Dermatology    -> "Other"                     (19.7% conf) [OUT OF SCOPE] Candidates: Ortho (19.7%), Cardio (18.9%)
Test 6: Psychiatry     -> "Other"                     (33.7% conf) [OUT OF SCOPE] Candidates: Neuro (33.7%), Cardio (25.3%)
Test 7: Dentistry      -> "Other"                     (25.7% conf) [OUT OF SCOPE] Candidates: Ortho (25.7%), Eye (13.9%)
Test 8: Non-Medical    -> "Other"                     (29.4% conf) [OUT OF SCOPE] Candidates: Neuro (29.4%), Cardio (18.7%)
```

---

## 8. Repository Deliverables & File Structure

The project code is organized cleanly within `model training project/`:

```
d:\Antigravity Projects\Mini Project S3 MCA\
│
├── Dataset\
│   └── mtsamples.csv                         # Original Kaggle dataset (4,999 records)
│
├── model training project\
│   ├── 01_dataset_filtering_and_eda.py       # Data cleaning, whitespace fix & 8-class curation
│   ├── 02_train_and_balance_models.py        # Core ML training, evaluation & serialization script
│   ├── triage_inference.py                   # 9-Class Open-Set Clinical Triage Inference Engine
│   ├── Balanced_Medical_Classification_Pipeline.ipynb # Interactive end-to-end Jupyter Notebook
│   ├── filtered_mtsamples_8classes.csv       # Curated clean dataset (1,663 records)
│   │
│   ├── tfidf_vectorizer_8classes.pkl         # Serialized 8,000-feature vectorizer (0.30 MB)
│   ├── best_balanced_model.pkl               # Serialized Linear SVM classifier (0.49 MB)
│   ├── voting_ensemble_model.pkl             # Serialized Soft Voting Ensemble (11.07 MB)
│   │
│   ├── model_performance_comparison.png      # Clustered bar chart (all models vs 75% threshold)
│   ├── best_model_confusion_matrix.png       # 8x8 heatmap confusion matrix (Soft Voting Ensemble)
│   ├── evaluation_summary.csv                # Complete numerical evaluation benchmark table
│   └── best_model_classification_report.txt  # Detailed per-class precision/recall/F1 metrics
│
├── PROJECT_SUMMARY.md                        # This comprehensive technical report
└── build_interim_presentation.py             # 16-slide PowerPoint compiler (16:9 widescreen)
```

---

## 9. GitHub 100MB File-Size Resolution

During early commits, unconstrained 310,000-feature models produced large pickle files:
* `naive_bayes_model.pkl`: $189.4\text{ MB}$ *(exceeded GitHub's 100 MB hard limit)*
* `random_forest_model.pkl`: $116.2\text{ MB}$

### Resolution Applied:
1. **Dimensional Constraint:** Capping features to 8,000 compressed model files down to **$0.30\text{ MB} - 11.07\text{ MB}$**.
2. **Git Tracking Cleanup:** Configured `.gitignore` to prevent historical large binaries from being staged:
   ```bash
   git reset --soft origin/main
   git reset "MINI Project ML/*.pkl"
   git add .gitignore "model training project/"
   git commit -m "feat: add 9-class ensemble triage pipeline (88.59% accuracy)"
   git push origin main
   ```

---

## 10. Academic Timeline & Milestone Schedule

```
[17.07.2026] Proposal Approval  ──► [20.07.2026] Proposal Presentation ──► [Weeks 1-2] EDA & 184:1 Imbalance
                                                                                   │
[09.09.2026] Sprint Release I   ◄── [08.09.2026] First Presentation     ◄──────────┘
      │
      ▼
[Weeks 3-5] Preprocessing & 8k TF-IDF ──► [Week 6] Candidate Model Training (SVM, LR, RF, MNB)
                                                │
[Week 7] Hyperparameter Tuning        ◄── [18.09.2026] Sprint Release II
      │
      ▼
[Week 8] Soft Voting & Serialization  ──► ★ [29-30.09.2026] Interim Presentation ★ [CURRENT MILESTONE]
                                                │
                                                ▼
[Week 9] Flask REST API & Web UI      ──► [09.10.2026] Sprint Release III
                                                │
                                                ▼
[Weeks 10-11] Latency & Edge Testing  ──► [22-23.10.2026] Final Presentation ──► [30.10.2026] Final Report
```

---

## 11. Viva & Project Defense Guide

### Top 5 Viva Questions & Model Answers

#### Q1: "Why did you reduce from 40 classes down to 8 specialties?"
> *"The raw 40-class dataset contained severe class imbalance (184:1 ratio; Surgery had 1,103 samples while minority classes had under 10), and many classes were administrative document formats (SOAP notes, Consultations, Discharge Summaries) rather than clinical medical specialties. Initial 40-class baselines failed completely (7.85% to 27.39% accuracy). By curating 8 mutually exclusive clinical departments with 1,663 records, we aligned the classification task with real-world hospital triage routing, enabling the models to learn genuine departmental terminology."*

#### Q2: "Why use TF-IDF instead of deep learning (BERT or ClinicalBERT)?"
> *"First, dataset scale: 1,663 records is relatively small; deep transformers (BERT) require tens of thousands of samples to prevent severe overfitting. Second, inference speed and hardware efficiency: our 8,000-feature TF-IDF pipeline executes in under 12 milliseconds on a standard CPU and produces an ultra-compact 11.9 MB bundle, compared to BERT's gigabyte-scale RAM requirements and 300ms latency. Third, high-dimensional text separability: an 8,000-dimensional unigram/bigram representation provides clear linear separability, allowing Linear SVM to achieve 88.59% accuracy."*

#### Q3: "Why did Linear SVM outperform the Soft Voting Ensemble by 0.6%?"
> *"Linear SVM maximizes the geometric margin between high-dimensional sparse TF-IDF vectors, which is mathematically optimal for text classification. However, Soft Voting combining SVM, Logistic Regression, Random Forest, and Naive Bayes outputs continuous calibrated class probabilities (0.0 to 1.0). This enables our clinical triage interface to display confidence distributions and reliably flag uncertain cases (< 48%) as 'Other'."*

#### Q4: "How does the system handle cases outside the 8 specialties?"
> *"We built an Open-Set Triage Inference Engine (`triage_inference.py`). When an incoming note belongs to an outside department (like Dermatology, Psychiatry, or Pediatrics), the ensemble's predicted probability across the 8 specialties is diffuse and falls below our 48% threshold. The engine automatically classifies it as 'Other' and returns the top nearest candidate departments for manual clinician review."*

#### Q5: "What was completed in Phase 1 vs. Phase 2?"
> *"Phase 1 was strictly dedicated to dataset understanding, exploratory data analysis, class frequency auditing, and identifying the 184:1 class imbalance. No machine learning models were trained in Phase 1. All baseline evaluations, dataset curation, TF-IDF engineering, model training, hyperparameter tuning, soft voting ensembles, and serialization were completed in Phase 2."*

---
*Report compiled and verified for MCA Mini Project Phase 2 & 3.*
