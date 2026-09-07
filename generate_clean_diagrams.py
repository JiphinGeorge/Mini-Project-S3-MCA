import pymupdf
import os

pdf_path = r"D:\Antigravity Projects\Mini Project S3 MCA\Inital Report\Mini_Project_Inital_report.pdf"
doc = pymupdf.open(pdf_path)

out_dir = r"D:\Antigravity Projects\Mini Project S3 MCA\report_diagrams_clean"
os.makedirs(out_dir, exist_ok=True)

# Exact bounding boxes in PDF points (72 points/inch)
# Page size: 595.28 x 841.89
crops = {
    # Figure 7: SVM (Page 25)
    # START is at y=80, END is at y=460, decision loop branches to x~220
    "svm": (25, pymupdf.Rect(200, 70, 400, 465), "Figure 7: Activity Diagram of Support Vector Machine"),
    
    # Figure 8: Random Forest (Page 27)
    # START is at y=307, END is at y=659, loop branches to x~220
    "rf": (27, pymupdf.Rect(200, 298, 400, 665), "Figure 8: Activity Diagram of Random Forest"),
    
    # Figure 9: Logistic Regression (Page 29)
    # START is at y=80, END is at y=484, loop branches to x~220
    "lr": (29, pymupdf.Rect(200, 70, 400, 490), "Figure 9: Activity Diagram of Logistic Regression"),
    
    # Figure 10: Multinomial Naive Bayes (Page 30)
    # START is at y=418, END is at y=689
    "mnb": (30, pymupdf.Rect(200, 410, 395, 695), "Figure 10: Activity Diagram of Multinomial Naive Bayes"),
    
    # Figure 11: TF-IDF (Page 32)
    # START is at y=80, END is at y=289
    "tfidf": (32, pymupdf.Rect(200, 70, 395, 296), "Figure 11: Activity Diagram of TF-IDF Feature Vectorizer"),
    
    # Figure 12: Voting Ensemble (Page 33)
    # START is at y=301, 4 parallel models x from 140 to 455, END is at y=567
    "ensemble": (33, pymupdf.Rect(130, 292, 465, 573), "Figure 12: Activity Diagram of Voting Ensemble Classifier"),
    
    # Figure 13: Project Pipeline (Page 35)
    # Embedded image or rect from 70 to 525, y from 160 to 530
    "pipeline": (35, pymupdf.Rect(70, 160, 525, 530), "Figure 13: Project Pipeline Diagram")
}

zoom = 4.0 # High resolution (~288 DPI)
mat = pymupdf.Matrix(zoom, zoom)

for name, (p_num, r, desc) in crops.items():
    page = doc[p_num - 1]
    
    # Check drawings on page to find exact min_x, max_x within y-range
    drawings = page.get_drawings()
    in_range = [d["rect"] for d in drawings if d["rect"].y0 >= r.y0 - 5 and d["rect"].y1 <= r.y1 + 5]
    if in_range:
        x0 = min(d.x0 for d in in_range) - 10
        x1 = max(d.x1 for d in in_range) + 10
        y0 = min(d.y0 for d in in_range) - 8
        y1 = max(d.y1 for d in in_range) + 8
        tight_rect = pymupdf.Rect(x0, y0, x1, y1)
    else:
        tight_rect = r
        
    pix = page.get_pixmap(matrix=mat, clip=tight_rect)
    out_file = os.path.join(out_dir, f"{name}.png")
    pix.save(out_file)
    print(f"Generated {name}.png: {tight_rect} -> {pix.width}x{pix.height} at {out_file}")
