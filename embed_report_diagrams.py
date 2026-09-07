import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
import os, subprocess, time

PPTX_PATH = r"D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation.pptx"
DIAG_DIR = r"D:\Antigravity Projects\Mini Project S3 MCA\report_diagrams_clean"

prs = pptx.Presentation(PPTX_PATH)

TEAL_ACCENT = RGBColor(0x0E, 0x7C, 0x86)
DARK_NAVY = RGBColor(0x0B, 0x1F, 0x3A)
BORDER_GRAY = RGBColor(0xCB, 0xD5, 0xE1)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLUE_ACCENT = RGBColor(0x25, 0x63, 0xEB)
PURPLE_ACCENT = RGBColor(0x93, 0x33, 0xEA)
GREEN_ACCENT = RGBColor(0x16, 0xA3, 0x4A)
SLATE_DARK = RGBColor(0x33, 0x41, 0x55)

# =========================================================================
# 1. SLIDE 13: SVM & MULTINOMIAL NAIVE BAYES (FIGURE 7 & FIGURE 10)
# =========================================================================
s13 = prs.slides[12]
sp_tree13 = s13.shapes._spTree

# Keep header, title, footers; remove inner shapes
shapes_to_remove = []
for sh in s13.shapes:
    if sh.top > Inches(1.4) and sh.top < Inches(7.0):
        shapes_to_remove.append(sh)

for sh in shapes_to_remove:
    sp_tree13.remove(sh._element)

# Left Card: Support Vector Machine
c1 = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.45), Inches(5.95), Inches(5.55))
c1.fill.solid()
c1.fill.fore_color.rgb = WHITE
c1.line.color.rgb = TEAL_ACCENT
c1.line.width = Pt(1.5)

h1 = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.55), Inches(5.65), Inches(0.42))
h1.fill.solid()
h1.fill.fore_color.rgb = TEAL_ACCENT
h1.line.fill.background()
p = h1.text_frame.paragraphs[0]
p.text = "SUPPORT VECTOR MACHINE (SVM) — ACTIVITY DIAGRAM"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Add SVM Image
svm_img_path = os.path.join(DIAG_DIR, "svm.png")
# Image original aspect ratio: 900x1560 (w/h = 0.577)
# Fit inside 5.65 wide x 4.85 high -> width = 2.80 in, height = 4.85 in
s13.shapes.add_picture(svm_img_path, Inches(2.07), Inches(2.05), width=Inches(2.80))

# Right Card: Multinomial Naive Bayes
c2 = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.80), Inches(1.45), Inches(6.00), Inches(5.55))
c2.fill.solid()
c2.fill.fore_color.rgb = WHITE
c2.line.color.rgb = BLUE_ACCENT
c2.line.width = Pt(1.5)

h2 = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), Inches(1.55), Inches(5.70), Inches(0.42))
h2.fill.solid()
h2.fill.fore_color.rgb = BLUE_ACCENT
h2.line.fill.background()
p = h2.text_frame.paragraphs[0]
p.text = "MULTINOMIAL NAIVE BAYES (MNB) — ACTIVITY DIAGRAM"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Add MNB Image
mnb_img_path = os.path.join(DIAG_DIR, "mnb.png")
# Image original aspect ratio: 820x1128 (w/h = 0.727)
# Fit inside 5.70 wide x 4.85 high -> width = 3.45 in, height = 4.75 in
s13.shapes.add_picture(mnb_img_path, Inches(8.07), Inches(2.10), width=Inches(3.45))

print("Slide 13 updated with actual report diagrams for SVM & MNB.")

# =========================================================================
# 2. SLIDE 14: RANDOM FOREST & LOGISTIC REGRESSION (FIGURE 8 & FIGURE 9)
# =========================================================================
s14 = prs.slides[13]
sp_tree14 = s14.shapes._spTree

shapes_to_remove = []
for sh in s14.shapes:
    if sh.top > Inches(1.4) and sh.top < Inches(7.0):
        shapes_to_remove.append(sh)

for sh in shapes_to_remove:
    sp_tree14.remove(sh._element)

# Left Card: Random Forest
c1 = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.45), Inches(5.95), Inches(5.55))
c1.fill.solid()
c1.fill.fore_color.rgb = WHITE
c1.line.color.rgb = GREEN_ACCENT
c1.line.width = Pt(1.5)

h1 = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.55), Inches(5.65), Inches(0.42))
h1.fill.solid()
h1.fill.fore_color.rgb = GREEN_ACCENT
h1.line.fill.background()
p = h1.text_frame.paragraphs[0]
p.text = "RANDOM FOREST (RF) — ACTIVITY DIAGRAM"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Add RF Image
rf_img_path = os.path.join(DIAG_DIR, "rf.png")
# Image original aspect ratio: 900x1448 (w/h = 0.622)
# Width = 2.95 in, height = 4.75 in
s14.shapes.add_picture(rf_img_path, Inches(2.00), Inches(2.05), width=Inches(2.95))

# Right Card: Logistic Regression
c2 = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.80), Inches(1.45), Inches(6.00), Inches(5.55))
c2.fill.solid()
c2.fill.fore_color.rgb = WHITE
c2.line.color.rgb = PURPLE_ACCENT
c2.line.width = Pt(1.5)

h2 = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), Inches(1.55), Inches(5.70), Inches(0.42))
h2.fill.solid()
h2.fill.fore_color.rgb = PURPLE_ACCENT
h2.line.fill.background()
p = h2.text_frame.paragraphs[0]
p.text = "LOGISTIC REGRESSION (LR) — ACTIVITY DIAGRAM"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Add LR Image
lr_img_path = os.path.join(DIAG_DIR, "lr.png")
# Image original aspect ratio: 900x1652 (w/h = 0.545)
# Width = 2.65 in, height = 4.85 in
s14.shapes.add_picture(lr_img_path, Inches(8.47), Inches(2.05), width=Inches(2.65))

print("Slide 14 updated with actual report diagrams for RF & LR.")

# =========================================================================
# 3. SLIDE 15: VOTING ENSEMBLE CLASSIFIER (FIGURE 12)
# =========================================================================
s15 = prs.slides[14]
sp_tree15 = s15.shapes._spTree

shapes_to_remove = []
for sh in s15.shapes:
    if sh.top > Inches(1.4) and sh.top < Inches(7.0):
        shapes_to_remove.append(sh)

for sh in shapes_to_remove:
    sp_tree15.remove(sh._element)

# Left / Center Container for Figure 12
c_ens = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.45), Inches(7.50), Inches(5.55))
c_ens.fill.solid()
c_ens.fill.fore_color.rgb = WHITE
c_ens.line.color.rgb = TEAL_ACCENT
c_ens.line.width = Pt(1.5)

h_ens = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.55), Inches(7.20), Inches(0.42))
h_ens.fill.solid()
h_ens.fill.fore_color.rgb = TEAL_ACCENT
h_ens.line.fill.background()
p = h_ens.text_frame.paragraphs[0]
p.text = "VOTING ENSEMBLE CLASSIFIER — ACTIVITY DIAGRAM"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Add Ensemble Image (1620x1108, w/h = 1.46)
ens_img_path = os.path.join(DIAG_DIR, "ensemble.png")
# Width = 7.10 in, height = 4.85 in
s15.shapes.add_picture(ens_img_path, Inches(0.70), Inches(2.05), width=Inches(7.10))

# Right Explanatory Card (Architecture & Mechanics)
c_info = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.25), Inches(1.45), Inches(4.55), Inches(5.55))
c_info.fill.solid()
c_info.fill.fore_color.rgb = RGBColor(0xFA, 0xFA, 0xFC)
c_info.line.color.rgb = BORDER_GRAY
c_info.line.width = Pt(1.5)

tf_info = c_info.text_frame
tf_info.word_wrap = True
tf_info.margin_left = Inches(0.22)
tf_info.margin_right = Inches(0.22)
tf_info.margin_top = Inches(0.20)

p = tf_info.paragraphs[0]
p.text = "ENSEMBLE ARCHITECTURE"
p.font.name = "Calibri"
p.font.size = Pt(11.5)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT
p.space_after = Pt(6)

points = [
    ("Parallel Execution", "All 4 base classifiers (LR, SVM, RF, MNB) ingest identical TF-IDF vectors simultaneously."),
    ("Probability Calibration", "Logistic Regression, RF, and MNB output natural probabilities; SVM decision scores are calibrated to produce true probability distributions."),
    ("Soft Voting Consensus", "P_ensemble(c | x) = 1/4 Σ P_m(c | x) averages predicted probabilities across all 40 categories."),
    ("Argmax Decision Rule", "The final medical specialty is selected as the class that maximizes the aggregated ensemble probability: ŷ = argmax P_ensemble(c | x)."),
    ("Variance Reduction", "Compensates for individual estimator weaknesses, smoothing noise and stabilizing prediction on rare specialty classes.")
]

for title, desc in points:
    p = tf_info.add_paragraph()
    r1 = p.add_run()
    r1.text = "• " + title + ": "
    r1.font.name = "Calibri"
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = DARK_NAVY
    
    r2 = p.add_run()
    r2.text = desc
    r2.font.name = "Calibri"
    r2.font.size = Pt(9)
    r2.font.color.rgb = SLATE_DARK
    p.space_after = Pt(4)

print("Slide 15 updated with actual report diagram for Voting Ensemble.")

# =========================================================================
# 4. SLIDE 16: PROJECT PIPELINE DIAGRAM (FIGURE 13)
# =========================================================================
s16 = prs.slides[15]
sp_tree16 = s16.shapes._spTree

shapes_to_remove = []
for sh in s16.shapes:
    if sh.top > Inches(1.4) and sh.top < Inches(7.0):
        shapes_to_remove.append(sh)

for sh in shapes_to_remove:
    sp_tree16.remove(sh._element)

# Pipeline Container Card
c_pipe = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.45), Inches(12.30), Inches(5.55))
c_pipe.fill.solid()
c_pipe.fill.fore_color.rgb = WHITE
c_pipe.line.color.rgb = TEAL_ACCENT
c_pipe.line.width = Pt(1.5)

h_pipe = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.55), Inches(12.00), Inches(0.42))
h_pipe.fill.solid()
h_pipe.fill.fore_color.rgb = TEAL_ACCENT
h_pipe.line.fill.background()
p = h_pipe.text_frame.paragraphs[0]
p.text = "END-TO-END PROJECT PIPELINE DIAGRAM (FIGURE 13 FROM REPORT)"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Add Pipeline Image (1860x1480 or diagram_page_35_img_1.png)
pipe_img_path = r"D:\Antigravity Projects\Mini Project S3 MCA\extracted_diagrams\diagram_page_35_img_1.png"
if not os.path.exists(pipe_img_path):
    pipe_img_path = os.path.join(DIAG_DIR, "pipeline.png")

# Width = 11.50 in, height = 4.80 in
s16.shapes.add_picture(pipe_img_path, Inches(0.91), Inches(2.05), width=Inches(11.50))

print("Slide 16 updated with actual report diagram for Project Pipeline.")

# Close PowerPoint before saving to avoid lock
subprocess.run(["powershell", "-Command", "Stop-Process -Name POWERPNT -Force -ErrorAction SilentlyContinue"], capture_output=True)
time.sleep(1)

# Save
prs.save(PPTX_PATH)
print(f"Successfully saved to: {PPTX_PATH}")

try:
    prs.save(r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation.pptx")
    print("Also updated Downloads file.")
except Exception as e:
    print(f"Downloads note: {e}")

print("Report diagrams successfully integrated into presentation!")
