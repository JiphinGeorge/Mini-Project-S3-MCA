import os
import time
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

def main():
    print("=" * 80)
    print("EXCLUSIVELY 4 BASE MODELS (LR, SVM, RF, MNB) + ENSEMBLE CLASSIFIERS")
    print("=" * 80)
    
    csv_file = "filtered_mtsamples_8classes.csv"
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"{csv_file} not found. Please run 01_dataset_filtering_and_eda.py first.")
        
    df = pd.read_csv(csv_file)
    print(f"Loaded dataset: {df.shape[0]} records across {df['medical_specialty'].nunique()} specialties.")
    
    # Feature & Target Selection
    X = df['clinical_text'].astype(str)
    y = df['medical_specialty']
    
    # Stratified 80/20 Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Training set: {len(X_train)} samples | Testing set: {len(X_test)} samples")
    
    # TF-IDF Feature Extraction with Sublinear Scaling
    print("\nExtracting TF-IDF Features (max_features=8000, n-grams=(1,2), sublinear_tf=True)...")
    tfidf = TfidfVectorizer(
        max_features=8000,
        ngram_range=(1, 2),
        sublinear_tf=True,
        min_df=2,
        max_df=0.7,
        norm='l2'
    )
    
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)
    print(f"X_train_tfidf Shape: {X_train_tfidf.shape}")
    print(f"X_test_tfidf Shape : {X_test_tfidf.shape}")
    
    # Save Feature Matrices and Labels
    joblib.dump(tfidf, "tfidf_vectorizer_8classes.pkl")
    joblib.dump(X_train_tfidf, "X_train_tfidf.pkl")
    joblib.dump(X_test_tfidf, "X_test_tfidf.pkl")
    joblib.dump(y_train, "y_train.pkl")
    joblib.dump(y_test, "y_test.pkl")
    
    # 1. Base Classifiers
    # Logistic Regression (LR)
    lr = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
    # Support Vector Machine (Linear SVM)
    svm = LinearSVC(class_weight='balanced', max_iter=3000, random_state=42)
    # Calibrated SVM for soft probability voting
    cal_svm = CalibratedClassifierCV(LinearSVC(class_weight='balanced', max_iter=3000, random_state=42))
    # Random Forest (RF)
    rf = RandomForestClassifier(n_estimators=100, max_depth=25, class_weight='balanced', random_state=42, n_jobs=1)
    # Multinomial Naive Bayes (MNB)
    mnb = MultinomialNB(alpha=0.5)
    
    # 2. Ensemble Classifiers combining LR, SVM, RF, and MNB
    hard_voting = VotingClassifier(
        estimators=[
            ('lr', lr),
            ('svm', svm),
            ('rf', rf),
            ('mnb', mnb)
        ],
        voting='hard',
        weights=[2, 2, 1, 1],
        n_jobs=1
    )
    
    soft_voting = VotingClassifier(
        estimators=[
            ('lr', lr),
            ('svm', cal_svm),
            ('rf', rf),
            ('mnb', mnb)
        ],
        voting='soft',
        weights=[2, 2, 1, 1],
        n_jobs=1
    )
    
    models = {
        "Logistic Regression (LR)": lr,
        "Support Vector Machine (SVM)": svm,
        "Random Forest (RF)": rf,
        "Multinomial Naive Bayes (MNB)": mnb,
        "Hard Voting Ensemble (LR+SVM+RF+MNB)": hard_voting,
        "Soft Voting Ensemble (LR+SVM+RF+MNB)": soft_voting
    }
    
    # Evaluation Loop
    results = []
    trained_models = {}
    
    print("\n" + "=" * 80)
    print(f"{'Model Name':<38} | {'Acc':<7} | {'M-Prec':<7} | {'M-Recall':<8} | {'M-F1':<7} | {'W-F1':<7}")
    print("-" * 80)
    
    for name, clf in models.items():
        t0 = time.time()
        clf.fit(X_train_tfidf, y_train)
        fit_time = time.time() - t0
        
        preds = clf.predict(X_test_tfidf)
        
        acc = accuracy_score(y_test, preds)
        m_prec = precision_score(y_test, preds, average='macro', zero_division=0)
        m_rec = recall_score(y_test, preds, average='macro', zero_division=0)
        m_f1 = f1_score(y_test, preds, average='macro', zero_division=0)
        w_f1 = f1_score(y_test, preds, average='weighted', zero_division=0)
        
        print(f"{name:<38} | {acc:.4f}  | {m_prec:.4f}  | {m_rec:.4f}   | {m_f1:.4f}  | {w_f1:.4f}")
        
        results.append({
            "Model": name,
            "Accuracy": acc,
            "Macro Precision": m_prec,
            "Macro Recall": m_rec,
            "Macro F1": m_f1,
            "Weighted F1": w_f1,
            "Train Time (s)": round(fit_time, 2)
        })
        trained_models[name] = clf
        
    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values(by="Accuracy", ascending=False).reset_index(drop=True)
    df_results.to_csv("evaluation_summary.csv", index=False)
    
    print("\n" + "=" * 80)
    print("RANKED BY ACCURACY:")
    print("=" * 80)
    print(df_results.to_string(index=False))
    
    # Save the Best Model
    best_model_name = df_results.iloc[0]["Model"]
    best_model = trained_models[best_model_name]
    joblib.dump(best_model, "best_balanced_model.pkl")
    print(f"\nBest Model: '{best_model_name}' saved to 'best_balanced_model.pkl'")
    
    # Also explicitly save the Soft Voting Ensemble
    joblib.dump(soft_voting, "voting_ensemble_model.pkl")
    print("Saved 'voting_ensemble_model.pkl' successfully.")
    
    # Detailed Classification Report for Best Model and Ensemble
    print("\n" + "=" * 80)
    print(f"DETAILED CLASSIFICATION REPORT FOR: {best_model_name}")
    print("=" * 80)
    best_preds = best_model.predict(X_test_tfidf)
    report = classification_report(y_test, best_preds, zero_division=0)
    print(report)
    with open("best_model_classification_report.txt", "w") as f:
        f.write(f"BEST MODEL: {best_model_name}\n\n")
        f.write(report)
        
    # Visualizations: Performance Comparison Bar Chart
    plt.figure(figsize=(12, 6))
    x_pos = np.arange(len(df_results))
    width = 0.25
    
    plt.bar(x_pos - width, df_results["Accuracy"], width=width, label="Accuracy", color="#2980b9")
    plt.bar(x_pos, df_results["Macro F1"], width=width, label="Macro F1", color="#27ae60")
    plt.bar(x_pos + width, df_results["Macro Recall"], width=width, label="Macro Recall", color="#e67e22")
    
    plt.axhline(0.75, color='red', linestyle='--', linewidth=2, label='Target Threshold (75%)')
    plt.xticks(x_pos, df_results["Model"], rotation=25, ha="right", fontsize=9)
    plt.ylabel("Score")
    plt.title("LR, SVM, RF, MNB & Ensemble Performance Comparison (8 Specialties)")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("model_performance_comparison.png", dpi=300)
    plt.close()
    print("Saved 'model_performance_comparison.png'")
    
    # Visualizations: Confusion Matrix for the Ensemble
    labels = sorted(y_test.unique())
    ens_preds = soft_voting.predict(X_test_tfidf)
    cm = confusion_matrix(y_test, ens_preds, labels=labels)
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels
    )
    plt.title(f"Confusion Matrix: Soft Voting Ensemble (Accuracy: {accuracy_score(y_test, ens_preds)*100:.2f}%)")
    plt.xlabel("Predicted Specialty")
    plt.ylabel("True Specialty")
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    plt.savefig("best_model_confusion_matrix.png", dpi=300)
    plt.close()
    print("Saved 'best_model_confusion_matrix.png'")
    
    print("\nAll 4 models and the ensembles trained, evaluated, and saved successfully!")

if __name__ == '__main__':
    main()
