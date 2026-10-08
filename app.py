import os
import re
import time
import joblib
import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
import fitz  # PyMuPDF for high-speed PDF text extraction
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file upload

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model training project")

# Path to serialized ML artifacts
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer_8classes.pkl")
VOTING_MODEL_PATH = os.path.join(MODEL_DIR, "voting_ensemble_model.pkl")

# Verify and load ML artifacts
print(f"Loading TF-IDF Vectorizer from: {VECTORIZER_PATH}")
vectorizer = joblib.load(VECTORIZER_PATH)

print(f"Loading Voting Ensemble Model from: {VOTING_MODEL_PATH}")
ensemble_model = joblib.load(VOTING_MODEL_PATH)
classes_list = list(ensemble_model.classes_)
feature_names = vectorizer.get_feature_names_out()

print(f"Model successfully initialized with {len(classes_list)} classes and {len(feature_names)} vocabulary features.")

# Model Performance Benchmark Data (from held-out 333 test samples)
MODEL_BENCHMARKS = {
    "svm": {
        "name": "Linear SVM (SGD / LinearSVC)",
        "accuracy": 88.59,
        "macro_f1": 0.8971,
        "macro_precision": 0.9051,
        "macro_recall": 0.8902,
        "weighted_f1": 0.8862,
        "weight": 2,
        "is_best_individual": True,
        "description": "High-margin hyperplane separator optimizing maximum clinical text distinction."
    },
    "ensemble": {
        "name": "Soft Voting Ensemble",
        "accuracy": 87.99,
        "macro_f1": 0.8898,
        "macro_precision": 0.9041,
        "macro_recall": 0.8795,
        "weighted_f1": 0.8818,
        "weight": "2:2:1:1",
        "is_best_ensemble": True,
        "description": "Probability-weighted consensus synthesizing margins and calibrated posteriors."
    },
    "lr": {
        "name": "Logistic Regression",
        "accuracy": 87.09,
        "macro_f1": 0.8846,
        "macro_precision": 0.8966,
        "macro_recall": 0.8768,
        "weighted_f1": 0.8730,
        "weight": 2,
        "description": "L2-regularized multinomial logistic regression with well-calibrated odds."
    },
    "rf": {
        "name": "Random Forest",
        "accuracy": 81.98,
        "macro_f1": 0.8274,
        "macro_precision": 0.8340,
        "macro_recall": 0.8257,
        "weighted_f1": 0.8209,
        "weight": 1,
        "description": "Non-linear decision tree ensemble capturing interaction terms."
    },
    "mnb": {
        "name": "Multinomial Naive Bayes",
        "accuracy": 77.48,
        "macro_f1": 0.7743,
        "macro_precision": 0.8602,
        "macro_recall": 0.7331,
        "weighted_f1": 0.7824,
        "weight": 1,
        "description": "Probabilistic frequency baseline under conditional independence assumption."
    }
}

DATASET_STATS = {
    "corpus": "MTSamples Medical Transcriptions",
    "raw_records": 4999,
    "curated_records": 1663,
    "supported_specialties": 8,
    "train_records": 1330,
    "test_records": 333,
    "split_ratio": "80% Train / 20% Test",
    "balancing": "Stratified Sampling with Class Weights",
    "open_set_threshold": 0.48
}

CONFUSION_MATRIX_DATA = {
    "classes": classes_list,
    "matrix": [
        [69, 0, 2, 2, 0, 0, 1, 0],
        [3, 15, 0, 1, 0, 0, 0, 0],
        [1, 0, 40, 2, 2, 0, 0, 0],
        [2, 1, 0, 36, 0, 0, 6, 0],
        [2, 0, 0, 0, 29, 0, 0, 0],
        [0, 0, 0, 1, 0, 16, 0, 0],
        [0, 0, 0, 11, 0, 0, 60, 0],
        [0, 0, 3, 0, 0, 0, 0, 28]
    ]
}

CLASSIFICATION_REPORT_DATA = [
    {"specialty": "Cardiovascular / Pulmonary", "precision": 0.90, "recall": 0.93, "f1": 0.91, "support": 74},
    {"specialty": "ENT - Otolaryngology", "precision": 0.94, "recall": 0.79, "f1": 0.86, "support": 19},
    {"specialty": "Gastroenterology", "precision": 0.89, "recall": 0.89, "f1": 0.89, "support": 45},
    {"specialty": "Neurology", "precision": 0.68, "recall": 0.80, "f1": 0.73, "support": 45},
    {"specialty": "Obstetrics / Gynecology", "precision": 0.94, "recall": 0.94, "f1": 0.94, "support": 31},
    {"specialty": "Ophthalmology", "precision": 1.00, "recall": 0.94, "f1": 0.97, "support": 17},
    {"specialty": "Orthopedic", "precision": 0.90, "recall": 0.85, "f1": 0.87, "support": 71},
    {"specialty": "Urology", "precision": 1.00, "recall": 0.90, "f1": 0.95, "support": 31}
]

# Clinical Rule-Based Morphological Lemmatizer / Stemmer
def morphological_lemmatize(word):
    """Clean clinical suffix normalizer."""
    w = word.lower()
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"
    if w.endswith("ing") and len(w) > 5:
        return w[:-3]
    if w.endswith("ed") and len(w) > 4:
        return w[:-2]
    if w.endswith("es") and len(w) > 4:
        return w[:-2]
    if w.endswith("s") and not w.endswith("ss") and len(w) > 3:
        return w[:-1]
    return w

# -------------------------------------------------------------
# Web Application Routes
# -------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# -------------------------------------------------------------
# REST API Endpoints
# -------------------------------------------------------------
@app.route("/api/extract-pdf", methods=["POST"])
def extract_pdf():
    """Extracts medical transcription text from uploaded clinical PDF file."""
    if "file" not in request.files:
        return jsonify({"success": False, "error": "No file uploaded."}), 400

    file = request.files["file"]
    if not file or file.filename == "":
        return jsonify({"success": False, "error": "No file selected."}), 400

    filename = secure_filename(file.filename)
    if not filename.lower().endswith(".pdf"):
        return jsonify({"success": False, "error": "Invalid file type. Please upload a PDF document."}), 400

    try:
        file_bytes = file.read()
        file_size_kb = round(len(file_bytes) / 1024, 1)

        # PyMuPDF in-memory parsing
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        page_count = len(doc)
        extracted_text_parts = []

        for page in doc:
            text = page.get_text()
            if text:
                extracted_text_parts.append(text)

        full_text = "\n\n".join(extracted_text_parts).strip()

        if not full_text:
            return jsonify({
                "success": False,
                "error": "No readable text was found in this PDF.",
                "details": "The uploaded PDF appears to be empty or contains scanned images without OCR text."
            }), 422

        word_count = len(full_text.split())
        char_count = len(full_text)

        return jsonify({
            "success": True,
            "filename": filename,
            "file_size_kb": file_size_kb,
            "page_count": page_count,
            "word_count": word_count,
            "char_count": char_count,
            "extracted_text": full_text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Failed to extract PDF: {str(e)}"
        }), 500


@app.route("/api/preprocess", methods=["POST"])
def preprocess_text():
    """Returns step-by-step clinical NLP preprocessing stages."""
    data = request.get_json(silent=True) or {}
    raw_text = data.get("text", "")

    if not raw_text or not raw_text.strip():
        return jsonify({
            "raw_text": "",
            "cleaned_text": "",
            "tokens": [],
            "stopwords_removed": [],
            "lemmatized_tokens": [],
            "stats": {"raw_chars": 0, "token_count": 0, "filtered_count": 0}
        })

    # Step 1: Cleaned Text (Lowercased, punctuation handled, normalized spaces)
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', ' ', raw_text.lower())
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    # Step 2: Tokenization
    tokens = re.findall(r'\b[a-zA-Z]{2,}\b', cleaned_text)

    # Step 3: Stopword Removal
    stopwords_removed = [t for t in tokens if t not in ENGLISH_STOP_WORDS]

    # Step 4: Morphological Lemmatization
    lemmatized = [morphological_lemmatize(t) for t in stopwords_removed]

    return jsonify({
        "raw_text": raw_text[:500] + ("..." if len(raw_text) > 500 else ""),
        "cleaned_text": cleaned_text[:500] + ("..." if len(cleaned_text) > 500 else ""),
        "tokens": tokens[:80],
        "stopwords_removed": stopwords_removed[:80],
        "lemmatized_tokens": lemmatized[:80],
        "stats": {
            "raw_chars": len(raw_text),
            "raw_words": len(raw_text.split()),
            "token_count": len(tokens),
            "filtered_count": len(stopwords_removed),
            "stopword_ratio": round((1 - len(stopwords_removed) / max(len(tokens), 1)) * 100, 1)
        }
    })


@app.route("/api/features", methods=["POST"])
def extract_features():
    """Computes TF-IDF vector breakdown and top informative n-grams for the text."""
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")

    if not text or not text.strip():
        return jsonify({
            "total_features": 8000,
            "non_zero_count": 0,
            "sparsity_pct": 100.0,
            "top_features": [],
            "all_features": []
        })

    # Transform through trained TF-IDF vectorizer
    tfidf_matrix = vectorizer.transform([text])
    non_zero_indices = tfidf_matrix.nonzero()[1]
    non_zero_count = len(non_zero_indices)
    sparsity_pct = round((1 - (non_zero_count / 8000.0)) * 100, 2)

    feature_scores = []
    for idx in non_zero_indices:
        feat = feature_names[idx]
        score = float(tfidf_matrix[0, idx])
        feat_type = "Bigram" if " " in feat else "Unigram"
        feature_scores.append({
            "index": int(idx),
            "feature": feat,
            "score": round(score, 4),
            "type": feat_type
        })

    # Sort descending by TF-IDF weight
    feature_scores.sort(key=lambda x: x["score"], reverse=True)

    top_features = feature_scores[:20]

    return jsonify({
        "total_features": 8000,
        "non_zero_count": non_zero_count,
        "sparsity_pct": sparsity_pct,
        "top_features": top_features,
        "all_features": feature_scores[:100]  # Compact list for vector inspection
    })


@app.route("/api/predict", methods=["POST"])
def predict():
    """Executes multi-model inference, soft voting aggregation, and open-set check."""
    start_time = time.time()
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    threshold = float(data.get("threshold", 0.48))

    if not text:
        return jsonify({
            "success": False,
            "error": "Clinical transcription text is empty. Please enter or extract text first."
        }), 400

    # 1. Transform clinical text using TF-IDF
    tfidf_vec = vectorizer.transform([text])
    vocab_matches = int(tfidf_vec.nnz)

    if vocab_matches == 0:
        elapsed_ms = round((time.time() - start_time) * 1000, 2)
        return jsonify({
            "success": True,
            "predicted_specialty": "Other",
            "is_other": True,
            "confidence": 0.0,
            "confidence_percent": "0.0%",
            "triage_status": "UNRECOGNIZED_NON_MEDICAL",
            "explanation": "Input text contains zero recognized medical vocabulary terms in the 8,000-feature dictionary.",
            "probability_distribution": {c: 0.0 for c in classes_list},
            "nearest_candidates": [],
            "models_breakdown": {},
            "vocabulary_matches": 0,
            "inference_time_ms": elapsed_ms
        })

    # 2. Extract Individual Model Probabilities from Voting Classifier Estimators
    models_breakdown = {}
    estimator_keys = [("svm", "Linear SVM", 2), ("lr", "Logistic Regression", 2),
                      ("rf", "Random Forest", 1), ("mnb", "Multinomial Naive Bayes", 1)]

    for key, name, weight in estimator_keys:
        est = ensemble_model.named_estimators_[key]
        probs = est.predict_proba(tfidf_vec)[0]
        top_idx = int(np.argmax(probs))
        top_class = classes_list[top_idx]
        top_prob = float(probs[top_idx])
        models_breakdown[key] = {
            "name": name,
            "weight": weight,
            "accuracy": MODEL_BENCHMARKS[key]["accuracy"],
            "macro_f1": MODEL_BENCHMARKS[key]["macro_f1"],
            "predicted_specialty": top_class,
            "confidence": round(top_prob, 4),
            "confidence_percent": f"{round(top_prob * 100, 1)}%",
            "top_probabilities": {classes_list[i]: round(float(probs[i]), 4) for i in np.argsort(probs)[::-1][:3]}
        }

    # 3. Soft Voting Ensemble Aggregated Probabilities
    ensemble_probs = ensemble_model.predict_proba(tfidf_vec)[0]
    sorted_indices = np.argsort(ensemble_probs)[::-1]

    top_idx = int(sorted_indices[0])
    top_class = classes_list[top_idx]
    top_prob = float(ensemble_probs[top_idx])

    second_idx = int(sorted_indices[1])
    second_class = classes_list[second_idx]
    second_prob = float(ensemble_probs[second_idx])

    prob_distribution = {classes_list[i]: round(float(ensemble_probs[i]), 4) for i in sorted_indices}

    elapsed_ms = round((time.time() - start_time) * 1000, 2)

    # 4. Open-Set 9-Class Rejection Gate (Threshold tau = 0.48)
    if top_prob >= threshold:
        # Confirmed In-Domain Specialty
        predicted_specialty = top_class
        is_other = False
        triage_status = "CONFIRMED_SPECIALTY"
        explanation = f"High-confidence clinical consensus ({round(top_prob * 100, 1)}%) matching {top_class} operative terminology."
    else:
        # Rejected into "Other" (9th class)
        predicted_specialty = "Other"
        is_other = True
        triage_status = "OUT_OF_SCOPE_OR_AMBIGUOUS"
        explanation = (
            f"Peak ensemble confidence ({round(top_prob * 100, 1)}%) is below the {round(threshold * 100, 1)}% safety threshold. "
            f"This case either belongs to an unsupported medical specialty (e.g., Dermatology, Psychiatry, Pediatrics) "
            f"or requires manual clinician review."
        )

    nearest_candidates = [
        {"specialty": top_class, "confidence": round(top_prob, 4), "percent": f"{round(top_prob * 100, 1)}%"},
        {"specialty": second_class, "confidence": round(second_prob, 4), "percent": f"{round(second_prob * 100, 1)}%"}
    ]

    return jsonify({
        "success": True,
        "predicted_specialty": predicted_specialty,
        "is_other": is_other,
        "confidence": round(top_prob, 4),
        "confidence_percent": f"{round(top_prob * 100, 1)}%",
        "triage_status": triage_status,
        "explanation": explanation,
        "threshold_applied": threshold,
        "probability_distribution": prob_distribution,
        "nearest_candidates": nearest_candidates,
        "models_breakdown": models_breakdown,
        "ensemble_consensus": {
            "name": "Soft Voting Ensemble",
            "weights": [2, 2, 1, 1],
            "formula": "(2×SVM + 2×LR + 1×RF + 1×MNB) / 6",
            "accuracy": 87.99,
            "macro_f1": 0.8898
        },
        "vocabulary_matches": vocab_matches,
        "inference_time_ms": elapsed_ms
    })


@app.route("/api/model-info", methods=["GET"])
def get_model_info():
    """Returns dataset summary, benchmark accuracies, and confusion matrix data."""
    return jsonify({
        "dataset_stats": DATASET_STATS,
        "model_benchmarks": MODEL_BENCHMARKS,
        "confusion_matrix": CONFUSION_MATRIX_DATA,
        "classification_report": CLASSIFICATION_REPORT_DATA,
        "specialties": classes_list
    })


@app.route("/api/specialties", methods=["GET"])
def get_specialties():
    """Returns list of the 8 supported clinical specialties + Other definition."""
    return jsonify({
        "supported_specialties": classes_list,
        "open_set_class": {
            "name": "Other",
            "status": "Out of Scope / Requires Review",
            "threshold": 0.48,
            "examples": ["Dermatology", "Psychiatry", "Pediatrics", "Dentistry", "Non-medical text"]
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting MedSpecialty AI Platform on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
