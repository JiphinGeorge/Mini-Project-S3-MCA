import pymupdf
import os

pdf_path = r"D:\Antigravity Projects\Mini Project S3 MCA\Inital Report\Mini_Project_Inital_report.pdf"
doc = pymupdf.open(pdf_path)

out_dir = r"D:\Antigravity Projects\Mini Project S3 MCA\extracted_diagrams"
os.makedirs(out_dir, exist_ok=True)

# Define crop boxes in page coordinates (x0, y0, x1, y1)
# Page dimensions: 595.3 x 841.9
# We can find the drawings bounding box on each page!
diagram_pages = {
    "svm": (25, 60, 465, "Figure 7: Activity Diagram of Support Vector Machine"),
    "rf": (27, 290, 665, "Figure 8: Activity Diagram of Random Forest"),
    "lr": (29, 60, 490, "Figure 9: Activity Diagram of Logistic Regression"),
    "mnb": (30, 390, 695, "Figure 10: Activity Diagram of Multinomial Naive Bayes"),
    "tfidf": (32, 60, 295, "Figure 11: Activity Diagram of TF-IDF Feature Vectorizer"),
    "ensemble": (33, 270, 570, "Figure 12: Activity Diagram of Voting Ensemble Classifier"),
    "pipeline": (35, 100, 530, "Figure 13: Project Pipeline Diagram")
}

zoom = 300 / 72 # 300 DPI high resolution
mat = pymupdf.Matrix(zoom, zoom)

for name, (p_num, y0, y1, desc) in diagram_pages.items():
    page = doc[p_num - 1]
    
    # Calculate tight horizontal bounding box from drawings
    drawings = page.get_drawings()
    min_x = 50
    max_x = 545
    
    # Let's inspect drawing rects in range [y0, y1]
    y_drawings = [d["rect"] for d in drawings if d["rect"].y0 >= y0 - 15 and d["rect"].y1 <= y1 + 15]
    if y_drawings:
        calc_x0 = max(40, min(r.x0 for r in y_drawings) - 10)
        calc_y0 = max(y0 - 20, min(r.y0 for r in y_drawings) - 10)
        calc_x1 = min(555, max(r.x1 for r in y_drawings) + 10)
        calc_y1 = min(y1 + 5, max(r.y1 for r in y_drawings) + 10)
    else:
        calc_x0, calc_y0, calc_x1, calc_y1 = 70, y0, 525, y1
        
    crop_rect = pymupdf.Rect(calc_x0, calc_y0, calc_x1, calc_y1)
    pix = page.get_pixmap(matrix=mat, clip=crop_rect)
    out_path = os.path.join(out_dir, f"{name}_activity_diagram.png")
    pix.save(out_path)
    print(f"Saved {name}: {out_path} ({pix.width}x{pix.height}) from rect {crop_rect}")
