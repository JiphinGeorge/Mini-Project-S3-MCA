import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Define Palettes matching Presentation 1
DARK_BG = RGBColor(0x0A, 0x19, 0x2F)      # Deep Luxury Navy
LIGHT_BG = RGBColor(0xF6, 0xF8, 0xFB)     # Clean Slate-White
CARD_BG = RGBColor(0xFF, 0xFF, 0xFF)      # Pure White Card
CARD_BORDER = RGBColor(0xDC, 0xE2, 0xEC)  # Crisp Border
DARK_CARD = RGBColor(0x11, 0x22, 0x40)    # Dark Card Fill
DARK_TAG = RGBColor(0x13, 0x32, 0x54)     # Dark Tag Fill
TEAL_ACCENT = RGBColor(0x0E, 0x7C, 0x86)  # Signature Teal
NAVY_TITLE = RGBColor(0x0B, 0x1F, 0x3A)   # Deep Navy Title
TEXT_DARK = RGBColor(0x1E, 0x29, 0x3B)    # Slate Dark Text
TEXT_MUTED = RGBColor(0x55, 0x65, 0x7D)   # Muted Gray
TEXT_WHITE = RGBColor(0xFF, 0xFF, 0xFF)   # White
ACCENT_BLUE = RGBColor(0x25, 0x63, 0xEB)  # Royal Blue Accent
ACCENT_GREEN = RGBColor(0x0D, 0x94, 0x88) # Emerald Accent
GOLD_ACCENT = RGBColor(0xD9, 0x77, 0x06)  # Warm Amber/Gold
RED_ACCENT = RGBColor(0xDC, 0x26, 0x26)   # Danger / Red Accent
LIGHT_BLUE_BG = RGBColor(0xEE, 0xF2, 0xF6)# Subtle Blue Card

FONT_TITLE = 'Cambria'
FONT_BODY = 'Calibri'

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

img_perf = r'D:\Antigravity Projects\Mini Project S3 MCA\model training project\model_performance_comparison.png'
img_cm = r'D:\Antigravity Projects\Mini Project S3 MCA\model training project\best_model_confusion_matrix.png'

def set_slide_background(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, pill_text, title_text, slide_num, total_slides=16):
    # Pill Badge
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.32), Inches(4.5), Inches(0.34))
    pill.fill.solid()
    pill.fill.fore_color.rgb = TEAL_ACCENT
    pill.line.fill.background()
    tf = pill.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = pill_text
    p.alignment = PP_ALIGN.CENTER
    p.font.name = FONT_BODY
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    
    # Title
    t_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.68), Inches(12.13), Inches(0.65))
    tf2 = t_box.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = 0
    p2 = tf2.paragraphs[0]
    p2.text = title_text
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = NAVY_TITLE

    # Footer elements
    sep = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(7.05), Inches(12.13), Inches(0.015))
    sep.fill.solid()
    sep.fill.fore_color.rgb = CARD_BORDER
    sep.line.fill.background()

    f_left = slide.shapes.add_textbox(Inches(0.6), Inches(7.10), Inches(4.5), Inches(0.3))
    tf_l = f_left.text_frame
    tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = tf_l.margin_bottom = 0
    pl = tf_l.paragraphs[0]
    pl.text = "Department of Computer Applications | MACE"
    pl.font.name = FONT_BODY
    pl.font.size = Pt(9.5)
    pl.font.color.rgb = TEXT_MUTED

    f_center = slide.shapes.add_textbox(Inches(5.0), Inches(7.10), Inches(4.5), Inches(0.3))
    tf_c = f_center.text_frame
    tf_c.margin_left = tf_c.margin_right = tf_c.margin_top = tf_c.margin_bottom = 0
    pc = tf_c.paragraphs[0]
    pc.alignment = PP_ALIGN.CENTER
    pc.text = "Mar Athanasius College of Engineering, Kothamangalam"
    pc.font.name = FONT_BODY
    pc.font.size = Pt(9.5)
    pc.font.color.rgb = TEXT_MUTED

    f_right = slide.shapes.add_textbox(Inches(10.0), Inches(7.10), Inches(2.73), Inches(0.3))
    tf_r = f_right.text_frame
    tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = tf_r.margin_bottom = 0
    pr = tf_r.paragraphs[0]
    pr.alignment = PP_ALIGN.RIGHT
    pr.text = f"Slide {slide_num} of {total_slides}"
    pr.font.name = FONT_BODY
    pr.font.size = Pt(9.5)
    pr.font.bold = True
    pr.font.color.rgb = NAVY_TITLE

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
    else:
        card.line.fill.background()
    return card

card_w = Inches(5.9)
card_h = Inches(2.45)
coords = [
    (Inches(0.6), Inches(1.5)),
    (Inches(6.8), Inches(1.5)),
    (Inches(0.6), Inches(4.2)),
    (Inches(6.8), Inches(4.2))
]

# ==============================================================================
# SLIDE 1: Title Slide (Dark Theme)
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, DARK_BG)

t1 = s1.shapes.add_textbox(Inches(0.9), Inches(0.50), Inches(11.53), Inches(0.40))
tf1 = t1.text_frame
p1 = tf1.paragraphs[0]
p1.text = "MAR ATHANASIUS COLLEGE OF ENGINEERING, KOTHAMANGALAM"
p1.font.name = FONT_BODY
p1.font.size = Pt(13)
p1.font.bold = True
p1.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

pill1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.05), Inches(5.4), Inches(0.42))
pill1.fill.solid()
pill1.fill.fore_color.rgb = TEAL_ACCENT
pill1.line.fill.background()
tf_p1 = pill1.text_frame
p_p1 = tf_p1.paragraphs[0]
p_p1.text = "MCA MINI PROJECT  |  INTERIM PRESENTATION"
p_p1.alignment = PP_ALIGN.CENTER
p_p1.font.name = FONT_BODY
p_p1.font.size = Pt(12)
p_p1.font.bold = True
p_p1.font.color.rgb = TEXT_WHITE

t_title = s1.shapes.add_textbox(Inches(0.9), Inches(1.65), Inches(11.53), Inches(1.6))
tf_title = t_title.text_frame
tf_title.word_wrap = True
p_title = tf_title.paragraphs[0]
p_title.text = "Medical Specialty Classification Using NLP and Ensemble Machine Learning"
p_title.font.name = FONT_TITLE
p_title.font.size = Pt(32)
p_title.font.bold = True
p_title.font.color.rgb = TEXT_WHITE

p_sub = tf_title.add_paragraph()
p_sub.text = "Phase 2: Model Training, Class Imbalance Mitigation & Ensemble Evaluation"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(17)
p_sub.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8)
p_sub.space_before = Pt(8)

c_pres = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(3.60), Inches(5.6), Inches(2.35))
c_pres.fill.solid()
c_pres.fill.fore_color.rgb = DARK_CARD
c_pres.line.color.rgb = DARK_TAG
tf_pr = c_pres.text_frame
tf_pr.margin_left = Inches(0.35)
tf_pr.margin_top = Inches(0.25)
p_pr_h = tf_pr.paragraphs[0]
p_pr_h.text = "PRESENTED BY"
p_pr_h.font.name = FONT_BODY
p_pr_h.font.size = Pt(11)
p_pr_h.font.bold = True
p_pr_h.font.color.rgb = TEAL_ACCENT

p_name = tf_pr.add_paragraph()
p_name.text = "Jiphin George"
p_name.font.name = FONT_TITLE
p_name.font.size = Pt(20)
p_name.font.bold = True
p_name.font.color.rgb = TEXT_WHITE
p_name.space_before = Pt(4)

p_reg = tf_pr.add_paragraph()
p_reg.text = "Register No: MAC25MCA-2033\nCourse: Master of Computer Applications (MCA)\nDepartment of Computer Applications"
p_reg.font.name = FONT_BODY
p_reg.font.size = Pt(12)
p_reg.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)
p_reg.space_before = Pt(6)

c_guide = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.83), Inches(3.60), Inches(5.6), Inches(2.35))
c_guide.fill.solid()
c_guide.fill.fore_color.rgb = DARK_CARD
c_guide.line.color.rgb = DARK_TAG
tf_g = c_guide.text_frame
tf_g.margin_left = Inches(0.35)
tf_g.margin_top = Inches(0.25)
p_gh = tf_g.paragraphs[0]
p_gh.text = "PROJECT GUIDE"
p_gh.font.name = FONT_BODY
p_gh.font.size = Pt(11)
p_gh.font.bold = True
p_gh.font.color.rgb = TEAL_ACCENT

p_gname = tf_g.add_paragraph()
p_gname.text = "Prof. Biju Skaria"
p_gname.font.name = FONT_TITLE
p_gname.font.size = Pt(20)
p_gname.font.bold = True
p_gname.font.color.rgb = TEXT_WHITE
p_gname.space_before = Pt(4)

p_gdept = tf_g.add_paragraph()
p_gdept.text = "Department of Computer Applications\nMar Athanasius College of Engineering, Kothamangalam\nDate of Presentation: 30-09-2026"
p_gdept.font.name = FONT_BODY
p_gdept.font.size = Pt(12)
p_gdept.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)
p_gdept.space_before = Pt(6)

tags = ["Clinical NLP", "Imbalance Mitigation", "LR, SVM, RF, MNB", "Voting Ensembles", "Date: 30-09-2026"]
tag_w = Inches(2.23)
for i, tag in enumerate(tags):
    tg = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9 + i * 2.35), Inches(6.25), tag_w, Inches(0.42))
    tg.fill.solid()
    tg.fill.fore_color.rgb = DARK_TAG
    tg.line.fill.background()
    tf_tag = tg.text_frame
    p_t = tf_tag.paragraphs[0]
    p_t.text = tag
    p_t.alignment = PP_ALIGN.CENTER
    p_t.font.name = FONT_BODY
    p_t.font.size = Pt(10.5)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8)

# ==============================================================================
# SLIDE 2: Project Recap & Phase 1 Bridge
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2, LIGHT_BG)
add_header(s2, "MCA MINI PROJECT | PROJECT RECAP & BRIDGE", "Project Recap & Phase 1 Bridge", 2)

# Flow banner
banner2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.45), Inches(12.13), Inches(0.65))
banner2.fill.solid()
banner2.fill.fore_color.rgb = LIGHT_BLUE_BG
banner2.line.color.rgb = TEAL_ACCENT
tf_b2 = banner2.text_frame
p_b2 = tf_b2.paragraphs[0]
p_b2.text = "Phase 1: EDA & Problem Identification  →  Phase 2: Preprocessing → Baselines → Refinement → ML Training → Ensemble Evaluation"
p_b2.font.name = FONT_BODY
p_b2.font.size = Pt(12)
p_b2.font.bold = True
p_b2.font.color.rgb = NAVY_TITLE
p_b2.alignment = PP_ALIGN.CENTER

# Left Card: Phase 1 Scope
add_card(s2, Inches(0.6), Inches(2.3), Inches(5.9), Inches(4.5))
t_s2_l = s2.shapes.add_textbox(Inches(0.85), Inches(2.45), Inches(5.4), Inches(4.2))
tf_s2_l = t_s2_l.text_frame
tf_s2_l.word_wrap = True

p = tf_s2_l.paragraphs[0]
p.text = "Phase 1: Exploratory Data Analysis (Completed)"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

p1_points = [
    ("Focus of Phase 1", "Phase 1 focused strictly on Exploratory Data Analysis of the Kaggle MTSamples clinical dataset."),
    ("Dataset Collection & Inspection", "Audited 4,999 raw records across 6 attributes; identified and pruned 33 null transcription records (leaving 4,966 cleaned rows)."),
    ("Feature & Column Profiling", "Analyzed distributions of clinical text length, vocabulary density, and missing keyword attributes."),
    ("Class Frequency Audit", "Uncovered severe class imbalance across the raw 40 categorical labels (Surgery with 1,103 samples vs micro-classes with ≤ 10 samples)."),
    ("Scope Boundary", "NO model training, NO baseline evaluation, and NO ensemble experiments were conducted in Phase 1.")
]
for title, desc in p1_points:
    p_b = tf_s2_l.add_paragraph()
    p_b.text = f"• {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Right Card: Phase 2 Scope & Transition
add_card(s2, Inches(6.8), Inches(2.3), Inches(5.93), Inches(4.5))
t_s2_r = s2.shapes.add_textbox(Inches(7.05), Inches(2.45), Inches(5.43), Inches(4.2))
tf_s2_r = t_s2_r.text_frame
tf_s2_r.word_wrap = True

p = tf_s2_r.paragraphs[0]
p.text = "Phase 2: Full Machine Learning Pipeline"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN

p2_points = [
    ("Phase 2 Transition", "Phase 2 began by converting EDA findings into a complete, executable machine-learning classification pipeline."),
    ("All ML Started in Phase 2", "All text preprocessing, 40-class baselines, failure diagnosis, dataset refinement, model training, and ensembles were executed in Phase 2."),
    ("Initial Baseline Experimentation", "Tested raw 40-class classifiers; identified extreme collapse (7.85%–27.39% accuracy)."),
    ("Systematic Refinement", "Addressed high dimensionality (310k features) and label ambiguity, progressing from 40 classes → 20 classes → 8 clinical specialties."),
    ("Final Optimization & Evaluation", "Balanced feature matrices, trained LR, Linear SVM, RF, and MNB, and built Voting Ensembles targeting ≥ 75% accuracy.")
]
for title, desc in p2_points:
    p_b = tf_s2_r.add_paragraph()
    p_b.text = f"✓ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_GREEN
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 3: Phase 2: Initial Baseline Experiment
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, LIGHT_BG)
add_header(s3, "MCA MINI PROJECT | PHASE 2 BASELINE EXPERIMENT", "Phase 2: Initial 40-Class Baseline Experiment", 3)

# Left Side: Table of Baseline Results
add_card(s3, Inches(0.6), Inches(1.5), Inches(6.1), Inches(5.3))
t_s3_tbl = s3.shapes.add_textbox(Inches(0.85), Inches(1.65), Inches(5.6), Inches(0.4))
tf_s3t = t_s3_tbl.text_frame
p = tf_s3t.paragraphs[0]
p.text = "Initial 40-Class Model Accuracy (Phase 2 Experiment)"
p.font.name = FONT_TITLE
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

t3_rows = 7
t3_cols = 2
tbl_shape3 = s3.shapes.add_table(t3_rows, t3_cols, Inches(0.85), Inches(2.1), Inches(5.6), Inches(3.4))
tbl3 = tbl_shape3.table
tbl3.columns[0].width = Inches(3.8)
tbl3.columns[1].width = Inches(1.8)

headers3 = ["Candidate Baseline Model", "Test Accuracy"]
for j, h in enumerate(headers3):
    cell = tbl3.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TITLE
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    if j > 0:
        p.alignment = PP_ALIGN.RIGHT

data_s3 = [
    ("Random Forest", "7.85%"),
    ("Linear SVM", "10.67%"),
    ("Balanced Linear SVM", "10.07%"),
    ("Logistic Regression", "22.96%"),
    ("Weighted Multinomial Naive Bayes", "27.09%"),
    ("Balanced Logistic Regression", "27.39%")
]
for i, row in enumerate(data_s3):
    for j, val in enumerate(row):
        cell = tbl3.cell(i+1, j)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        if "Balanced" in row[0] or "Weighted" in row[0]:
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BLUE_BG
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_BODY
        p.font.size = Pt(10)
        p.font.color.rgb = RED_ACCENT if j == 1 and float(val.replace('%','')) < 15 else NAVY_TITLE
        if j > 0:
            p.alignment = PP_ALIGN.RIGHT
            p.font.bold = True

t_callout = s3.shapes.add_textbox(Inches(0.85), Inches(5.65), Inches(5.6), Inches(0.95))
tf_co = t_callout.text_frame
tf_co.word_wrap = True
p = tf_co.paragraphs[0]
p.text = "⚠ Empirical Finding: The raw 40-class formulation was completely unsuitable for clinical deployment, with every model failing to exceed 27.4% accuracy."
p.font.name = FONT_BODY
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = RED_ACCENT

# Right Side: Why the Baseline Failed
add_card(s3, Inches(6.9), Inches(1.5), Inches(5.83), Inches(5.3))
t_s3_r = s3.shapes.add_textbox(Inches(7.15), Inches(1.7), Inches(5.33), Inches(4.9))
tf_s3_r = t_s3_r.text_frame
tf_s3_r.word_wrap = True

p = tf_s3_r.paragraphs[0]
p.text = "Baseline Failure Observations"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

base_fails = [
    ("Unconstrained Feature Explosion", "TF-IDF generated 310,298 unigram and bigram features for only 3,971 training samples, causing severe sparsity and overfitting."),
    ("Trivial Majority Prediction", "Unweighted Logistic Regression predicted 'Surgery' almost exclusively, securing 22.96% accuracy simply because Surgery represented 22.2% of the dataset."),
    ("Tree-Based Model Collapse", "Random Forest collapsed to 7.85% accuracy as random feature subsets in a 310k-dimension space almost never contained discriminative terms."),
    ("Non-Specialty Document Contamination", "Classes like 'SOAP Notes' and 'Discharge Summary' contained vocabulary identical to true clinical specialties, making mathematical separation impossible.")
]
for title, desc in base_fails:
    p_b = tf_s3_r.add_paragraph()
    p_b.text = f"• {title}:\n"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 4: Baseline Problem Diagnosis
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, LIGHT_BG)
add_header(s4, "MCA MINI PROJECT | PROBLEM DIAGNOSIS", "Baseline Problem Diagnosis: Three Core Obstacles", 4)

diag_cards = [
    ("1. Severe Class Imbalance", RED_ACCENT,
     "• 40 raw categories with extreme distribution skew.\n• Surgery alone comprised 1,103 samples (22.2%).\n• Minority classes had as few as 2–10 samples:\n  - Autopsy: 2 samples\n  - Executive Evaluation: 2 samples\n  - Lab Medicine: 8 samples\n• Imbalance ratio exceeded 184:1, starving minority classes of gradient and decision updates during training."),
    
    ("2. High-Dimensional TF-IDF", GOLD_ACCENT,
     "• Unconstrained vocabulary generated 310,298 features.\n• Only 3,971 training records in the 80% split.\n• Massive feature-to-sample ratio (> 78:1) created severe data sparsity.\n• Non-informative filler words and rare typographical tokens diluted diagnostic signal, crippling distance- and tree-based estimators."),
    
    ("3. Clinical Label Ambiguity", TEAL_ACCENT,
     "• Inherent conflict between clinical specialties and document formats:\n  - Consult - History and Phy.: 516 records\n  - SOAP / Progress Notes: 166 records\n  - Discharge Summary: 108 records\n  - Emergency Room Reports: 75 records\n  - Office Notes: 50 records\n• These describe document structures, not medical organ specialties, introducing overlapping vocabularies across domains.")
]

c_w4 = Inches(3.85)
gap4 = Inches(0.28)
for idx, (title, color_h, body) in enumerate(diag_cards):
    cx = Inches(0.6 + idx * (c_w4 + gap4))
    add_card(s4, cx, Inches(1.5), c_w4, Inches(5.3))
    tb = s4.shapes.add_textbox(cx + Inches(0.2), Inches(1.7), c_w4 - Inches(0.4), Inches(4.9))
    tf_d = tb.text_frame
    tf_d.word_wrap = True
    
    p = tf_d.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = color_h
    
    p_b = tf_d.add_paragraph()
    p_b.text = body
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10)
    p_b.font.color.rgb = TEXT_DARK
    p_b.space_before = Pt(8)

# ==============================================================================
# SLIDE 5: Phase 2 Dataset Refinement (Iterative Process)
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, LIGHT_BG)
add_header(s5, "MCA MINI PROJECT | DATASET REFINEMENT", "Phase 2 Dataset Refinement: Iterative Optimization", 5)

steps_refine = [
    ("Iteration 1: 40 Raw Classes (Baseline)", RED_ACCENT,
     "• Scope: All 4,966 cleaned records across 40 raw categories.\n• Outcome: Severe model collapse (7.85% to 27.39% accuracy).\n• Diagnosis: Severe 184:1 imbalance, 310k unconstrained features, and procedural/document label overlap made accurate learning impossible."),
    
    ("Iteration 2: 20-Class Threshold Filtering", GOLD_ACCENT,
     "• Scope: Pruned micro-classes with fewer than 50 samples.\n• Retained 20 moderate-to-large categories (~3,800 records).\n• Outcome: Accuracy improved marginally into the 40%–50% range.\n• Remaining Issue: Heavy semantic overlap persisted between 'Surgery' and individual operative specialties, along with document-type noise ('Consults', 'SOAP Notes')."),
    
    ("Iteration 3: 8 Focused Clinical Specialties", ACCENT_GREEN,
     "• Scope: Curated 8 core mutually exclusive organ-system specialties (1,663 records).\n• Removed umbrella procedural labels ('Surgery') and administrative document formats.\n• Outcome: Dramatic performance jump to 77.48%–88.59% accuracy across all models.\n• Clinical Significance: Clear anatomical boundaries provide pristine diagnostic separation.")
]

for idx, (title, color_h, body) in enumerate(steps_refine):
    cx = Inches(0.6 + idx * (c_w4 + gap4))
    add_card(s5, cx, Inches(1.5), c_w4, Inches(5.3))
    tb = s5.shapes.add_textbox(cx + Inches(0.2), Inches(1.7), c_w4 - Inches(0.4), Inches(4.9))
    tf_r = tb.text_frame
    tf_r.word_wrap = True
    
    p = tf_r.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = color_h
    
    p_b = tf_r.add_paragraph()
    p_b.text = body
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10)
    p_b.font.color.rgb = TEXT_DARK
    p_b.space_before = Pt(8)

# ==============================================================================
# SLIDE 6: Final 8-Specialty Dataset
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, LIGHT_BG)
add_header(s6, "MCA MINI PROJECT | CURATED DATASET", "Final 8-Specialty Clinical Dataset (1,663 Records)", 6)

# Left: 8 Specialties Breakdown Table
add_card(s6, Inches(0.6), Inches(1.5), Inches(6.8), Inches(5.3))
t_s6_tbl = s6.shapes.add_textbox(Inches(0.85), Inches(1.65), Inches(6.3), Inches(0.4))
tf_s6t = t_s6_tbl.text_frame
p = tf_s6t.paragraphs[0]
p.text = "Curated Mutually Exclusive Clinical Specialties"
p.font.name = FONT_TITLE
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

t6_rows = 10
t6_cols = 3
tbl_shape6 = s6.shapes.add_table(t6_rows, t6_cols, Inches(0.85), Inches(2.1), Inches(6.3), Inches(4.4))
tbl6 = tbl_shape6.table
tbl6.columns[0].width = Inches(3.5)
tbl6.columns[1].width = Inches(1.4)
tbl6.columns[2].width = Inches(1.4)

headers6 = ["Medical Specialty", "Record Count", "Proportion"]
for j, h in enumerate(headers6):
    cell = tbl6.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TITLE
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    if j > 0:
        p.alignment = PP_ALIGN.RIGHT

data_s6 = [
    ("Cardiovascular / Pulmonary", "371", "22.31%"),
    ("Orthopedic", "355", "21.35%"),
    ("Gastroenterology", "224", "13.47%"),
    ("Neurology", "223", "13.41%"),
    ("Urology", "156", "9.38%"),
    ("Obstetrics / Gynecology", "155", "9.32%"),
    ("ENT - Otolaryngology", "96", "5.77%"),
    ("Ophthalmology", "83", "4.99%"),
    ("Total Curated Dataset", "1,663", "100.00%")
]
for i, row in enumerate(data_s6):
    for j, val in enumerate(row):
        cell = tbl6.cell(i+1, j)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        if i == len(data_s6)-1:
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BLUE_BG
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        if i == len(data_s6)-1:
            p.font.bold = True
            p.font.color.rgb = NAVY_TITLE
        else:
            p.font.color.rgb = TEXT_DARK
        if j > 0:
            p.alignment = PP_ALIGN.RIGHT

# Right: Clinical Rationale
add_card(s6, Inches(7.6), Inches(1.5), Inches(5.13), Inches(5.3))
t_s6_r = s6.shapes.add_textbox(Inches(7.8), Inches(1.7), Inches(4.73), Inches(4.9))
tf_s6_r = t_s6_r.text_frame
tf_s6_r.word_wrap = True

p = tf_s6_r.paragraphs[0]
p.text = "Clinical Rationale for Selection"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

rat_points = [
    ("Organ-System Distinctiveness", "Each selected department corresponds to a distinct anatomical system with distinct vocabulary (e.g., cardiac vessels, musculoskeletal joints, digestive tract)."),
    ("Elimination of Category Ambiguity", "Excluded procedural umbrellas like 'Surgery' which contaminated cardiac, orthopedic, and gastrointestinal procedures simultaneously."),
    ("Pruning Administrative Formats", "Excluded SOAP notes, consultations, and discharge summaries that represent hospital document templates rather than clinical domains."),
    ("Balanced Multi-Class Cohort", "Maintains sufficient representation across all 8 classes (83 to 371 samples) while preserving clinical realism.")
]
for title, desc in rat_points:
    p_b = tf_s6_r.add_paragraph()
    p_b.text = f"✓ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_GREEN
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 7: Text Preprocessing & TF-IDF
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, LIGHT_BG)
add_header(s7, "MCA MINI PROJECT | FEATURE ENGINEERING", "Text Preprocessing & TF-IDF Feature Engineering", 7)

# Left: Text Preprocessing
add_card(s7, Inches(0.6), Inches(1.5), Inches(5.9), Inches(5.3))
t_s7_l = s7.shapes.add_textbox(Inches(0.85), Inches(1.7), Inches(5.4), Inches(4.9))
tf_s7_l = t_s7_l.text_frame
tf_s7_l.word_wrap = True

p = tf_s7_l.paragraphs[0]
p.text = "Clinical Narrative Preprocessing"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

prep_steps = [
    ("Enriched Feature Construction", "Synthesized a unified 'clinical_text' field by concatenating the clinical 'description' (abstract summary) and 'transcription' (full dictation)."),
    ("Normalization & Noise Removal", "Converted all narratives to lowercase; stripped punctuation, formatting escapes, and non-ASCII character noise."),
    ("Alphanumeric Token Filtering", "Retained clinical terms, drug dosages, and surgical abbreviations while eliminating solitary numerical fragments."),
    ("Stop-Word Filtration", "Removed general English stop-words and non-informative clinical filler terms while preserving essential diagnostic terminology."),
    ("Morphological Lemmatization", "Standardized anatomical and surgical variants to base lemmas using NLTK WordNetLemmatizer.")
]
for title, desc in prep_steps:
    p_b = tf_s7_l.add_paragraph()
    p_b.text = f"• {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Right: TF-IDF Configuration
add_card(s7, Inches(6.8), Inches(1.5), Inches(5.93), Inches(5.3))
t_s7_r = s7.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.43), Inches(4.9))
tf_s7_r = t_s7_r.text_frame
tf_s7_r.word_wrap = True

p = tf_s7_r.paragraphs[0]
p.text = "TF-IDF Vectorizer Architecture"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

tfidf_spec = [
    ("max_features = 8,000", "Constrained high dimensionality from 310k+ to top 8,000 discriminative features to eliminate overfitting."),
    ("ngram_range = (1, 2)", "Captured unigrams ('stent', 'cataract') and bigrams ('coronary artery', 'lumbar spine')."),
    ("sublinear_tf = True", "Replaced raw TF with (1 + log(TF)) scaling to dampen overly repetitive terms."),
    ("min_df = 2, max_df = 0.7", "Pruned singleton words and filtered ubiquitous tokens occurring in > 70% of documents."),
    ("norm = 'l2' (L2 Normalization)", "Normalized document vector lengths, making representation invariant to report length."),
    ("Strict Anti-Leakage Partitioning", "Fitted ONLY on training data (1,330 samples); test data (333 samples) strictly transformed.")
]
for title, desc in tfidf_spec:
    p_b = tf_s7_r.add_paragraph()
    p_b.text = f"✓ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_GREEN
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

p_mat = tf_s7_r.add_paragraph()
p_mat.text = "Resulting Feature Matrices:\n• Training Matrix: 1,330 × 8,000  |  Testing Matrix: 333 × 8,000"
p_mat.font.name = FONT_BODY
p_mat.font.size = Pt(11)
p_mat.font.bold = True
p_mat.font.color.rgb = TEAL_ACCENT
p_mat.space_before = Pt(8)

# ==============================================================================
# SLIDE 8: Class Imbalance Mitigation
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, LIGHT_BG)
add_header(s8, "MCA MINI PROJECT | IMBALANCE MITIGATION", "Class Imbalance Mitigation Techniques in Phase 2", 8)

imb_techniques = [
    ("1. Algorithmic Cost Weighting (class_weight='balanced')", NAVY_TITLE,
     "• Applied natively across: Logistic Regression, Linear SVM, and Random Forest.\n• Mechanism: Automatically adjusts loss-function penalties inversely proportional to class frequencies:\n  w_j = N / (K · n_j)\n• Impact: Penalizes majority-class false predictions more heavily, preventing models from sacrificing minority classes like Ophthalmology (83) and ENT (96)."),
    
    ("2. Synthetic Minority Over-sampling (SMOTE)", TEAL_ACCENT,
     "• Applied strictly to the training fold (never on test data to preserve evaluation integrity).\n• Configuration: k_neighbors = 3 (tailored for sparse medical text representations).\n• Mechanism: Generates synthetic feature vectors along line segments connecting k-nearest minority neighbors, enriching minority decision regions."),
    
    ("3. Random Over-Sampling (ROS)", GOLD_ACCENT,
     "• Evaluated to boost minority-class representation during iterative experimentation.\n• Duplicates minority instances to balance gradient propagation across rare specialty categories."),
    
    ("Core Engineering Objective", ACCENT_GREEN,
     "• Objective: Prevent the models from being dominated by majority classes while preserving an uncorrupted, unseen test set of 333 held-out records.\n• Preserves exact stratified class proportions in the 20% test partition for unbiased clinical validation.")
]

for idx, (title, color_h, body) in enumerate(imb_techniques):
    cx, cy = coords[idx]
    add_card(s8, cx, cy, card_w, card_h)
    tb = s8.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
    tf_i = tb.text_frame
    tf_i.word_wrap = True
    
    p = tf_i.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = color_h
    
    p_b = tf_i.add_paragraph()
    p_b.text = body
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(9.5)
    p_b.font.color.rgb = TEXT_DARK
    p_b.space_before = Pt(4)

# ==============================================================================
# SLIDE 9: Model Training
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, LIGHT_BG)
add_header(s9, "MCA MINI PROJECT | MODEL TRAINING", "Model Training: Four Core Supervised ML Algorithms", 9)

models_train = [
    ("1. Linear Support Vector Machine (LinearSVC)",
     "Config: C = 1.0, class_weight = 'balanced', max_iter = 3000",
     "• Why Tested: SVMs excel on high-dimensional sparse text vectors by finding the maximum-margin hyperplane.\n• Training Behavior: Linear kernel separates 8,000 TF-IDF features with minimal computational overhead.\n• Regularization: L2 penalty ($C=1.0$) prevents overfitting on minority classes."),
    
    ("2. Logistic Regression (Multinomial)",
     "Config: Multinomial Softmax, class_weight = 'balanced', max_iter = 1000",
     "• Why Tested: Provides a well-calibrated probabilistic baseline with direct clinical interpretability.\n• Training Behavior: Optimizes multinomial cross-entropy with L2 regularization penalty.\n• Output: Produces natural class probability distributions for ensemble voting."),
    
    ("3. Random Forest Classifier",
     "Config: n_estimators = 100, max_depth = 25, class_weight = 'balanced'",
     "• Why Tested: Evaluates whether bagging non-linear decision trees captures keyword interactions.\n• Training Behavior: Ensembles 100 decorrelated trees with random feature subsampling.\n• Constraints: max_depth=25 prevents individual trees from memorizing sparse training text."),
    
    ("4. Multinomial Naive Bayes (MNB)",
     "Config: alpha = 0.5 (Additive Laplace Smoothing)",
     "• Why Tested: Standard generative text benchmark based on conditional word frequencies.\n• Training Behavior: Extremely rapid closed-form training with zero iterative gradient steps.\n• Smoothing: alpha=0.5 prevents zero-probability traps for rare clinical vocabulary.")
]

for idx, (title, cfg, body) in enumerate(models_train):
    cx, cy = coords[idx]
    add_card(s9, cx, cy, card_w, card_h)
    tb = s9.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
    tf_m = tb.text_frame
    tf_m.word_wrap = True
    
    p = tf_m.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY_TITLE
    
    p_c = tf_m.add_paragraph()
    p_c.text = cfg
    p_c.font.name = FONT_BODY
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = TEAL_ACCENT
    p_c.space_before = Pt(2)
    
    p_b = tf_m.add_paragraph()
    p_b.text = body
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(9)
    p_b.font.color.rgb = TEXT_DARK
    p_b.space_before = Pt(3)

# ==============================================================================
# SLIDE 10: Voting Ensembles
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, LIGHT_BG)
add_header(s10, "MCA MINI PROJECT | ENSEMBLE LEARNING", "Hard & Soft Voting Ensemble Architectures", 10)

# Left: Hard Voting
add_card(s10, Inches(0.6), Inches(1.5), Inches(5.9), Inches(5.3))
t_s10_l = s10.shapes.add_textbox(Inches(0.85), Inches(1.7), Inches(5.4), Inches(4.9))
tf_s10_l = t_s10_l.text_frame
tf_s10_l.word_wrap = True

p = tf_s10_l.paragraphs[0]
p.text = "Hard Voting Ensemble (Majority Rule)"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

hard_points = [
    ("Consensus Mechanism", "Aggregates discrete class predictions across the 4 base classifiers (LR, SVM, RF, MNB) and assigns the final label via majority vote: ŷ = mode(ŷ_1, ŷ_2, ŷ_3, ŷ_4)."),
    ("Non-Probabilistic Decision", "Operates directly on predicted class labels without requiring probability outputs."),
    ("Empirical Performance", "Achieved 87.09% accuracy and 0.8846 Macro F1 on the 333 test samples, matching Logistic Regression."),
    ("Limitation", "Treats high-confidence and borderline predictions with equal weight, discarding nuanced confidence margins.")
]
for title, desc in hard_points:
    p_b = tf_s10_l.add_paragraph()
    p_b.text = f"• {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Right: Soft Voting
add_card(s10, Inches(6.8), Inches(1.5), Inches(5.93), Inches(5.3))
t_s10_r = s10.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.43), Inches(4.9))
tf_s10_r = t_s10_r.text_frame
tf_s10_r.word_wrap = True

p = tf_s10_r.paragraphs[0]
p.text = "Soft Voting Ensemble (Weighted Probability)"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

soft_points2 = [
    ("Linear SVM Probability Calibration", "LinearSVC natively outputs raw hyperplane distances. Used CalibratedClassifierCV with Platt scaling to produce valid posterior probabilities P(c | x)."),
    ("Weighted Consensus Formula", "Combined class probabilities with empirical weights [LR:2, SVM:2, RF:1, MNB:1]:\n  P_ensemble = (2·P_LR + 2·P_SVM + P_RF + P_MNB) / 6"),
    ("Decision Rule", "Final specialty assigned by argmax: ŷ = argmax P_ensemble(c | x)."),
    ("Why Investigated", "Soft voting captures model certainty, smoothing out individual estimator noise and stabilizing predictions across diverse model families (87.99% accuracy / 0.8898 Macro F1).")
]
for title, desc in soft_points2:
    p_b = tf_s10_r.add_paragraph()
    p_b.text = f"✓ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_GREEN
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 11: Model Performance Comparison
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11, LIGHT_BG)
add_header(s11, "MCA MINI PROJECT | EVALUATION BENCHMARK", "Model Performance Comparison (Final 8-Specialty Results)", 11)

# Left: Full Table
add_card(s11, Inches(0.6), Inches(1.5), Inches(6.8), Inches(5.3))
t_s11_tbl = s11.shapes.add_textbox(Inches(0.85), Inches(1.65), Inches(6.3), Inches(0.4))
tf_s11t = t_s11_tbl.text_frame
p = tf_s11t.paragraphs[0]
p.text = "Final Evaluation Benchmark (333 Held-Out Test Records)"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

t11_rows = 7
t11_cols = 6
tbl_shape11 = s11.shapes.add_table(t11_rows, t11_cols, Inches(0.85), Inches(2.1), Inches(6.3), Inches(3.6))
tbl11 = tbl_shape11.table
tbl11.columns[0].width = Inches(2.3)
tbl11.columns[1].width = Inches(0.8)
tbl11.columns[2].width = Inches(0.8)
tbl11.columns[3].width = Inches(0.8)
tbl11.columns[4].width = Inches(0.8)
tbl11.columns[5].width = Inches(0.8)

headers11 = ["Model Architecture", "Accuracy", "Macro Prec", "Macro Rec", "Macro F1", "Weighted F1"]
for j, h in enumerate(headers11):
    cell = tbl11.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TITLE
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = FONT_BODY
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    if j > 0:
        p.alignment = PP_ALIGN.RIGHT

data_s11 = [
    ("Linear SVM (Best Model)", "0.8859", "0.9051", "0.8902", "0.8971", "0.8862"),
    ("Soft Voting Ensemble", "0.8799", "0.9041", "0.8795", "0.8898", "0.8818"),
    ("Logistic Regression", "0.8709", "0.8966", "0.8768", "0.8846", "0.8730"),
    ("Hard Voting Ensemble", "0.8709", "0.8966", "0.8768", "0.8846", "0.8730"),
    ("Random Forest", "0.8198", "0.8340", "0.8257", "0.8274", "0.8209"),
    ("Multinomial Naive Bayes", "0.7748", "0.8602", "0.7331", "0.7743", "0.7824")
]
for i, row in enumerate(data_s11):
    for j, val in enumerate(row):
        cell = tbl11.cell(i+1, j)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        if i == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(0xFE, 0xF3, 0xC7) # Soft Gold
        elif i == 1:
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(0xEC, 0xFD, 0xF5) # Soft Green
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_BODY
        p.font.size = Pt(8.5)
        if i < 2:
            p.font.bold = True
            p.font.color.rgb = NAVY_TITLE
        else:
            p.font.color.rgb = TEXT_DARK
        if j > 0:
            p.alignment = PP_ALIGN.RIGHT

# Highlights box below table
tb_bot11 = s11.shapes.add_textbox(Inches(0.85), Inches(5.8), Inches(6.3), Inches(0.85))
tf_b11 = tb_bot11.text_frame
tf_b11.word_wrap = True
p = tf_b11.paragraphs[0]
p.text = "★ Best Individual: Linear SVM — 88.59% Accuracy | 0.8971 Macro F1\n★ Best Ensemble: Soft Voting — 87.99% Accuracy | 0.8898 Macro F1\n✓ All 6 configurations comfortably beat the required 75.0% project target threshold."
p.font.name = FONT_BODY
p.font.size = Pt(9.5)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN

# Right: Chart Image
add_card(s11, Inches(7.6), Inches(1.5), Inches(5.13), Inches(5.3))
if os.path.exists(img_perf):
    s11.shapes.add_picture(img_perf, Inches(7.75), Inches(1.65), width=Inches(4.83), height=Inches(4.95))

# ==============================================================================
# SLIDE 12: Confusion Matrix & Classification Analysis
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12, LIGHT_BG)
add_header(s12, "MCA MINI PROJECT | CONFUSION MATRIX", "Confusion Matrix & Classification Analysis", 12)

# Left: CM Heatmap
add_card(s12, Inches(0.6), Inches(1.5), Inches(5.8), Inches(5.3))
if os.path.exists(img_cm):
    s12.shapes.add_picture(img_cm, Inches(0.75), Inches(1.65), width=Inches(5.5), height=Inches(4.95))

# Right: Diagonal & Pattern Analysis
add_card(s12, Inches(6.6), Inches(1.5), Inches(6.13), Inches(5.3))
t_s12_r = s12.shapes.add_textbox(Inches(6.8), Inches(1.7), Inches(5.7), Inches(4.9))
tf_s12_r = t_s12_r.text_frame
tf_s12_r.word_wrap = True

p = tf_s12_r.paragraphs[0]
p.text = "Diagnostic Classification Patterns"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

cm_analysis = [
    ("Heavy Diagonal Concentration", "295 out of 333 test instances correctly classified (88.59%), confirming sharp decision boundaries across most clinical specialties."),
    ("Easiest Specialty to Distinguish: Ophthalmology", "17 out of 17 correct (100% precision & recall, 0 misclassifications) due to unique eye-specific clinical terminology (e.g. 'phacoemulsification', 'corneal')."),
    ("High Diagnostic Separation", "Zero cross-domain confusion between unrelated organ systems (e.g. Ophthalmology vs Cardiovascular, Urology vs Orthopedic)."),
    ("Hardest Boundary: Neurology ↔ Orthopedic", "Accounts for 12 of the 38 total misclassifications:\n• 7 Orthopedic cases misclassified as Neurology\n• 5 Neurology cases misclassified as Orthopedic"),
    ("Linguistic Root Cause of Error", "Shared operative terminology in spinal procedures (e.g., lumbar discectomy, radiculopathy, disc herniation, and nerve root decompression) where nerve and bone tissue co-occur.")
]
for title, desc in cm_analysis:
    p_b = tf_s12_r.add_paragraph()
    p_b.text = f"• {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 13: Specialty-wise Performance
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
set_slide_background(s13, LIGHT_BG)
add_header(s13, "MCA MINI PROJECT | DETAILED EVALUATION", "Specialty-wise Classification Performance (Final Report)", 13)

# Left: Exact Classification Report Table
add_card(s13, Inches(0.6), Inches(1.5), Inches(7.5), Inches(5.3))
t_s13_tbl = s13.shapes.add_textbox(Inches(0.85), Inches(1.65), Inches(7.0), Inches(0.4))
tf_s13t = t_s13_tbl.text_frame
p = tf_s13t.paragraphs[0]
p.text = "Per-Class Classification Report (Best Model: Linear SVM)"
p.font.name = FONT_TITLE
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

t13_rows = 12
t13_cols = 5
tbl_shape13 = s13.shapes.add_table(t13_rows, t13_cols, Inches(0.85), Inches(2.1), Inches(7.0), Inches(4.4))
tbl13 = tbl_shape13.table
tbl13.columns[0].width = Inches(3.0)
tbl13.columns[1].width = Inches(1.0)
tbl13.columns[2].width = Inches(1.0)
tbl13.columns[3].width = Inches(1.0)
tbl13.columns[4].width = Inches(1.0)

headers13 = ["Medical Specialty", "Precision", "Recall", "F1-Score", "Support"]
for j, h in enumerate(headers13):
    cell = tbl13.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TITLE
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    if j > 0:
        p.alignment = PP_ALIGN.RIGHT

data_s13 = [
    ("Cardiovascular / Pulmonary", "0.88", "0.92", "0.90", "74"),
    ("ENT - Otolaryngology", "0.94", "0.84", "0.89", "19"),
    ("Gastroenterology", "0.87", "0.89", "0.88", "45"),
    ("Neurology", "0.76", "0.78", "0.77", "45"),
    ("Obstetrics / Gynecology", "0.93", "0.90", "0.92", "31"),
    ("Ophthalmology", "1.00", "1.00", "1.00", "17"),
    ("Orthopedic", "0.89", "0.89", "0.89", "71"),
    ("Urology", "0.97", "0.90", "0.93", "31"),
    ("Accuracy", "", "", "0.89", "333"),
    ("Macro Average", "0.91", "0.89", "0.90", "333"),
    ("Weighted Average", "0.89", "0.89", "0.89", "333")
]
for i, row in enumerate(data_s13):
    for j, val in enumerate(row):
        cell = tbl13.cell(i+1, j)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        if i == 5:
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(0xEC, 0xFD, 0xF5) # soft green
        elif i >= 8:
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BLUE_BG
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_BODY
        p.font.size = Pt(9)
        if i == 5 or i >= 8:
            p.font.bold = True
            p.font.color.rgb = NAVY_TITLE
        else:
            p.font.color.rgb = TEXT_DARK
        if j > 0:
            p.alignment = PP_ALIGN.RIGHT

# Right: Observations
add_card(s13, Inches(8.35), Inches(1.5), Inches(4.38), Inches(5.3))
t_s13_r = s13.shapes.add_textbox(Inches(8.55), Inches(1.7), Inches(3.98), Inches(4.9))
tf_s13_r = t_s13_r.text_frame
tf_s13_r.word_wrap = True

p = tf_s13_r.paragraphs[0]
p.text = "Specialty-wise Observations"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

spec_obs = [
    ("Ophthalmology: Flawless Generalization", "1.00 F1-score across all 17 test cases with 100% precision and recall."),
    ("High Precision Specialties", "Urology (0.97 Precision), ENT (0.94 Precision), and OB/GYN (0.93 Precision) demonstrate exceptional specificity."),
    ("Robust Majority Classes", "Cardiovascular / Pulmonary (0.90 F1) and Orthopedic (0.89 F1) maintain high recall despite being the largest classes."),
    ("Challenging Class", "Neurology (0.77 F1) reflects the semantic overlap with Orthopedic spinal cases.")
]
for title, desc in spec_obs:
    p_b = tf_s13_r.add_paragraph()
    p_b.text = f"★ {title}:\n"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 14: Key Findings
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
set_slide_background(s14, LIGHT_BG)
add_header(s14, "MCA MINI PROJECT | EMPIRICAL FINDINGS", "Key Empirical Findings from Phase 2", 14)

findings8 = [
    ("1. Raw 40-Class Formulation Failed",
     "• Initial 40-class training produced 7.85% to 27.39% accuracy, demonstrating that the raw dataset was unsuitable without domain refinement."),
    
    ("2. Severe Class Imbalance Distorted Learning",
     "• Extreme 184:1 skew starved minority classes; unweighted models predicted majority 'Surgery' trivially. Class weighting and SMOTE restored balanced gradients."),
    
    ("3. 310,000-Feature TF-IDF Created Sparsity Trap",
     "• Unconstrained TF-IDF severely overfitted (78:1 feature-to-sample ratio). Restricting to 8,000 features with sublinear scaling stabilized feature space."),
    
    ("4. Pruning Document Formats Cleared Noise",
     "• Removing administrative formats (SOAP notes, consults, discharge summaries) eliminated non-specialty linguistic overlap."),
    
    ("5. Final 8-Specialty Dataset Achieved 77%–89%",
     "• Focusing on 8 mutually exclusive clinical departments dramatically elevated performance across all 4 machine-learning algorithms."),
    
    ("6. Linear SVM Delivered Top Individual Accuracy",
     "• Linear SVM achieved 88.59% accuracy and 0.8971 Macro F1, outperforming Random Forest by > 6.6% due to optimal high-dimensional text separation."),
    
    ("7. Soft Voting Produced Robust Ensemble Generalization",
     "• Weighted probability consensus (2:2:1:1) achieved 87.99% accuracy and 0.8898 Macro F1, providing smooth confidence calibration."),
    
    ("8. Controlled TF-IDF Drastically Reduced Dimensionality",
     "• 8,000 features with sublinear TF scaling provided compact, highly discriminative vectors yielding sub-15ms CPU inference.")
]

card_w14 = Inches(5.9)
card_h14 = Inches(1.18)
coords14 = [
    (Inches(0.6), Inches(1.5)),
    (Inches(6.8), Inches(1.5)),
    (Inches(0.6), Inches(2.85)),
    (Inches(6.8), Inches(2.85)),
    (Inches(0.6), Inches(4.2)),
    (Inches(6.8), Inches(4.2)),
    (Inches(0.6), Inches(5.55)),
    (Inches(6.8), Inches(5.55))
]

for idx, (title, body) in enumerate(findings8):
    cx, cy = coords14[idx]
    add_card(s14, cx, cy, card_w14, card_h14)
    tb = s14.shapes.add_textbox(cx + Inches(0.15), cy + Inches(0.08), card_w14 - Inches(0.3), card_h14 - Inches(0.16))
    tf_f = tb.text_frame
    tf_f.word_wrap = True
    
    p = tf_f.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = NAVY_TITLE
    
    p_b = tf_f.add_paragraph()
    p_b.text = body
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(8.5)
    p_b.font.color.rgb = TEXT_DARK
    p_b.space_before = Pt(2)

# ==============================================================================
# SLIDE 15: Current Status & Next Phase
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
set_slide_background(s15, LIGHT_BG)
add_header(s15, "MCA MINI PROJECT | PROJECT STATUS", "Current Project Status & Phase 3 Roadmap", 15)

# Left: Completed in Phase 2
add_card(s15, Inches(0.6), Inches(1.5), Inches(5.9), Inches(5.3))
t_s15_l = s15.shapes.add_textbox(Inches(0.85), Inches(1.7), Inches(5.4), Inches(4.9))
tf_s15_l = t_s15_l.text_frame
tf_s15_l.word_wrap = True

p = tf_s15_l.paragraphs[0]
p.text = "Completed in Phase 2"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN

comp_phase2 = [
    ("EDA Findings Incorporated", "Transferred Phase 1 data characteristics into ML pipeline design."),
    ("40-Class Baseline Benchmark", "Trained and evaluated initial models; documented collapse."),
    ("Class Imbalance Analysis", "Identified 184:1 skew and 310k feature explosion."),
    ("20-Class Filtering Experiment", "Pruned <50 sample classes; analyzed persistent semantic overlap."),
    ("Final 8-Specialty Dataset", "Curated 1,663 records across 8 mutually exclusive clinical departments."),
    ("TF-IDF Feature Engineering", "Engineered 8,000-dim unigram/bigram representation with sublinear scaling."),
    ("Imbalance Mitigation Applied", "Applied class_weight='balanced', SMOTE, and ROS to training folds."),
    ("Model & Ensemble Training", "Trained LR, SVM, RF, MNB, Hard Voting, and Soft Voting ensembles."),
    ("Comprehensive Evaluation", "Produced comparative metrics, confusion matrix, and classification reports."),
    ("Model Serialization", "Saved vectorizer (0.30 MB), SVM (0.49 MB), and Ensemble (11.07 MB)."),
    ("Repository Hygiene", "Resolved GitHub file-size limits via .gitignore configuration.")
]
for title, desc in comp_phase2:
    p_b = tf_s15_l.add_paragraph()
    p_b.text = f"✓ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(9)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(3)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Right: Planned for Phase 3
add_card(s15, Inches(6.8), Inches(1.5), Inches(5.93), Inches(5.3))
t_s15_r = s15.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.43), Inches(4.9))
tf_s15_r = t_s15_r.text_frame
tf_s15_r.word_wrap = True

p = tf_s15_r.paragraphs[0]
p.text = "Planned for Phase 3 (Deployment & Testing)"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = ACCENT_BLUE

plan_phase3 = [
    ("Finalize Deployment Pipeline", "Construct automated ingestion, preprocessing, and vector transformation pipeline for live clinical text."),
    ("Flask REST API Integration", "Build lightweight Python Flask web endpoints (/predict, /health) to serve model predictions."),
    ("Clinician Text Input Interface", "Develop an intuitive web interface for clinicians to paste operative dictations and inspect results."),
    ("Serialized Model Testing in App", "Verify real-time latency (< 15 ms) and validate predictions directly through the web application."),
    ("Final System Usability Review", "Benchmark end-to-end reliability, edge cases, and confidence threshold warnings (< 0.65)."),
    ("Final Defense & Documentation", "Complete MCA project report, user manual, and project defense documentation.")
]
for title, desc in plan_phase3:
    p_b = tf_s15_r.add_paragraph()
    p_b.text = f"→ {title}:\n"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_BLUE
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 16: Conclusion & Academic Acknowledgements (Dark Theme)
# ==============================================================================
s16 = prs.slides.add_slide(blank_layout)
set_slide_background(s16, DARK_BG)

t16 = s16.shapes.add_textbox(Inches(0.9), Inches(0.50), Inches(11.53), Inches(0.40))
tf16 = t16.text_frame
p16 = tf16.paragraphs[0]
p16.text = "MAR ATHANASIUS COLLEGE OF ENGINEERING, KOTHAMANGALAM"
p16.font.name = FONT_BODY
p16.font.size = Pt(13)
p16.font.bold = True
p16.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

pill16 = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.05), Inches(4.8), Inches(0.42))
pill16.fill.solid()
pill16.fill.fore_color.rgb = TEAL_ACCENT
pill16.line.fill.background()
tf_p16 = pill16.text_frame
p_p16 = tf_p16.paragraphs[0]
p_p16.text = "MCA MINI PROJECT  |  CONCLUSION & Q&A"
p_p16.alignment = PP_ALIGN.CENTER
p_p16.font.name = FONT_BODY
p_p16.font.size = Pt(12)
p_p16.font.bold = True
p_p16.font.color.rgb = TEXT_WHITE

t_end_title = s16.shapes.add_textbox(Inches(0.9), Inches(1.65), Inches(11.53), Inches(0.8))
tf_et = t_end_title.text_frame
p_et = tf_et.paragraphs[0]
p_et.text = "Conclusion: Phase 2 Progression & Outcome"
p_et.font.name = FONT_TITLE
p_et.font.size = Pt(26)
p_et.font.bold = True
p_et.font.color.rgb = TEXT_WHITE

c_sum = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(2.55), Inches(11.53), Inches(2.75))
c_sum.fill.solid()
c_sum.fill.fore_color.rgb = DARK_CARD
c_sum.line.color.rgb = DARK_TAG
tf_cs = c_sum.text_frame
tf_cs.margin_left = Inches(0.4)
tf_cs.margin_top = Inches(0.25)

p_cs = tf_cs.paragraphs[0]
p_cs.text = "Authoritative Summary Statement"
p_cs.font.name = FONT_TITLE
p_cs.font.size = Pt(15)
p_cs.font.bold = True
p_cs.font.color.rgb = TEAL_ACCENT

p_quote = tf_cs.add_paragraph()
p_quote.text = '"Phase 1 established the dataset characteristics and class imbalance through EDA. Phase 2 converted these findings into a complete machine-learning pipeline, beginning with a 40-class baseline and progressing through dataset refinement, imbalance mitigation, model training and ensemble evaluation. The final 8-specialty formulation achieved up to 88.59% accuracy with Linear SVM."'
p_quote.font.name = FONT_BODY
p_quote.font.size = Pt(12)
p_quote.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8)
p_quote.space_before = Pt(8)

p_pts = tf_cs.add_paragraph()
p_pts.text = "Key Takeaways: 8 Mutually Exclusive Specialties  •  8,000 TF-IDF Features  •  Class Imbalance Mitigation  •  88.59% SVM Accuracy  •  87.99% Soft Voting  •  Exceeded 75% Target"
p_pts.font.name = FONT_BODY
p_pts.font.size = Pt(10.5)
p_pts.font.bold = True
p_pts.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)
p_pts.space_before = Pt(12)

c_ty = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(5.5), Inches(11.53), Inches(1.4))
c_ty.fill.solid()
c_ty.fill.fore_color.rgb = TEAL_ACCENT
c_ty.line.fill.background()
tf_ty = c_ty.text_frame
tf_ty.margin_left = Inches(0.4)
tf_ty.margin_top = Inches(0.18)

p_ty1 = tf_ty.paragraphs[0]
p_ty1.text = "THANK YOU!"
p_ty1.font.name = FONT_TITLE
p_ty1.font.size = Pt(22)
p_ty1.font.bold = True
p_ty1.font.color.rgb = TEXT_WHITE
p_ty1.alignment = PP_ALIGN.CENTER

p_ty2 = tf_ty.add_paragraph()
p_ty2.text = "Open for Questions, Faculty Suggestions & Discussion\nPresented by: Jiphin George (MAC25MCA-2033) | Guide: Prof. Biju Skaria | Department of Computer Applications"
p_ty2.font.name = FONT_BODY
p_ty2.font.size = Pt(11)
p_ty2.font.color.rgb = RGBColor(0xF0, 0xFD, 0xFA)
p_ty2.alignment = PP_ALIGN.CENTER
p_ty2.space_before = Pt(3)

# Save output presentation
output_dir = r'D:\Antigravity Projects\Mini Project S3 MCA\model training project\2nd Presentation 30-9-2026'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'Medical_Specialty_Classification_Interim_Presentation_2.pptx')
prs.save(output_path)
print(f"Presentation successfully created at: {output_path}")
print(f"Total slides generated: {len(prs.slides)}")
