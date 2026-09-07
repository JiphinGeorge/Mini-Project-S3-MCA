import pptx

pptx_path = r"D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation.pptx"
prs = pptx.Presentation(pptx_path)

notes_content = {
    # -------------------------------------------------------------
    # SLIDE 1
    # -------------------------------------------------------------
    1: """[FORMAL PRESENTATION SCRIPT]
Respected Guide Prof. Biju Skaria, Chairperson, and esteemed members of the evaluation committee, good morning. 

I am Jiphin George, Register Number MAC25MCA-2033, pursuing my Master of Computer Applications at Mar Athanasius College of Engineering, Kothamangalam. Today, I am privileged to present the first review of my MCA Mini Project titled: 'Medical Specialty Classification Using TF-IDF and Ensemble Machine Learning'.

[KEY TECHNICAL HIGHLIGHTS]
• Domain Problem: Healthcare systems generate thousands of unstructured clinical dictations daily. Manually reading and routing these to medical departments causes clinical delays, high administrative costs, and coding inconsistencies.
• Proposed Solution: An automated, lightweight, and explainable NLP and Machine Learning classification system capable of classifying medical transcripts into 40 medical specialties.
• Architectural Pillars:
  1. Clinical NLP Normalization (cleaning, tokenization, stopword removal, WordNet lemmatization).
  2. Sublinear TF-IDF Feature Vectorization (unigrams + bigrams with L2 normalization).
  3. Soft Voting Ensemble combining 4 diverse classifiers: Linear SVM, Random Forest, Multinomial Logistic Regression, and Multinomial Naive Bayes.
  4. Lightweight Flask Web Deployment running in real-time on standard commodity CPU hardware without requiring expensive GPUs.

[TRANSITION TO NEXT SLIDE]
Let us begin by examining the underlying problem statement and the core objectives guiding this project.""",

    # -------------------------------------------------------------
    # SLIDE 2
    # -------------------------------------------------------------
    2: """[FORMAL PRESENTATION SCRIPT]
Moving to Slide 2, let us look closely at why automated clinical specialty categorization is a vital healthcare informatics challenge.

As shown on the left, clinical narratives are inherently unstructured, written in dense physician shorthand with complex jargon, abbreviations, and variable lengths. In hospitals, medical coders manually inspect these narratives to assign departmental specialty tags. This process is time-consuming, prone to human fatigue, expensive, and inconsistent across coders.

Our objective, shown on the right, is to design and implement an end-to-end Machine Learning pipeline that automates this categorization, speeding up document routing and eliminating administrative bottlenecks.

[KEY OBJECTIVES EXPLAINED]
1. Explore & Analyze: Conduct exhaustive statistical and exploratory analysis on the Kaggle MTSamples clinical transcription dataset across all 40 specialties.
2. Preprocess Text: Build a robust 5-step clinical NLP cleaning sequence to eliminate noise while preserving clinical root meanings.
3. Extract Features: Transform raw text into standardized, high-dimensional numerical feature vectors using sublinear TF-IDF.
4. Ensemble & Deploy: Train and ensemble four diverse machine learning models via soft voting to handle severe class imbalance, deploying the finalized model through an interactive Flask web application.

[TRANSITION TO NEXT SLIDE]
To ground our methodology in established research, I conducted an extensive review of the literature, summarized on Slide 3.""",

    # -------------------------------------------------------------
    # SLIDE 3
    # -------------------------------------------------------------
    3: """[FORMAL PRESENTATION SCRIPT]
Slide 3 presents the academic context, theoretical foundation, and research landscape of clinical text classification.

The top phase bar outlines our research progression:
1. Prior Literature: Validated the feasibility of supervised machine learning for clinical text classification.
2. Key Methodologies: Established TF-IDF vectorization and linear classifiers as strong, interpretable baselines.
3. Identified Gap: Deep learning approaches (such as BERT or ClinicalBERT) achieve high benchmarks but demand massive GPU compute, suffer from long inference latency, and show high variance when trained on severely imbalanced text data.
4. Proposed Architecture: A lightweight Soft Voting Ensemble designed to achieve robust multi-class accuracy across all 40 specialties on standard CPU hardware.

[FOUR CORE METHODOLOGICAL PILLARS]
• Clinical NLP & Preprocessing: Clinical dictations contain non-standard abbreviations and punctuation noise. We implement a systematic 5-stage cleaning sequence (HTML/noise removal, case normalization, regex tokenization, clinical stopword removal, and morphological lemmatization) that normalizes inflected clinical terms to their diagnostic roots.
• TF-IDF Feature Representation: Converts unstructured narratives into high-dimensional sparse numerical vectors. Sublinear scaling (1 + log(TF)) dampens repetitive non-informative terms while highlighting discriminative clinical tokens. L2 normalization handles document length variations.
• Supervised ML Classifiers: Linear models (SVM, Logistic Regression) excel on high-dimensional sparse text vectors; Random Forest introduces non-linear decision boundaries and bagging variance reduction; Multinomial Naive Bayes provides fast probabilistic likelihood estimation.
• Ensemble Learning & Research Gap: Single models often struggle with rare classes under severe imbalance. Combining calibrated base models through soft probability voting balances variance and achieves superior generalization.

[TRANSITION TO NEXT SLIDE]
Let us now examine three specific peer-reviewed papers that directly informed our methodological design on Slide 4.""",

    # -------------------------------------------------------------
    # SLIDE 4
    # -------------------------------------------------------------
    4: """[FORMAL PRESENTATION SCRIPT]
On Slide 4, I have synthesized three pivotal research publications that directly influenced our pipeline design.

[PAPER 1: Omar et al. (2023, iJOE)]
• Methodology: Compared classical feature representations (Bag-of-Words, TF-IDF, Word2Vec) across multiple classifiers including Logistic Regression, SVM, Naive Bayes, and k-NN.
• Key Finding: Word2Vec + k-NN achieved the highest accuracy at 92%, but distance-based k-NN scales poorly during inference on large, expanding hospital databases.
• Relevance: Validated the standard 4-phase preprocessing pipeline and guided us toward parametric, computationally lightweight linear and ensemble classifiers.

[PAPER 2: Zhang et al. (2023, Hindawi CIN)]
• Methodology: Explored SemiADA synthetic data augmentation paired with BERT on an 18-class MTSamples subset.
• Key Finding: Demonstrated that class imbalance is the primary cause of clinical classification error, achieving a +14.9% gain with augmentation, but at the cost of heavy GPU fine-tuning overhead.
• Relevance: Highlighted the extreme class imbalance in MTSamples and motivated our approach: an accessible TF-IDF + soft voting ensemble that mitigates imbalance through probability calibration without requiring expensive GPU clusters.

[PAPER 3: Blanchard et al. (2022, IEEE JBHI)]
• Methodology: Designed a CNN with keyword-constrained loss for cancer pathology text on the NCI SEER registry.
• Key Finding: Proved that clinical keywords carry the bulk of diagnostic signal; keyword weighting significantly improved macro-F1 and recall on rare classes without hurting majority performance.
• Relevance: Justified our choice of sublinear TF-IDF with n-gram weighting to preserve and amplify predictive medical terms for rare specialty classes.

[TRANSITION TO NEXT SLIDE]
With this literature background established, let us inspect the empirical dataset used in this research, shown on Slide 5.""",

    # -------------------------------------------------------------
    # SLIDE 5
    # -------------------------------------------------------------
    5: """[FORMAL PRESENTATION SCRIPT]
Slide 5 introduces the dataset: the Kaggle MTSamples Medical Transcriptions dataset, a well-established open-source benchmark in healthcare text analytics.

[DATASET SPECIFICATIONS & SCHEMA]
• Source: Authentic clinical dictations transcribed from MTSamples.com, covering real-world patient histories, physical exams, diagnostic consultations, and operative notes.
• Scale: Exactly 4,999 clinical records categorized into 40 distinct medical specialties.
• 6 Attributes:
  1. Unnamed: 0: Integer row identifier / index.
  2. description: Short 1–2 sentence summary of the clinical encounter.
  3. medical_specialty: The ground-truth categorical target label spanning 40 clinical classes.
  4. sample_name: Specific clinical dictation or procedure heading.
  5. transcription: The primary independent feature containing the unstructured narrative text.
  6. keywords: Comma-separated extracted medical keywords.

[INITIAL QUALITY AUDIT]
• Data Completeness: The target attribute `medical_specialty` has 0 missing values across all 4,999 rows (100% complete).
• Feature Completeness: The `transcription` narrative is 99.34% complete, with only 33 null records (0.66%).
• High Sparsity in Keywords: `keywords` is missing in 1,068 records (21.36%), confirming that we must extract features directly from raw transcription text rather than relying on keywords.

[TRANSITION TO NEXT SLIDE]
On Slide 6, we examine the statistical verification and structural profiling performed on this dataset.""",

    # -------------------------------------------------------------
    # SLIDE 6
    # -------------------------------------------------------------
    6: """[FORMAL PRESENTATION SCRIPT]
Slide 6 presents the statistical profiling of the dataset conducted using Python's pandas and NumPy libraries.

[STATISTICAL VERIFICATION]
• Programmatic Inspection: We applied standard DataFrame inspection methods: `df.shape`, `df.info()`, `df.dtypes`, `df.describe()`, `df.head()`, and `df.memory_usage(deep=True)`.
• Dimensions: Verified exact dimensions of 4,999 observations and 6 attributes.
• Data Types: Confirmed 1 integer index column and 5 object (string) columns. Total memory usage in pandas is approximately 25 megabytes.
• Text Description Analysis: Descriptive statistics confirm that `transcription` is free-form natural language text of highly variable length and rich clinical vocabulary.
• Deduplication Check: Checked via `df.duplicated(subset=['transcription'])`. Confirmed no duplicate clinical narratives in the corpus, ruling out artificial memorization or data leakage.

[TRANSITION TO NEXT SLIDE]
Next, on Slide 7, we visualize our missing value audit across all dataset attributes.""",

    # -------------------------------------------------------------
    # SLIDE 7
    # -------------------------------------------------------------
    7: """[FORMAL PRESENTATION SCRIPT]
Slide 7 visualizes the data quality audit, specifically analyzing missing values across all dataset fields using pandas `isnull().sum()`, rendered with Seaborn and Matplotlib.

[DATA QUALITY AUDIT FINDINGS]
• `transcription` (Primary Feature): 33 missing values out of 4,999 (0.66%). In text classification, imputing missing free-form narrative text is statistically invalid. Because 0.66% is negligible, dropping these 33 rows leaves 4,966 high-integrity records with zero synthetic distortion.
• `keywords`: 1,068 missing records (21.36%). This severe sparsity validates our architectural choice to discard `keywords` and derive our own TF-IDF feature space directly from the full transcription text.
• `description`: 6 missing records (0.12%).
• `medical_specialty` (Target Label): 0 missing records (0.00%). Every record is deterministically labeled, providing a clean ground truth for supervised multi-class learning.

[TRANSITION TO NEXT SLIDE]
Let us now turn to Slide 8 to analyze the distribution of our target variable, which reveals our primary modeling challenge: class imbalance.""",

    # -------------------------------------------------------------
    # SLIDE 8
    # -------------------------------------------------------------
    8: """[FORMAL PRESENTATION SCRIPT]
Slide 8 displays the complete distribution across all 40 medical specialty classes in the MTSamples dataset, generated using Seaborn and Matplotlib.

[CLASS IMBALANCE ANALYSIS]
• Extreme Imbalance Ratio: The dataset exhibits a severe long-tail Pareto distribution:
  - Majority Class: 'Surgery' dominates with 1,103 records (over 22% of the entire dataset).
  - Next Largest Classes: 'Consult - History and Phy.' has 516 records, and 'Cardiovascular / Pulmonary' has 371 records.
  - Minority Classes: Rare specialties at the tail have very few samples—'Autopsy' and 'Executive Evaluation' have only 2 records each; 'Hospice - Palliative Care' has only 6 records.
• Why This Matters for Modeling:
  1. Standard train/test splitting would randomly place rare classes entirely in the training set or test set, causing evaluation failure. A strictly stratified train-test split (`stratify=y`) is mandatory.
  2. Standard Accuracy is a misleading metric under severe imbalance (a naive model predicting 'Surgery' always would achieve ~22% accuracy). Evaluation must rely on Macro-averaged Precision, Recall, and F1-score.
  3. Classifiers must incorporate cost-sensitive weighting (`class_weight='balanced'`) and probability calibration.

[TRANSITION TO NEXT SLIDE]
Having analyzed the target labels, on Slide 9 we inspect the linguistic characteristics of the clinical narratives.""",

    # -------------------------------------------------------------
    # SLIDE 9
    # -------------------------------------------------------------
    9: """[FORMAL PRESENTATION SCRIPT]
Slide 9 examines the word count distribution and clinical vocabulary extracted from the transcription narratives.

[TEXT LENGTH & VOCABULARY INSIGHTS]
• Word Count Distribution (Left Chart):
  - Highly right-skewed distribution. The median narrative length is approximately 435 words, with the interquartile range between 210 and 680 words.
  - However, comprehensive surgical and operative notes extend up to nearly 3,000 words.
  - This extreme variability justifies document-level L2 normalization in TF-IDF, ensuring that lengthy documents do not artificially dominate feature magnitudes.
• Word Cloud of High-Frequency Terms (Right Chart):
  - Generated using the Python `wordcloud` library.
  - Prominent terms include 'patient', 'procedure', 'left', 'right', 'placed', 'noted', 'history', 'normal', 'tolerated'.
  - These ubiquitous terms represent generic clinical documentation boilerplate common across almost all hospital encounters.
  - Without proper Inverse Document Frequency (IDF) down-weighting and clinical stopword filtering, these frequent words act as noise and overpower discriminative specialty terms (e.g., 'myocardial', 'laparoscopic', 'electroencephalogram').

[TRANSITION TO NEXT SLIDE]
Slide 10 synthesizes these empirical findings into four foundational modeling conclusions.""",

    # -------------------------------------------------------------
    # SLIDE 10
    # -------------------------------------------------------------
    10: """[FORMAL PRESENTATION SCRIPT]
Slide 10 synthesizes the four key insights derived from our exploratory data analysis that directly dictate our preprocessing, feature engineering, and modeling strategies.

[FOUR CORE CONCLUSIONS]
1. Severe Class Imbalance (1,103 vs. 2 records):
   - Strategy: Mandatory stratified 80:20 data splitting, balanced cost-sensitive sample weighting, and ensemble voting to prevent majority class bias.
2. Variable Text Length (200 to 3,000 words):
   - Strategy: Sublinear TF scaling (1 + log(TF)) to dampen high-frequency repetition, paired with document-level L2 vector normalization.
3. High-Dimensional Text Vocabulary:
   - Strategy: Set minimum document frequency (`min_df=3`) to eliminate single-occurrence spelling noise, and maximum document frequency (`max_df=0.85`) to exclude ubiquitous words, capturing unigrams and bigrams.
4. Generic Documentation Noise:
   - Strategy: Combine NLTK standard English stopwords with clinical-specific boilerplate tokens, followed by WordNet morphological lemmatization.
5. Evaluation Metric: Overall accuracy alone is deceptive under severe imbalance; model success will be evaluated using Macro-averaged Precision, Recall, and F1-Score.

[TRANSITION TO NEXT SLIDE]
On Slide 11, we examine the pre-processed dataset structure ready for machine learning.""",

    # -------------------------------------------------------------
    # SLIDE 11
    # -------------------------------------------------------------
    11: """[FORMAL PRESENTATION SCRIPT]
Slide 11 contrasts the raw ingested dataset against the clean, preprocessed data structure established for model training.

[CLEANED DATASET STRUCTURE]
• Drop Null Records: Removed the 33 records with missing transcriptions, yielding a clean dataset of 4,966 high-quality rows spanning all 40 original medical specialties.
• Feature Matrix ($X$): The cleaned `transcription` narrative text.
• Target Variable ($y$): The categorical `medical_specialty` label, encoded into numerical format via scikit-learn's `LabelEncoder`.
• Stratified Train-Test Split:
  - 80% Training Set (3,972 samples) : 20% Test Set (994 samples).
  - Stratification ensures that all 40 specialties—including the rarest classes—are proportionally represented in both training and test partitions.
• Strict Data Leakage Prevention: The TF-IDF Vectorizer is fitted strictly on the training partition (`fit_transform`). The test set is strictly transformed (`transform`) using frozen vocabulary and IDF weights, ensuring no data snooping or leakage occurs.

[TRANSITION TO NEXT SLIDE]
Slide 12 introduces our proposed machine learning algorithms and ensemble architecture.""",

    # -------------------------------------------------------------
    # SLIDE 12
    # -------------------------------------------------------------
    12: """[FORMAL PRESENTATION SCRIPT]
Slide 12 presents our proposed classification architecture, combining four diverse base machine learning models into an overarching Soft Voting Ensemble.

[TOP 4 BASE CLASSIFIERS]
1. Support Vector Machine (Linear Kernel): Finds the maximum-margin separating hyperplane. Proven mathematically to excel on sparse, high-dimensional text feature spaces where the number of features exceeds the number of samples.
2. Random Forest Classifier: An ensemble of decision trees utilizing bootstrap aggregation (bagging). Captures non-linear keyword interactions and provides variance reduction.
3. Logistic Regression (Multinomial / Softmax): Provides a well-calibrated probabilistic baseline with L2 regularization, generating interpretable posterior odds ratios for clinical features.
4. Multinomial Naive Bayes: A fast, count-based probabilistic classifier using Laplace smoothing. Computationally efficient and highly effective on word frequency distributions.

[BOTTOM 3 STAGES: PIPELINE ARCHITECTURE]
• Feature Extraction: TF-IDF vectorizer extracts unigrams and bigrams with sublinear TF scaling and L2 normalization, producing a standardized sparse matrix.
• Classification: The four base estimators independently evaluate the sparse vector and generate class probability distributions.
• Ensemble Aggregation: A Soft Voting Classifier aggregates consensus probabilities across all four base models: P_ensemble(c) = 1/4 * sum(P_m(c)). The predicted specialty corresponds to argmax(P_ensemble).

[TRANSITION TO NEXT SLIDE]
Let us now examine the formal UML Activity Diagrams for each algorithm, starting with SVM and Naive Bayes on Slide 13.""",

    # -------------------------------------------------------------
    # SLIDE 13
    # -------------------------------------------------------------
    13: """[FORMAL PRESENTATION SCRIPT]
Slide 13 displays the formal UML Activity Diagrams for our first two classifiers—Support Vector Machine on the left and Multinomial Naive Bayes on the right—extracted directly from Figures 7 and 8 of our project report.

[DETAILED STEP-BY-STEP ACTIVITY DIAGRAM WALKTHROUGH]

• LEFT DIAGRAM: SVM Model Training & Classification (Figure 7):
  1. Initial Node (Black Circle): Ingestion of preprocessed clinical transcription text.
  2. TF-IDF Vectorization Activity: Converts the clinical text into a high-dimensional numerical sparse feature vector.
  3. Hyperplane Optimization: Solves the convex quadratic programming dual problem: finding the maximum-margin hyperplane separating specialty classes using a linear kernel K(x_i, x_j) = x_i^T x_j.
  4. Decision Node (Platt Scaling / Probability Calibration): Because standard SVM outputs uncalibrated geometric margins, Platt scaling (logistic sigmoid fitting) is applied to convert margins into well-calibrated class probability distributions P(y|x) necessary for soft voting.
  5. Multi-Class Decision: One-vs-Rest (OvR) decision strategy constructs 40 binary decision boundaries.
  6. Output & Terminal Node: Outputs the calibrated probability vector and predicted specialty class.

• RIGHT DIAGRAM: Multinomial Naive Bayes (Figure 8):
  1. Initial Node: Ingestion of tokenized transcription feature vector.
  2. Prior & Likelihood Computation: Computes class prior log-probabilities log P(c) and feature likelihoods log P(w_i | c).
  3. Laplace Smoothing Activity: Applies additive Laplace smoothing (alpha = 1.0) to prevent zero-probability errors on words absent in specific classes: P(w_i|c) = (N_ci + 1) / (N_c + |V|).
  4. Posterior Likelihood Aggregation: Sums log-likelihoods over all tokens to prevent floating-point underflow: log P(c) + sum(log P(w_i | c)).
  5. Softmax Normalization: Normalizes posterior log-odds into a calibrated probability distribution across all 40 specialties.
  6. Terminal Node: Outputs probability distribution to the ensemble aggregator.

[TRANSITION TO NEXT SLIDE]
Slide 14 presents the activity diagrams for our remaining two base estimators: Random Forest and Logistic Regression.""",

    # -------------------------------------------------------------
    # SLIDE 14
    # -------------------------------------------------------------
    14: """[FORMAL PRESENTATION SCRIPT]
Slide 14 displays the formal UML Activity Diagrams for Random Forest on the left and Logistic Regression on the right, corresponding to Figures 9 and 10 in our project report.

[DETAILED STEP-BY-STEP ACTIVITY DIAGRAM WALKTHROUGH]

• LEFT DIAGRAM: Random Forest Classifier (Figure 9):
  1. Initial Node: Ingestion of TF-IDF feature matrix.
  2. Fork Bar (Parallel Bootstrap Sampling): Splits the training process across an ensemble of B decision trees (n_estimators=100) via Bootstrap Aggregation (Bagging).
  3. Random Feature Subspace Split: At each split node of every tree, a random subset of features (sqrt(D)) is evaluated to maximize Gini Impurity reduction: Gini = 1 - sum(p_i^2).
  4. Tree Growing: Decision trees grow independently without pruning down to minimum leaf size.
  5. Join Bar (Ensemble Synchronization): Gathers predictions across all parallel decision trees.
  6. Probability Averaging Activity: Averages leaf node class distributions across all trees: P_RF(c) = 1/B * sum(p_b(c)).
  7. Terminal Node: Outputs the aggregated ensemble probability distribution.

• RIGHT DIAGRAM: Multinomial Logistic Regression (Figure 10):
  1. Initial Node: Ingestion of TF-IDF feature vector.
  2. Logit Linear Combination: Evaluates linear log-odds for each specialty class: z_k = w_k^T x + b_k.
  3. Multinomial Softmax Activation: Converts raw logit scores into valid probabilities summing to 1: P(y=k|x) = exp(z_k) / sum(exp(z_j)).
  4. L2 Regularized Cross-Entropy Optimization: Optimizes the cross-entropy loss function with Ridge penalty (lambda/2 * ||w||^2) using the L-BFGS quasi-Newton optimization solver.
  5. Class Weight Balancing Activity: Adjusts gradient weights inversely proportional to class frequencies to counteract class imbalance.
  6. Terminal Node: Outputs calibrated multi-class posterior probability vector.

[TRANSITION TO NEXT SLIDE]
On Slide 15, we see how these four streams converge into our Soft Voting Ensemble architecture.""",

    # -------------------------------------------------------------
    # SLIDE 15
    # -------------------------------------------------------------
    15: """[FORMAL PRESENTATION SCRIPT]
Slide 15 illustrates the architectural synthesis and complete UML Activity Diagram of our Soft Voting Ensemble Model, corresponding directly to Figure 12 in the project report.

[DETAILED STEP-BY-STEP ENSEMBLE ACTIVITY FLOW]
1. Initial Node (Start): A raw clinical transcription text string is received by the system.
2. Clinical NLP Preprocessing: The string is cleaned, lowercased, tokenized, filtered for stopwords, and morphologically lemmatized.
3. TF-IDF Feature Extraction: The normalized token stream is transformed into a standardized numerical sparse vector x using the fitted vocabulary.
4. Fork Bar (Concurrent Classifier Evaluation): The feature vector x is broadcast simultaneously to all four trained base estimators:
   - Branch A: Linear SVM (Platt Calibrated) -> computes P_SVM(c)
   - Branch B: Random Forest Classifier -> computes P_RF(c)
   - Branch C: Logistic Regression (Softmax) -> computes P_LR(c)
   - Branch D: Multinomial Naive Bayes -> computes P_MNB(c)
5. Join Bar (Probability Matrix Collection): Synchronizes and collects the four 40-dimensional probability vectors into a unified consensus matrix.
6. Soft Voting Aggregation Activity: Evaluates the unweighted/weighted arithmetic mean: P_ensemble(c) = 1/4 * [ P_SVM(c) + P_RF(c) + P_LR(c) + P_MNB(c) ].
7. Argmax Decision Node: Evaluates y_hat = argmax_c P_ensemble(c) to select the specialty with the highest consensus confidence.
8. Terminal Node (End): Returns the predicted medical specialty along with top-3 candidate confidence scores.

[THEORETICAL ADVANTAGE OF SOFT VOTING]
Unlike Hard Majority Voting (which counts discrete votes and discards confidence), Soft Voting weights predictions by continuous model certainty. If SVM and Logistic Regression are 90% confident on 'Cardiology', they overpower weak 51% majority ties from other models, significantly reducing error variance.

[TRANSITION TO NEXT SLIDE]
Slide 16 presents the complete end-to-end macro system pipeline covering training, persistence, and web deployment.""",

    # -------------------------------------------------------------
    # SLIDE 16
    # -------------------------------------------------------------
    16: """[FORMAL PRESENTATION SCRIPT]
Slide 16 presents the macro-level UML Activity Diagram for the complete project lifecycle, corresponding to Figure 13 of the project report.

[DETAILED END-TO-END PIPELINE WALKTHROUGH]

• STAGE 1: Offline Data Preparation & Model Training:
  1. Data Ingestion: Loads the raw Kaggle MTSamples CSV (4,999 records).
  2. Data Audit & Cleansing: Drops 33 null transcription records, retaining 4,966 clean rows.
  3. Stratified Partitioning: Splits into 80% train (3,972) and 20% test (994) partitions with preserved class ratios.
  4. TF-IDF Fitting: Fits vectorizer strictly on training data; transforms test data.
  5. Multi-Model Training: Trains SVM, Random Forest, Logistic Regression, and Multinomial Naive Bayes.
  6. Soft Voting Ensemble Assembly: Chains models into a scikit-learn VotingClassifier(voting='soft').
  7. Evaluation & Validation: Computes Precision, Recall, Macro-F1, and generates confusion matrices.
  8. Model Serialization: Persists finalized pipeline objects (`voting_model.pkl` and `tfidf_vectorizer.pkl`) to disk via Python `joblib` / `pickle`.

• STAGE 2: Online Real-Time Inference & Flask Web Deployment:
  1. User Input: Clinician enters or pastes a clinical narrative into the web GUI.
  2. HTTP Request: Browser dispatches POST request with text payload to Flask backend.
  3. Deserialization & Pipeline Execution: Flask loads serialized artifacts, executes identical NLP preprocessing and TF-IDF vectorization.
  4. Soft Voting Inference: The ensemble predicts the top medical specialty and confidence scores in under 200 milliseconds.
  5. Response Rendering: Formatted JSON/HTML results are displayed on the clinician's dashboard.

[TRANSITION TO NEXT SLIDE]
Slide 17 summarizes our project progress and implementation roadmap.""",

    # -------------------------------------------------------------
    # SLIDE 17
    # -------------------------------------------------------------
    17: """[FORMAL PRESENTATION SCRIPT]
Slide 17 presents our current project implementation status and roadmap across all four project phases.

[PHASE-BY-PHASE STATUS]
• Phase 1: Problem Formulation & Literature Review (100% COMPLETED):
  - Conducted extensive literature review of text mining in clinical domains.
  - Formulated problem statement, technical objectives, and scope.
  - Established project repository and version-controlled codebase.
• Phase 2: Dataset Acquisition & Exploratory Data Analysis (100% COMPLETED):
  - Ingested and profiled all 4,999 MTSamples records across 40 classes.
  - Completed missing value analysis, deduplication, and class distribution audits.
  - Implemented 5-step clinical NLP cleaning pipeline and verified zero data leakage.
• Phase 3: Model Development & Ensemble Optimization (IN PROGRESS - 40% COMPLETED):
  - Implemented baseline classifiers: Linear SVM, Random Forest, Logistic Regression, and MNB.
  - Currently tuning hyperparameters using Stratified 5-fold cross-validation with GridSearchCV.
  - Calibrating probability estimators for optimal soft voting weights.
• Phase 4: Web Application Deployment & Evaluation (UPCOMING - 0% COMPLETED):
  - Building lightweight Flask application backend with REST API endpoint.
  - Designing clean, responsive web interface for clinical text submission.
  - Conducting stress testing, latency benchmarking, and final report compilation.

[CORE TECHNOLOGY STACK]
Python 3.10+, Scikit-Learn, Pandas, NumPy, NLTK, Matplotlib, Seaborn, Flask, HTML5/CSS3.

[TRANSITION TO NEXT SLIDE]
On Slide 18, we review the project execution timeline, milestone schedule, and risk management strategies.""",

    # -------------------------------------------------------------
    # SLIDE 18
    # -------------------------------------------------------------
    18: """[FORMAL PRESENTATION SCRIPT]
Slide 18 details our structured 16-week project execution timeline, key milestones M1 through M6, and risk management strategies.

[16-WEEK TIMELINE & MILESTONES]
• Weeks 1–4 (Month 1): Problem formulation, literature survey, environment setup. -> Milestone M1: Topic Approval & Feasibility Report.
• Weeks 5–8 (Month 2): Dataset acquisition, EDA, data quality audit, baseline NLP pipeline. -> Milestone M2: EDA Completion & Initial Project Review (CURRENT REVIEW).
• Weeks 9–12 (Month 3): Advanced feature engineering, ensemble optimization, hyperparameter tuning via GridSearchCV. -> Milestone M3: Model Optimization & Milestone M4: Internal Review.
• Weeks 13–16 (Month 4): Flask web app development, UI integration, latency benchmarking, final documentation. -> Milestone M5: Web Deployment & Milestone M6: Final Defense.

[RISK MANAGEMENT & MITIGATION STRATEGIES]
• Risk 1 (Extreme Class Imbalance): Mitigated via stratified splitting, cost-sensitive class weighting (`class_weight='balanced'`), and soft probability aggregation.
• Risk 2 (Inference Latency): Mitigated by choosing sublinear TF-IDF over heavy deep learning models, enabling sub-200ms CPU inference.
• Risk 3 (Data Leakage): Mitigated by strictly fitting the vectorizer on training data and applying frozen transforms on test sets.
• Risk 4 (High-Dimensional Sparsity): Mitigated by frequency pruning (`min_df=3`, `max_df=0.85`) and L2 regularization in base models.

[TRANSITION TO NEXT SLIDE]
This brings me to the conclusion of my presentation on Slide 19.""",

    # -------------------------------------------------------------
    # SLIDE 19
    # -------------------------------------------------------------
    19: """[FORMAL PRESENTATION SCRIPT]
Thank you, respected Guide Prof. Biju Skaria, Chairperson, and distinguished members of the evaluation committee, for your time, patient listening, and constructive guidance.

[SUMMARY RECAP]
In summary, this first review has demonstrated:
1. A rigorous formulation of the automated clinical transcription classification problem.
2. Comprehensive exploratory data analysis across all 4,999 records and 40 medical specialties.
3. Concrete architectural solutions to mitigate severe class imbalance, high vocabulary dimensionality, and document length variance.
4. A clear, scientifically validated UML activity workflow for our four base estimators and Soft Voting Ensemble.

I am deeply grateful for your feedback and now warmly open the floor for your questions, suggestions, and technical discussion."""
}

print("Setting detailed speaker notes for all 19 slides...")

for slide_num, text in notes_content.items():
    slide = prs.slides[slide_num - 1]
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = text
    print(f" Slide {slide_num}: Notes set successfully ({len(text)} characters).")

prs.save(pptx_path)
print("\nSaved updated presentation to:", pptx_path)
