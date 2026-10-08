"""
triage_inference.py
===================
9-Class Medical Specialty Classification & Clinical Triage Inference Engine
Supports:
  - 8 Core In-Domain Hospital Specialties:
      1. Cardiovascular / Pulmonary
      2. Orthopedic
      3. Gastroenterology
      4. Neurology
      5. Urology
      6. Obstetrics / Gynecology
      7. ENT - Otolaryngology
      8. Ophthalmology
  - 9th Class:
      9. "Other" (Open-Set Recognition / Out-of-Domain Triage)
         Triggered when:
           a) Case belongs to an unsupported clinical specialty (e.g., Dermatology, Psychiatry, Pediatrics)
           b) Prediction confidence is below the calibrated threshold (default: 0.48)
           c) Input text lacks sufficient clinical vocabulary overlap
"""

import os
import time
import joblib
import numpy as np

class ClinicalTriageClassifier:
    def __init__(self, model_dir=None, default_threshold=0.48):
        """
        Initializes the 9-class triage classifier with serialized model artifacts.
        """
        if model_dir is None:
            model_dir = os.path.dirname(os.path.abspath(__file__))
            
        self.vectorizer_path = os.path.join(model_dir, "tfidf_vectorizer_8classes.pkl")
        self.model_path = os.path.join(model_dir, "voting_ensemble_model.pkl")
        self.default_threshold = default_threshold
        
        self.vectorizer = None
        self.model = None
        self.classes_ = None
        self._load_artifacts()

    def _load_artifacts(self):
        """Loads serialized TF-IDF vectorizer and Soft Voting Ensemble model."""
        if not os.path.exists(self.vectorizer_path):
            raise FileNotFoundError(f"Vectorizer artifact missing at: {self.vectorizer_path}")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model artifact missing at: {self.model_path}")
            
        self.vectorizer = joblib.load(self.vectorizer_path)
        self.model = joblib.load(self.model_path)
        self.classes_ = list(self.model.classes_)

    def predict(self, text, threshold=None):
        """
        Predicts medical specialty across 9 classes (8 core specialties + 'Other').
        
        Parameters:
        -----------
        text : str
            Raw clinical transcription or medical dictation text.
        threshold : float, optional
            Confidence threshold for in-domain acceptance (defaults to self.default_threshold).
            
        Returns:
        --------
        dict containing:
            - 'predicted_specialty': str (one of the 8 specialties or 'Other')
            - 'is_other': bool
            - 'confidence': float
            - 'triage_status': str
            - 'probability_distribution': dict
            - 'nearest_candidates': list
            - 'vocabulary_matches': int
            - 'inference_time_ms': float
        """
        start_time = time.time()
        th = threshold if threshold is not None else self.default_threshold
        
        # 1. Input Validation
        if not text or not isinstance(text, str) or not text.strip():
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            return {
                "predicted_specialty": "Other",
                "is_other": True,
                "confidence": 0.0,
                "triage_status": "EMPTY_INPUT",
                "explanation": "No text content provided in patient record.",
                "probability_distribution": {c: 0.0 for c in self.classes_},
                "nearest_candidates": [],
                "vocabulary_matches": 0,
                "inference_time_ms": elapsed_ms
            }

        cleaned_text = text.strip()
        
        # 2. Vectorization
        tfidf_vec = self.vectorizer.transform([cleaned_text])
        vocab_matches = int(tfidf_vec.nnz)
        
        # 3. Non-medical / Zero vocabulary check
        if vocab_matches == 0:
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            return {
                "predicted_specialty": "Other",
                "is_other": True,
                "confidence": 0.0,
                "triage_status": "UNRECOGNIZED_NON_MEDICAL",
                "explanation": "Input text contains zero recognized medical vocabulary terms.",
                "probability_distribution": {c: 0.0 for c in self.classes_},
                "nearest_candidates": [],
                "vocabulary_matches": 0,
                "inference_time_ms": elapsed_ms
            }

        # 4. Model Probability Prediction via Soft Voting Ensemble
        probs = self.model.predict_proba(tfidf_vec)[0]
        sorted_indices = np.argsort(probs)[::-1]
        
        top_idx = sorted_indices[0]
        top_class = self.classes_[top_idx]
        top_prob = float(probs[top_idx])
        
        second_idx = sorted_indices[1]
        second_class = self.classes_[second_idx]
        second_prob = float(probs[second_idx])
        
        prob_dist = {self.classes_[i]: round(float(probs[i]), 4) for i in sorted_indices}
        
        elapsed_ms = round((time.time() - start_time) * 1000, 2)

        # 5. Open-Set 9-Class Decision Logic
        if top_prob >= th:
            # In-Domain Specialty Confirmed
            return {
                "predicted_specialty": top_class,
                "is_other": False,
                "confidence": round(top_prob, 4),
                "triage_status": "CONFIRMED_SPECIALTY",
                "explanation": f"High confidence match ({top_prob*100:.1f}%) for {top_class}.",
                "probability_distribution": prob_dist,
                "nearest_candidates": [
                    {"specialty": top_class, "confidence": round(top_prob, 4)},
                    {"specialty": second_class, "confidence": round(second_prob, 4)}
                ],
                "vocabulary_matches": vocab_matches,
                "inference_time_ms": elapsed_ms
            }
        else:
            # Below Threshold -> Routed to "Other"
            return {
                "predicted_specialty": "Other",
                "is_other": True,
                "confidence": round(top_prob, 4),
                "triage_status": "OUT_OF_SCOPE_OR_AMBIGUOUS",
                "explanation": (
                    f"Peak confidence ({top_prob*100:.1f}%) is below the {th*100:.0f}% triage threshold. "
                    f"Case belongs to an unsupported medical specialty (e.g., Dermatology, Psychiatry) "
                    f"or requires manual clinician review."
                ),
                "probability_distribution": prob_dist,
                "nearest_candidates": [
                    {"specialty": top_class, "confidence": round(top_prob, 4)},
                    {"specialty": second_class, "confidence": round(second_prob, 4)}
                ],
                "vocabulary_matches": vocab_matches,
                "inference_time_ms": elapsed_ms
            }

# Module-level singleton instance for convenient import
_classifier = None

def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = ClinicalTriageClassifier()
    return _classifier

def predict_specialty(text, threshold=None):
    """Convenience functional interface for predictions."""
    clf = get_classifier()
    return clf.predict(text, threshold=threshold)


if __name__ == "__main__":
    print("=" * 80)
    print("9-CLASS CLINICAL TRIAGE INFERENCE ENGINE - VERIFICATION SUITE")
    print("=" * 80)
    
    clf = ClinicalTriageClassifier()
    print(f"Loaded successfully with {len(clf.classes_)} core specialties + 1 'Other' class.")
    print(f"Default In-Domain Triage Threshold: {clf.default_threshold*100:.1f}%\n")
    
    test_cases = [
        (
            "Cardiovascular (In-Domain)",
            "The patient is a 64-year-old male with acute coronary syndrome and unstable angina. "
            "Coronary angiography revealed a 90% proximal left anterior descending (LAD) stenosis. "
            "Successful balloon angioplasty and drug-eluting stent placement performed."
        ),
        (
            "Ophthalmology (In-Domain)",
            "Operative procedure: Right eye phacoemulsification with posterior chamber intraocular lens "
            "implantation. Clear corneal incision made at 10 o'clock. Continuous curvilinear capsulorhexis "
            "performed. Cortex aspirated, lens placed in capsular bag."
        ),
        (
            "Orthopedic (In-Domain)",
            "Patient sustained a displaced fracture of the distal radius after a mechanical fall. "
            "Open reduction and internal fixation (ORIF) was performed with a volar locking plate "
            "and cortical screws. Stable fixation confirmed fluoroscopically."
        ),
        (
            "Neurology (In-Domain)",
            "The patient presents with recurrent focal seizures, right-sided hemiparesis, and expressive "
            "aphasia. Brain MRI demonstrates an acute ischemic infarct in the left middle cerebral artery territory."
        ),
        (
            "Dermatology (Unsupported Specialty -> 'Other')",
            "Patient presents with widespread erythematous scaling plaques with silvery scale on extensor surfaces "
            "of bilateral elbows and knees. Diagnosed with plaque psoriasis. Prescribed topical calcipotriene ointment."
        ),
        (
            "Psychiatry (Unsupported Specialty -> 'Other')",
            "Mental status examination reveals depressed mood, flat affect, anhedonia, and poor concentration. "
            "Patient reports major depressive disorder episodes with insomnia. Starting SSRI sertraline 50 mg daily."
        ),
        (
            "Dentistry (Unsupported Specialty -> 'Other')",
            "Surgical extraction of impacted mandibular third molars under local anesthesia. Full-thickness "
            "mucoperiosteal flap elevated. Bone guttering performed and tooth sectioned."
        ),
        (
            "Non-Medical Text -> 'Other'",
            "The web server experienced a connection timeout error when querying the PostgreSQL relational database cluster."
        )
    ]
    
    for label, text in test_cases:
        res = clf.predict(text)
        is_oth = res["is_other"]
        flag = "[OTHER CLASS]" if is_oth else "[CORE SPECIALTY]"
        print(f"Test Case: {label}")
        print(f"  -> Prediction : {res['predicted_specialty']} {flag}")
        print(f"  -> Confidence : {res['confidence']*100:.1f}% | Time: {res['inference_time_ms']} ms")
        print(f"  -> Status     : {res['triage_status']}")
        if is_oth and res["nearest_candidates"]:
            cand_str = ", ".join([f"{c['specialty']} ({c['confidence']*100:.1f}%)" for c in res["nearest_candidates"]])
            print(f"  -> Candidates : {cand_str}")
        print("-" * 80)
