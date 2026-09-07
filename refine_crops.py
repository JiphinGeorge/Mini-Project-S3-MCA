import pymupdf
import os

pdf_path = r"D:\Antigravity Projects\Mini Project S3 MCA\Inital Report\Mini_Project_Inital_report.pdf"
doc = pymupdf.open(pdf_path)

out_dir = r"D:\Antigravity Projects\Mini Project S3 MCA\report_diagrams_clean"

# Let's refine the crop boxes so NO caption text ("Figure X...") and NO header text ("Medical Specialty...") is included!
# In PDF coords:
# Page 25: Caption "Figure 7" is at y0=472.1. END box is at y0=452.5, y1=460.5. So y1=465 is safe.
# Page 27: Caption "Figure 8" is at y0=670.9. END box is at y0=651.3, y1=659.2. So y1=664 is safe.
# Page 29: Caption "Figure 9" is at y0=495.6. END box is at y0=476.0, y1=484.0. So y1=489 is safe.
# Page 30: Caption "Figure 10" is at y0=701.2. END box is at y0=681.6, y1=689.6. So y1=694 is safe.
# Page 33: Caption "Figure 12" is at y0=579.0. END box is at y0=559.4, y1=567.4. So y1=572 is safe.

refined_crops = {
    "svm": (25, 185, 75, 410, 465),
    "rf": (27, 185, 302, 410, 664),
    "lr": (29, 185, 75, 410, 488),
    "mnb": (30, 195, 412, 400, 694),
    "tfidf": (32, 195, 75, 400, 294),
    "ensemble": (33, 95, 295, 500, 572),
}

zoom = 4.0
mat = pymupdf.Matrix(zoom, zoom)

for name, (p_num, x0, y0, x1, y1) in refined_crops.items():
    page = doc[p_num - 1]
    rect = pymupdf.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(matrix=mat, clip=rect)
    out_file = os.path.join(out_dir, f"{name}.png")
    pix.save(out_file)
    print(f"Refined {name}: {pix.width}x{pix.height} saved.")

# Also for Figure 13 (Pipeline), let's get the original embedded image or crop cleanly
page35 = doc[34]
# Check Figure 13 caption is at y0=535.4. Pipeline starts around y=160.
rect_pipe = pymupdf.Rect(65, 160, 530, 530)
pix_pipe = page35.get_pixmap(matrix=mat, clip=rect_pipe)
pix_pipe.save(os.path.join(out_dir, "pipeline.png"))
print("Refined pipeline.png saved.")
