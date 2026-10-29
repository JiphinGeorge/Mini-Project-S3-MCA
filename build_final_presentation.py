import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# ==============================================================================
# PREMIUM HEALTHCARE & AI PALETTE
# ==============================================================================
# Dark Theme Palettes (Deep Obsidian / Midnight Navy)
DARK_BG = RGBColor(0x07, 0x11, 0x22)          # Deepest Luxury Midnight
DARK_CARD = RGBColor(0x0E, 0x1E, 0x38)        # Elevated Dark Card Fill
DARK_CARD_BORDER = RGBColor(0x1B, 0x35, 0x5D) # Subtle Glowing Border
DARK_TAG = RGBColor(0x14, 0x2E, 0x52)         # Tag Pill Background

# Light Theme Palettes (Clinical Slate / Crisp White)
LIGHT_BG = RGBColor(0xF3, 0xF6, 0xFA)         # Ultra-Clean Slate-White Canvas
CARD_BG = RGBColor(0xFF, 0xFF, 0xFF)          # Pure Crisp White Card
CARD_BORDER = RGBColor(0xD8, 0xE2, 0xEE)      # Crisp Polished Border
LIGHT_BLUE_BG = RGBColor(0xEA, 0xF1, 0xF8)    # Alternating Row Tint
LIGHT_GREEN_BG = RGBColor(0xDC, 0xFC, 0xE7)   # Success Soft Tint
LIGHT_AMBER_BG = RGBColor(0xFE, 0xF3, 0xC7)   # Highlight Soft Tint

# Vibrant Accent Tokens
TEAL_ACCENT = RGBColor(0x0D, 0x94, 0x88)      # Signature Clinical Teal
CYAN_ACCENT = RGBColor(0x06, 0xB6, 0xD4)      # Tech Cyan
BLUE_ACCENT = RGBColor(0x25, 0x63, 0xEB)      # Royal Sapphire Blue
INDIGO_ACCENT = RGBColor(0x4F, 0x46, 0xE5)    # Deep Modern Indigo
EMERALD_ACCENT = RGBColor(0x10, 0xB9, 0x81)   # Success Emerald
AMBER_ACCENT = RGBColor(0xD9, 0x77, 0x06)     # Safety Warning Amber
ROSE_ACCENT = RGBColor(0xE1, 0x1D, 0x48)      # Clinical Alert Rose / Red

# Typography Colors
NAVY_TITLE = RGBColor(0x0A, 0x1A, 0x30)       # High-Contrast Deep Navy
TEXT_DARK = RGBColor(0x1E, 0x29, 0x3B)        # Slate Dark Text
TEXT_MUTED = RGBColor(0x64, 0x74, 0x8B)       # Slate Muted Gray
TEXT_WHITE = RGBColor(0xFF, 0xFF, 0xFF)       # Pure White
TEXT_SKY = RGBColor(0x38, 0xBD, 0xF8)         # Glowing Sky Blue for Dark Theme

FONT_TITLE = 'Cambria'
FONT_BODY = 'Calibri'

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Image Asset Paths
img_ui_prediction = r'D:\Antigravity Projects\Mini Project S3 MCA\Final Report Latex Code\images\ui_prediction.png'
img_ui_how_it_works = r'D:\Antigravity Projects\Mini Project S3 MCA\Final Report Latex Code\images\ui_how_it_works.png'
img_ui_performance = r'D:\Antigravity Projects\Mini Project S3 MCA\Final Report Latex Code\images\ui_performance.png'
img_ui_features = r'D:\Antigravity Projects\Mini Project S3 MCA\Final Report Latex Code\images\ui_features.png'
img_mace_logo = r'D:\Antigravity Projects\Mini Project S3 MCA\Final Report Latex Code\images\mace_logo.png'
img_perf = r'D:\Antigravity Projects\Mini Project S3 MCA\model training project\model_performance_comparison.png'
img_cm = r'D:\Antigravity Projects\Mini Project S3 MCA\model training project\best_model_confusion_matrix.png'

TOTAL_SLIDES = 20

def set_slide_background(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_slide_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text

def add_header(slide, pill_text, title_text, slide_num, is_dark=False, total_slides=TOTAL_SLIDES):
    # Category Pill
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.32), Inches(4.8), Inches(0.34))
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
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    
    # Title Text
    t_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.68), Inches(12.13), Inches(0.65))
    tf2 = t_box.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = tf2.margin_bottom = 0
    p2 = tf2.paragraphs[0]
    p2.text = title_text
    p2.font.name = FONT_TITLE
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE if is_dark else NAVY_TITLE

    # Bottom Separator
    sep = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(7.05), Inches(12.13), Inches(0.015))
    sep.fill.solid()
    sep.fill.fore_color.rgb = DARK_CARD_BORDER if is_dark else CARD_BORDER
    sep.line.fill.background()

    # Footer Left
    f_left = slide.shapes.add_textbox(Inches(0.6), Inches(7.10), Inches(4.5), Inches(0.3))
    tf_l = f_left.text_frame
    tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = tf_l.margin_bottom = 0
    pl = tf_l.paragraphs[0]
    pl.text = "Department of Computer Applications | MACE (Autonomous)"
    pl.font.name = FONT_BODY
    pl.font.size = Pt(9.5)
    pl.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8) if is_dark else TEXT_MUTED

    # Footer Center
    f_center = slide.shapes.add_textbox(Inches(4.5), Inches(7.10), Inches(5.0), Inches(0.3))
    tf_c = f_center.text_frame
    tf_c.margin_left = tf_c.margin_right = tf_c.margin_top = tf_c.margin_bottom = 0
    pc = tf_c.paragraphs[0]
    pc.alignment = PP_ALIGN.CENTER
    pc.text = "Medical Specialty Classification | Final Defense | 29-10-2026"
    pc.font.name = FONT_BODY
    pc.font.size = Pt(9.5)
    pc.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8) if is_dark else TEXT_MUTED

    # Footer Right
    f_right = slide.shapes.add_textbox(Inches(10.0), Inches(7.10), Inches(2.73), Inches(0.3))
    tf_r = f_right.text_frame
    tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = tf_r.margin_bottom = 0
    pr = tf_r.paragraphs[0]
    pr.alignment = PP_ALIGN.RIGHT
    pr.text = f"Slide {slide_num} of {total_slides}"
    pr.font.name = FONT_BODY
    pr.font.size = Pt(9.5)
    pr.font.bold = True
    pr.font.color.rgb = TEXT_SKY if is_dark else NAVY_TITLE

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER, top_accent=None):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
    else:
        card.line.fill.background()
    
    # Optional Top Accent Stripe for Modern Dashboard Look
    if top_accent:
        stripe = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.02), top + Inches(0.02), width - Inches(0.04), Inches(0.06))
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = top_accent
        stripe.line.fill.background()
        
    return card

# Layout Presets
COL2_L = Inches(0.60)
COL2_W = Inches(5.90)
COL2_R = Inches(6.80)
COL2_RW = Inches(5.93)

COL3_W = Inches(3.80)
COL3_GAP = Inches(0.36)
COL3_LEFT = Inches(0.60)
def get_col3_left(idx):
    return COL3_LEFT + idx * (COL3_W + COL3_GAP)

print("Starting themed slide generation...")

# ==============================================================================
# SLIDE 1: Title Slide (Dark Luxury Navy Theme)
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, DARK_BG)

t1 = s1.shapes.add_textbox(Inches(0.9), Inches(0.40), Inches(11.53), Inches(0.35))
tf1 = t1.text_frame
p1 = tf1.paragraphs[0]
p1.text = "MAR ATHANASIUS COLLEGE OF ENGINEERING, KOTHAMANGALAM"
p1.font.name = FONT_BODY
p1.font.size = Pt(13)
p1.font.bold = True
p1.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

p1_sub = tf1.add_paragraph()
p1_sub.text = "(A Government Aided Autonomous Institution Affiliated to APJ Abdul Kalam Technological University)"
p1_sub.font.name = FONT_BODY
p1_sub.font.size = Pt(10)
p1_sub.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

pill1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.10), Inches(5.8), Inches(0.40))
pill1.fill.solid()
pill1.fill.fore_color.rgb = TEAL_ACCENT
pill1.line.fill.background()
tf_p1 = pill1.text_frame
p_p1 = tf_p1.paragraphs[0]
p_p1.text = "MCA MINI PROJECT  |  FINAL PROJECT DEFENSE  |  29-10-2026"
p_p1.alignment = PP_ALIGN.CENTER
p_p1.font.name = FONT_BODY
p_p1.font.size = Pt(11)
p_p1.font.bold = True
p_p1.font.color.rgb = TEXT_WHITE

t_title = s1.shapes.add_textbox(Inches(0.9), Inches(1.65), Inches(11.53), Inches(1.65))
tf_title = t_title.text_frame
tf_title.word_wrap = True
p_title = tf_title.paragraphs[0]
p_title.text = "Medical Specialty Classification Using TF-IDF and Ensemble Machine Learning"
p_title.font.name = FONT_TITLE
p_title.font.size = Pt(30)
p_title.font.bold = True
p_title.font.color.rgb = TEXT_WHITE

p_sub = tf_title.add_paragraph()
p_sub.text = "End-to-End Clinical NLP Pipeline, Soft Voting Ensemble & Deployed Decision-Support Platform"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(16)
p_sub.font.color.rgb = TEXT_SKY
p_sub.space_before = Pt(6)

c_pres = add_card(s1, Inches(0.9), Inches(3.55), Inches(5.6), Inches(2.45), bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=TEAL_ACCENT)
tf_pr = c_pres.text_frame
tf_pr.margin_left = Inches(0.35)
tf_pr.margin_top = Inches(0.24)
p_pr_h = tf_pr.paragraphs[0]
p_pr_h.text = "CANDIDATE INFORMATION"
p_pr_h.font.name = FONT_BODY
p_pr_h.font.size = Pt(11)
p_pr_h.font.bold = True
p_pr_h.font.color.rgb = TEAL_ACCENT

p_name = tf_pr.add_paragraph()
p_name.text = "Jiphin George"
p_name.font.name = FONT_TITLE
p_name.font.size = Pt(21)
p_name.font.bold = True
p_name.font.color.rgb = TEXT_WHITE
p_name.space_before = Pt(3)

p_reg = tf_pr.add_paragraph()
p_reg.text = "Register No: MAC25MCA-2033\nCourse: Master of Computer Applications (MCA)\nDepartment of Computer Applications\nAcademic Year: 2025–2027"
p_reg.font.name = FONT_BODY
p_reg.font.size = Pt(11.5)
p_reg.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)
p_reg.space_before = Pt(4)

c_guide = add_card(s1, Inches(6.83), Inches(3.55), Inches(5.6), Inches(2.45), bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=BLUE_ACCENT)
tf_g = c_guide.text_frame
tf_g.margin_left = Inches(0.35)
tf_g.margin_top = Inches(0.24)
p_gh = tf_g.paragraphs[0]
p_gh.text = "FACULTY GUIDANCE & EVALUATION"
p_gh.font.name = FONT_BODY
p_gh.font.size = Pt(11)
p_gh.font.bold = True
p_gh.font.color.rgb = CYAN_ACCENT

p_gname = tf_g.add_paragraph()
p_gname.text = "Prof. Biju Skaria  (Faculty Guide)"
p_gname.font.name = FONT_TITLE
p_gname.font.size = Pt(17)
p_gname.font.bold = True
p_gname.font.color.rgb = TEXT_WHITE
p_gname.space_before = Pt(3)

p_gdept = tf_g.add_paragraph()
p_gdept.text = "Project Coordinator: Dr. Manu John\nHead of the Department: Dr. Sonia Abraham\nEvaluation: Internal Examiner Review\nFinal Presentation Date: 29-10-2026"
p_gdept.font.name = FONT_BODY
p_gdept.font.size = Pt(11.5)
p_gdept.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)
p_gdept.space_before = Pt(4)

tags = ["Sublinear TF-IDF", "8-Specialty Benchmark", "Soft Voting [2:2:1:1]", "Open-Set Gate (\u03c4=0.48)", "Deployed Web UI"]
tag_w = Inches(2.23)
for i, tag in enumerate(tags):
    tg = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9 + i * 2.35), Inches(6.25), tag_w, Inches(0.42))
    tg.fill.solid()
    tg.fill.fore_color.rgb = DARK_TAG
    tg.line.color.rgb = DARK_CARD_BORDER
    tg.line.width = Pt(1)
    tf_tag = tg.text_frame
    p_t = tf_tag.paragraphs[0]
    p_t.text = tag
    p_t.alignment = PP_ALIGN.CENTER
    p_t.font.name = FONT_BODY
    p_t.font.size = Pt(10)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_SKY

add_slide_notes(s1, """[EXPLANATION NOTES & TALKING POINTS]
Respected Faculty Guide Prof. Biju Skaria, respected Head of the Department Dr. Sonia Abraham, Project Coordinator Dr. Manu John, respected internal examiners, and dear faculty members, good morning.

I am Jiphin George, Register Number MAC25MCA-2033, third semester Master of Computer Applications. Today, 29th October 2026, I am honored to present my Final Project Defense titled: 'Medical Specialty Classification Using TF-IDF and Ensemble Machine Learning'.

In our interim review, we presented our preliminary data preparation, baseline failure diagnosis, and initial modeling. Today, I am presenting the complete, operationalized platform: covering our curated 8-specialty benchmark, our Soft Voting Ensemble achieving 88.59% SVM and 87.99% ensemble accuracy, our clinical open-set rejection gate for out-of-domain patient safety, and our deployed clinical web application (MedSpecialty AI) featuring in-memory PDF ingestion, transparent explainability keywords, multi-model consensus, and sub-10 millisecond CPU latency.

Key Technical Highlights to note:
1. Domain: Clinical Natural Language Processing & Automated Hospital Triage.
2. Machine Learning: Linear Support Vector Machine, Logistic Regression, Random Forest, Multinomial Naive Bayes, combined via a calibrated Soft Voting Ensemble [2:2:1:1].
3. Deployment: Flask 3.0 REST backend, PyMuPDF in-memory document parsing, and responsive HTML5/CSS3/JavaScript UI.
4. Patient Safety: Open-set confidence thresholding (tau = 0.48) intercepting out-of-scope clinical narratives.""")

print("Slide 1 (Dark Theme) generated.")

# ==============================================================================
# SLIDE 2: Executive Summary (Dark Luxury Navy Theme for Executive Impact)
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2, DARK_BG)
add_header(s2, "EXECUTIVE SUMMARY", "Project Overview & Core System Architecture", 2, is_dark=True)

card_w = Inches(3.80)
card_h = Inches(5.35)
top_pos = Inches(1.48)

# Col 1: Problem (Rose Accent)
c1 = add_card(s2, get_col3_left(0), top_pos, card_w, card_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=ROSE_ACCENT)
tf1 = c1.text_frame
tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.28)
p = tf1.paragraphs[0]
p.text = "1. CLINICAL PROBLEM"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = ROSE_ACCENT

p = tf1.add_paragraph()
p.text = "EHR Triage Bottleneck"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

b1 = [
    ("80%+ Unstructured Text", "Doctor dictations & clinical notes lack standard format"),
    ("18–36 Hr Latency", "Manual clerical routing causes severe diagnostic delay"),
    ("12–18% Misrouting", "High clerical error rate from cognitive fatigue"),
    ("Closed-World Pitfall", "Naive classifiers blindly force-fit out-of-scope notes")
]
for title_b, desc_b in b1:
    p = tf1.add_paragraph()
    p.space_before = Pt(12)
    run1 = p.add_run()
    run1.text = "\u25aa " + title_b + "\n"
    run1.font.bold = True
    run1.font.size = Pt(12)
    run1.font.color.rgb = TEXT_SKY
    run2 = p.add_run()
    run2.text = desc_b
    run2.font.size = Pt(10.5)
    run2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

# Col 2: Solution (Cyan Accent)
c2 = add_card(s2, get_col3_left(1), top_pos, card_w, card_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=CYAN_ACCENT)
tf2 = c2.text_frame
tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.28)
p = tf2.paragraphs[0]
p.text = "2. TECHNICAL SOLUTION"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = CYAN_ACCENT

p = tf2.add_paragraph()
p.text = "MedSpecialty AI Pipeline"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

b2 = [
    ("Curated 8-Class Benchmark", "1,663 records resolving administrative ambiguity"),
    ("Sublinear TF-IDF (8k terms)", "Logarithmic scaling w = 1 + log(TF) & bi-grams"),
    ("Soft Voting Ensemble", "Weights [2:2:1:1] combining SVM, LR, RF, & MNB"),
    ("Open-Set Rejection (\u03c4 = 0.48)", "Safety gate routing uncertain notes to human review")
]
for title_b, desc_b in b2:
    p = tf2.add_paragraph()
    p.space_before = Pt(12)
    run1 = p.add_run()
    run1.text = "\u25aa " + title_b + "\n"
    run1.font.bold = True
    run1.font.size = Pt(12)
    run1.font.color.rgb = CYAN_ACCENT
    run2 = p.add_run()
    run2.text = desc_b
    run2.font.size = Pt(10.5)
    run2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

# Col 3: Deliverables (Emerald Accent)
c3 = add_card(s2, get_col3_left(2), top_pos, card_w, card_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=EMERALD_ACCENT)
tf3 = c3.text_frame
tf3.margin_left = tf3.margin_right = tf3.margin_top = Inches(0.28)
p = tf3.paragraphs[0]
p.text = "3. SYSTEM DELIVERABLES"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = EMERALD_ACCENT

p = tf3.add_paragraph()
p.text = "Production Web Platform"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

b3 = [
    ("88.59% Peak Accuracy", "SVM 88.59% (0.8971 F1); Ensemble 87.99% (0.8898 F1)"),
    ("9.20 ms Turnaround", "Sub-10ms CPU latency (>100 TPS without GPU)"),
    ("In-Memory PDF Extraction", "PyMuPDF parsing in 3.85ms with zero disk caching"),
    ("Interactive 4-Screen UI", "Flask web dashboard with clinical explainability")
]
for title_b, desc_b in b3:
    p = tf3.add_paragraph()
    p.space_before = Pt(12)
    run1 = p.add_run()
    run1.text = "\u25aa " + title_b + "\n"
    run1.font.bold = True
    run1.font.size = Pt(12)
    run1.font.color.rgb = EMERALD_ACCENT
    run2 = p.add_run()
    run2.text = desc_b
    run2.font.size = Pt(10.5)
    run2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

add_slide_notes(s2, """[EXPLANATION NOTES & TALKING POINTS]
This slide summarizes the entire project trajectory in three logical pillars: Problem, Solution, and Deliverables.

1. The Clinical Problem:
Over 80% of Electronic Health Record (EHR) data is completely unstructured free-text (physician dictations, operative reports, discharge summaries). Because these documents lack standard formatting, hospitals rely on clerical staff to manually read and route them. During busy periods, this introduces severe delays between 18 and 36 hours. Furthermore, clerical error rates average 12% to 18%, leading to misdirected patient referrals and appointment backlogs. Naive AI systems worsen this because they force-fit any document into an arbitrary class.

2. Our Engineered Solution:
We developed MedSpecialty AI. We solved dataset contamination by curating 1,663 records across 8 distinct hospital departments. We built an 8,000-dimensional sublinear TF-IDF pipeline using logarithmic term scaling and bigram phrases. To eliminate individual model weaknesses, we pooled four diverse classifiers into a calibrated Soft Voting Ensemble [2:2:1:1]. Finally, we implemented an Open-Set Confidence Rejection Gate (tau = 0.48) to safeguard patient care against out-of-scope notes.

3. Complete Deliverables:
The project delivered concrete software artifacts: Linear SVM achieved 88.59% accuracy and 0.8971 Macro F1; the Soft Voting Ensemble achieved 87.99% accuracy and 0.8898 Macro F1. The system executes in under 10 milliseconds on commodity CPU hardware, parses clinical PDFs in-memory in 3.85 ms, and is fully deployed as a responsive web service.""")

print("Slide 2 (Dark Executive Theme) generated.")

# ==============================================================================
# SLIDE 3: Clinical Motivation & Problem Statement (Clinical Slate Theme)
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, LIGHT_BG)
add_header(s3, "PROBLEM DEFINITION & OBJECTIVES", "Clinical Motivation & Formal Research Objectives", 3)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s3, COL2_L, top_pos, COL2_W, col_h, top_accent=ROSE_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "THE CLINICAL INTAKE CRISIS"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = ROSE_ACCENT

p = tf_l.add_paragraph()
p.text = "Hospital Triage Deficiencies"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

left_items = [
    ("Unstandardized Narrative Text", "Physicians use varying acronyms, abbreviations, and sentence styles."),
    ("Triage Latency (18–36 Hours)", "Clerical reading creates serious diagnostic and referral backlogs."),
    ("Inter-Annotator Disagreement (12–18%)", "Clerical staff often misinterpret overlapping neuro-orthopedic cases."),
    ("Closed-World Pitfall of Naive AI", "Standard ML force-fits dermatology or non-medical notes arbitrarily.")
]
for h, b in left_items:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

c_right = add_card(s3, COL2_R, top_pos, COL2_RW, col_h, top_accent=TEAL_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.28)
p = tf_r.paragraphs[0]
p.text = "PROJECT OBJECTIVES"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_r.add_paragraph()
p.text = "Formal Research Goals"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

right_items = [
    ("Curate 8-Class Benchmark", "Eliminate administrative formats; isolate 1,663 pure records."),
    ("Domain-Optimized TF-IDF NLP", "Engineer 8,000 sublinear unigram/bigram features ($L_2$ normalized)."),
    ("Calibrated Ensemble Benchmarking", "Combine SVM, LR, RF, and MNB to exceed 75.0% target accuracy."),
    ("Open-Set Clinical Safety Gate", "Formulate threshold $\tau = 0.48$ to reject out-of-domain documents."),
    ("Operational Web Deployment", "Deploy interactive Flask web application with sub-10ms CPU latency.")
]
for h, b in right_items:
    p = tf_r.add_paragraph()
    p.space_before = Pt(10)
    r1 = p.add_run()
    r1.text = "\u2714 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s3, """[EXPLANATION NOTES & TALKING POINTS]
Here we establish the concrete clinical motivations and the five formal research objectives of our study.

Clinical Bottlenecks:
1. When patients are referred to a multi-specialty hospital, consultation notes must be routed to departments like Cardiology, Orthopedics, Neurology, or Gastroenterology.
2. Clinical notes are complex: a single operative summary can contain abbreviations like 'CABG', 'L4-L5', or 'ERCP'.
3. Manual clerical triage takes 18 to 36 hours. More seriously, clerical workers disagree with one another in 12% to 18% of cases, especially when a patient has spinal symptoms that could be either neurological or orthopedic.
4. If a standard machine learning model is deployed, it suffers from the 'Closed-World Assumption': it blindly forces every incoming note into one of its trained departments, even if the note belongs to Dermatology or Psychiatry.

Our Five Formal Objectives:
1. Benchmark Formulation: Construct a clean, mutually exclusive 8-specialty benchmark from MTSamples.
2. NLP Engineering: Build an 8,000-dimensional sublinear TF-IDF pipeline capturing diagnostic medical bi-grams.
3. Model Development: Train and calibrate four distinct classifiers and assemble a Soft Voting Ensemble exceeding the 75% accuracy threshold.
4. Clinical Safety: Implement an Open-Set Confidence Rejection Gate (tau = 0.48) to route ambiguous notes to human review.
5. System Deployment: Operationalize the pipeline into a responsive web dashboard with in-memory PDF extraction and sub-10ms CPU turnaround.""")

print("Slide 3 generated.")

# ==============================================================================
# SLIDE 4: Literature Review & Identified Research Gaps
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, LIGHT_BG)
add_header(s4, "LITERATURE REVIEW & RESEARCH GAP", "Comparison with Existing Approaches & Identified Gaps", 4)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s4, COL2_L, top_pos, COL2_W, col_h, top_accent=INDIGO_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "PARADIGM COMPARISON"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = INDIGO_ACCENT

p = tf_l.add_paragraph()
p.text = "Existing Approaches vs Ours"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

lit_items = [
    ("Rule-Based Regex Systems", "Brittle; fails on synonym variations; high manual maintenance."),
    ("Heavy Transformers (BioBERT)", "Accurate but requires 4–8GB GPU VRAM, >150ms latency, black-box."),
    ("Standard Bag-of-Words ML", "Suffers frequency explosion and unconstrained vocabulary collapse."),
    ("MedSpecialty AI (Proposed)", "Sublinear TF-IDF + Ensemble: <145MB RAM, <10ms CPU latency, 88.59% accuracy, explainable.")
]
for h, b in lit_items:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

c_right = add_card(s4, COL2_R, top_pos, COL2_RW, col_h, top_accent=AMBER_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.28)
p = tf_r.paragraphs[0]
p.text = "IDENTIFIED RESEARCH GAPS"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = AMBER_ACCENT

p = tf_r.add_paragraph()
p.text = "Limitations in Prior Work"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

gaps = [
    ("Neglect of Open-World Safety", "Existing models lack confidence rejection for out-of-scope notes."),
    ("GPU Dependency Barrier", "Deep learning models cannot execute on standard hospital workstations."),
    ("Benchmark Contamination", "Public datasets include administrative formats as clinical classes."),
    ("Absence of Clinician UI", "Prior academic works end at scripts without interactive web interfaces.")
]
for h, b in gaps:
    p = tf_r.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u26a0 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s4, """[EXPLANATION NOTES & TALKING POINTS]
Reviewing the state-of-the-art in medical text classification reveals clear trade-offs across existing paradigms:

1. Rule-Based Systems:
Historically, hospitals built keyword lookups and regex tables. These collapse whenever a clinician writes 'myocardial infarction' instead of 'heart attack', requiring constant rule updates.

2. Deep Transformer Architectures (BioBERT, ClinicalBERT):
Recent research papers apply large pretrained transformers. While they achieve high accuracy, they suffer from three fatal operational bottlenecks:
- Hardware Burden: Require dedicated GPUs with 4 to 8 GB of VRAM.
- High Latency: Average inference latency exceeds 150 milliseconds per note.
- Opacity: They function as black boxes without simple explainability tokens.

3. Four Identified Research Gaps:
- Gap 1: Existing classifiers ignore open-world safety. When fed out-of-domain notes, they blindly force-fit predictions.
- Gap 2: Prohibitive compute costs prevent edge deployment in regional clinics.
- Gap 3: Public benchmarks like MTSamples are frequently evaluated on raw 40 categories without recognizing that 'Surgery' is not a clinical department.
- Gap 4: Academic models lack usable clinician interfaces.

Our MedSpecialty AI platform bridges these gaps directly: sublinear TF-IDF paired with an ensemble delivers 88.59% accuracy, under 10ms CPU latency, open-set safety, and an interactive web dashboard.""")

print("Slide 4 generated.")

# ==============================================================================
# SLIDE 5: Raw Dataset Architecture & Exploratory Profiling
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, LIGHT_BG)
add_header(s5, "DATASET ARCHITECTURE & EXPLORATORY PROFILING", "The MTSamples Corpus: Architecture, Imbalance & Ambiguity", 5)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s5, COL2_L, top_pos, COL2_W, col_h, top_accent=TEAL_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "RAW DATASET CHARACTERISTICS"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_l.add_paragraph()
p.text = "MTSamples Corpus Overview"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

raw_props = [
    ("4,999 Raw Transcriptions", "Real-world hospital clinical records from diverse specialties."),
    ("40 Initial Categories", "Extreme mix of procedural, departmental, and administrative tags."),
    ("33 Null Transcriptions Dropped", "Cleaned to 4,966 records during Phase 1 exploratory audit."),
    ("High Length Variance", "Narratives range widely from 50 to 2,500 words per document.")
]
for h, b in raw_props:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

c_right = add_card(s5, COL2_R, top_pos, COL2_RW, col_h, top_accent=ROSE_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.28)
p = tf_r.paragraphs[0]
p.text = "EXPLORATORY DATA AUDIT"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = ROSE_ACCENT

p = tf_r.add_paragraph()
p.text = "Two Critical Failure Modes"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

eda_findings = [
    ("Severe Class Imbalance (180:1)", "Surgery had 1,088 notes; Hospice had <10 notes. Baseline collapsed."),
    ("Procedural Ambiguity", "'Surgery' is a document type! Heart surgery was tagged 'Surgery', not Cardiology."),
    ("Unconstrained RF Collapse (7.85%)", "310,298 unpruned features caused decision trees to overfit noise."),
    ("Cross-Departmental Contamination", "Generic surgical terms ('incision', 'tolerated') masked diagnostic tokens.")
]
for h, b in eda_findings:
    p = tf_r.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u26a0 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s5, """[EXPLANATION NOTES & TALKING POINTS]
Slide 5 covers our initial Exploratory Data Analysis on the MTSamples corpus.

Key Raw Dataset Characteristics:
- 4,999 clinical records across 40 classes.
- During our Phase 1 data audit, we discovered 33 records with missing transcription text and removed them, leaving 4,966 records.
- Text length varied dramatically, from brief 50-word clinic notes to 2,500-word surgical reports.

Two Critical Failure Modes in Raw Data:
1. Extreme Class Imbalance:
The 'Surgery' category held 1,088 notes (21.8%), whereas minority categories like Hospice had only 6 notes. When we trained a baseline Logistic Regression model directly on the raw 40 classes, it collapsed to 22.96% accuracy by predicting 'Surgery' for every single input.

2. Procedural vs Departmental Ambiguity:
Our clinical audit revealed a fundamental problem: categories like 'Surgery' (1,088 notes) and 'Consult - History and Phy.' (516 notes) are administrative document formats, not medical specialties. A coronary bypass was labeled 'Surgery' rather than 'Cardiovascular'; an endoscopy was labeled 'Surgery' rather than 'Gastroenterology'.

Furthermore, when an unconstrained Random Forest was trained on the raw data with 310,298 features, it collapsed to 7.85% accuracy because the trees split on low-frequency noise. This diagnostic proved that scientific dataset refinement was essential.""")

print("Slide 5 generated.")

# ==============================================================================
# SLIDE 6: Curated 8-Class Benchmark (1,663 Records)
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, LIGHT_BG)
add_header(s6, "DATASET REFINEMENT & BENCHMARK FORMULATION", "The Curated 8-Specialty Clinical Department Benchmark", 6)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s6, COL2_L, top_pos, COL2_W, col_h, top_accent=TEAL_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "REFINEMENT STRATEGY"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_l.add_paragraph()
p.text = "Scientific Benchmark Selection"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

steps = [
    ("Eliminated Administrative Tags", "Removed 'Surgery' & 'Consult' to eliminate multi-department contamination."),
    ("Pruned Sparse Micro-Classes", "Excluded categories with <50 records lacking statistical sample support."),
    ("Retained 8 Hospital Specialties", "Focused on distinct clinical domains: Cardiology, Ortho, Gastro, Neuro, etc."),
    ("Stratified 80/20 Partitioning", "1,330 Train / 333 Test preserving exact class proportions.")
]
for h, b in steps:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u2714 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

c_right = add_card(s6, COL2_R, top_pos, COL2_RW, col_h, top_accent=BLUE_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.25)
p = tf_r.paragraphs[0]
p.text = "8-SPECIALTY CLASS DISTRIBUTION"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_ACCENT

p = tf_r.add_paragraph()
p.text = "Benchmark Distribution (N = 1,663 Records)"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

table_shape = s6.shapes.add_table(9, 4, Inches(6.95), Inches(2.35), Inches(5.63), Inches(4.25))
table = table_shape.table
table.columns[0].width = Inches(2.65)
table.columns[1].width = Inches(0.95)
table.columns[2].width = Inches(0.95)
table.columns[3].width = Inches(1.08)

headers = ["Clinical Specialty", "Total", "Train (80%)", "Test (20%)"]
for col_idx, h_text in enumerate(headers):
    cell = table.cell(0, col_idx)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TITLE
    p = cell.text_frame.paragraphs[0]
    p.text = h_text
    p.font.name = FONT_BODY
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

dept_data = [
    ("Cardiovascular / Pulmonary", "371", "297", "74"),
    ("Orthopedic", "355", "284", "71"),
    ("Gastroenterology", "230", "185", "45"),
    ("Neurology", "223", "178", "45"),
    ("Urology", "156", "125", "31"),
    ("Obstetrics / Gynecology", "155", "124", "31"),
    ("ENT - Otolaryngology", "96", "77", "19"),
    ("Ophthalmology", "77", "60", "17"),
]

for row_idx, data in enumerate(dept_data, start=1):
    bg_col = CARD_BG if row_idx % 2 == 1 else LIGHT_BLUE_BG
    for col_idx, text in enumerate(data):
        cell = table.cell(row_idx, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg_col
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        p.font.color.rgb = TEXT_DARK
        p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT
        if col_idx == 0:
            p.font.bold = True

add_slide_notes(s6, """[EXPLANATION NOTES & TALKING POINTS]
Slide 6 presents our curated 8-specialty clinical benchmark.

Refinement Rationale:
1. Removing Administrative Tags:
We systematically dropped generic procedural categories like 'Surgery', 'Consult - History and Phy.', and 'Discharge Summary'. These represent document formats that cross-contaminate clinical specialties.
2. Pruning Sparse Micro-Classes:
We eliminated micro-classes with fewer than 50 records (such as Hospice or Chiropractic), which lacked statistical support for 5-fold cross-validation.
3. 8 Mutually Exclusive Specialties:
We retained eight primary hospital departments with distinct anatomical boundaries:
- Cardiovascular / Pulmonary (371 records)
- Orthopedic (355 records)
- Gastroenterology (230 records)
- Neurology (223 records)
- Urology (156 records)
- Obstetrics / Gynecology (155 records)
- ENT - Otolaryngology (96 records)
- Ophthalmology (77 records)

Partitioning Strategy:
We applied stratified 80/20 train/test holdout partitioning: exactly 1,330 training records and 333 unobserved test records. Stratification guarantees that the test partition preserves the exact proportional representation of each clinical department.""")

print("Slide 6 generated.")

# ==============================================================================
# SLIDE 7: Clinical NLP Preprocessing & Sublinear TF-IDF
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, LIGHT_BG)
add_header(s7, "NLP PREPROCESSING & FEATURE ENGINEERING", "Clinical NLP Normalization & Sublinear TF-IDF Vectorization", 7)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s7, COL2_L, top_pos, COL2_W, col_h, top_accent=TEAL_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "TEXT SANITIZATION PIPELINE"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_l.add_paragraph()
p.text = "4-Stage Text Cleaning"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

stages = [
    ("Stage 1: Regex Noise Stripping", "Applied [^a-zA-Z\\\\s] to strip numbers, symbols, and formatting artifacts."),
    ("Stage 2: Contraction Expansion", "Normalized clinical shorthand (e.g., didn\'t -> did not, pt\'s -> patient)."),
    ("Stage 3: Medical Stopword Filtering", "Customized NLTK stopwords; preserved vital anatomical markers ('bilateral', 'left')."),
    ("Stage 4: Morphological Lemmatization", "WordNet lemmatizer reduced inflected terms (stenosed -> stenosis) to root.")
]
for h, b in stages:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

c_right = add_card(s7, COL2_R, top_pos, COL2_RW, col_h, top_accent=BLUE_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.28)
p = tf_r.paragraphs[0]
p.text = "FEATURE VECTORIZATION"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_ACCENT

p = tf_r.add_paragraph()
p.text = "Sublinear TF-IDF Feature Space"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

tfidf_props = [
    ("Sublinear Term Frequency Scaling", "Logarithmic weighting w = 1 + log(TF) prevents term repetition dominance."),
    ("Smooth Inverse Document Frequency", "Downweights hospital-wide common words via log((1+N)/(1+DF)) + 1."),
    ("N-Gram Range: (1, 2)", "Captures critical clinical bigrams ('coronary artery', 'visual acuity')."),
    ("Vocabulary Cap: 8,000 Terms", "Pruned sparse lexical noise from 42,000 terms down to 8,000 features."),
    ("L2 Hypersphere Normalization", "Normalizes all document vectors to unit length (||x||_2 = 1).")
]
for h, b in tfidf_props:
    p = tf_r.add_paragraph()
    p.space_before = Pt(10)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s7, """[EXPLANATION NOTES & TALKING POINTS]
Slide 7 describes our Natural Language Processing and Feature Engineering pipeline.

Four-Stage Text Sanitization:
1. Regex Noise Removal: Removes punctuation, non-alphabetic symbols, and HTML/EHR formatting characters while preserving diagnostic terms.
2. Contraction Expansion: Normalizes colloquial contractions and clinical transcript abbreviations.
3. Medical Stopword Filtration: Standard stopword lists often remove words like 'left', 'right', 'under', or 'bilateral'. In medical text, these are critical anatomical directional markers (e.g., 'bilateral knee arthroplasty'). We curated the stopword list to preserve these vital anatomical tokens.
4. Morphological Lemmatization: WordNet lemmatization reduces inflections (e.g., 'stenosed', 'stenosing' -> 'stenosis') to their common lexical root.

Sublinear TF-IDF Formulation:
- Why Sublinear Scaling? In surgical reports, a doctor might mention the word 'catheter' 25 times. Standard TF-IDF multiplies this linearly by 25, distorting the document vector. Sublinear TF-IDF applies logarithmic scaling: w = 1 + log(TF) if TF > 0. This models diminishing returns for repeated mentions.
- N-Gram Range (1, 2): Extracts unigrams and bigrams, capturing essential multi-word medical terminology like 'myocardial infarction' or 'visual acuity'.
- 8,000-Feature Cap: Prunes typos, single-occurrence words, and lexical noise from 42,000 terms down to the top 8,000 most informative features.
- L2 Normalization: Normalizes all vectors to unit length, preventing longer operative notes from dominating shorter outpatient letters.""")

print("Slide 7 generated.")

# ==============================================================================
# SLIDE 8: Candidate Machine Learning Architectures
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, LIGHT_BG)
add_header(s8, "CANDIDATE MODEL ARCHITECTURES", "Four Complementary Supervised Learning Paradigms", 8)

card_w = Inches(5.90)
card_h = Inches(2.55)
top_r1 = Inches(1.48)
top_r2 = Inches(4.28)

# Model 1: Linear SVM (Teal Accent)
c_svm = add_card(s8, COL2_L, top_r1, card_w, card_h, top_accent=TEAL_ACCENT)
tf_svm = c_svm.text_frame
tf_svm.margin_left = tf_svm.margin_right = tf_svm.margin_top = Inches(0.24)
p = tf_svm.paragraphs[0]
p.text = "1. LINEAR SUPPORT VECTOR MACHINE (SVM)"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT
p = tf_svm.add_paragraph()
p.text = "Maximum-Margin Hyperplane with Platt Calibration"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
svm_b = [
    ("Mathematical Objective: ", "Maximizes geometric margin: min 1/2 ||w||^2 + C \u2211 \u03be_i"),
    ("Hyperparameters: ", "C = 1.0, squared hinge loss, L2 penalty, one-vs-rest multiclass"),
    ("Platt Calibration: ", "Sigmoid mapping transforms margin distances into posterior probabilities P(y|x)")
]
for h, b in svm_b:
    p = tf_svm.add_paragraph()
    p.space_before = Pt(4)
    r1 = p.add_run()
    r1.text = "\u25aa " + h
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

# Model 2: Logistic Regression (Blue Accent)
c_lr = add_card(s8, COL2_R, top_r1, card_w, card_h, top_accent=BLUE_ACCENT)
tf_lr = c_lr.text_frame
tf_lr.margin_left = tf_lr.margin_right = tf_lr.margin_top = Inches(0.24)
p = tf_lr.paragraphs[0]
p.text = "2. MULTINOMIAL LOGISTIC REGRESSION"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = BLUE_ACCENT
p = tf_lr.add_paragraph()
p.text = "Calibrated Softmax Probability Estimation"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
lr_b = [
    ("Mathematical Objective: ", "Minimizes multinomial cross-entropy loss across 8 classes via Softmax"),
    ("Hyperparameters: ", "C = 2.0, L2 regularization, L-BFGS quasi-Newton solver"),
    ("Key Strength: ", "Inherently well-calibrated posterior probabilities; robust to linear correlations")
]
for h, b in lr_b:
    p = tf_lr.add_paragraph()
    p.space_before = Pt(4)
    r1 = p.add_run()
    r1.text = "\u25aa " + h
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

# Model 3: Random Forest (Emerald Accent)
c_rf = add_card(s8, COL2_L, top_r2, card_w, card_h, top_accent=EMERALD_ACCENT)
tf_rf = c_rf.text_frame
tf_rf.margin_left = tf_rf.margin_right = tf_rf.margin_top = Inches(0.24)
p = tf_rf.paragraphs[0]
p.text = "3. RANDOM FOREST CLASSIFIER"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = EMERALD_ACCENT
p = tf_rf.add_paragraph()
p.text = "Constrained Non-Linear Ensemble of Decision Trees"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
rf_b = [
    ("Mathematical Objective: ", "Bootstrap bagging over 100 decision trees splitting on Gini impurity"),
    ("Hyperparameters: ", "n_estimators = 100, max_depth = 25, class_weight = 'balanced'"),
    ("Flaw Resolution: ", "Constraining depth to 25 stopped noise overfitting; accuracy jumped to 81.98%")
]
for h, b in rf_b:
    p = tf_rf.add_paragraph()
    p.space_before = Pt(4)
    r1 = p.add_run()
    r1.text = "\u25aa " + h
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

# Model 4: Multinomial Naive Bayes (Amber Accent)
c_mnb = add_card(s8, COL2_R, top_r2, card_w, card_h, top_accent=AMBER_ACCENT)
tf_mnb = c_mnb.text_frame
tf_mnb.margin_left = tf_mnb.margin_right = tf_mnb.margin_top = Inches(0.24)
p = tf_mnb.paragraphs[0]
p.text = "4. MULTINOMIAL NAIVE BAYES (MNB)"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = AMBER_ACCENT
p = tf_mnb.add_paragraph()
p.text = "Bayesian Prior-Likelihood Generative Model"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
mnb_b = [
    ("Mathematical Objective: ", "P(c|x) \u221d P(c) \u220f P(x_i|c) using conditional word probability vectors"),
    ("Hyperparameters: ", "Laplace smoothing parameter \u03b1 = 0.1, learned class prior frequencies"),
    ("Key Strength: ", "Instantaneous training (0.01s) and high precision (86.02%) on distinct vocabularies")
]
for h, b in mnb_b:
    p = tf_mnb.add_paragraph()
    p.space_before = Pt(4)
    r1 = p.add_run()
    r1.text = "\u25aa " + h
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s8, """[EXPLANATION NOTES & TALKING POINTS]
Slide 8 presents our four candidate supervised machine learning algorithms, spanning four fundamentally distinct learning paradigms:

1. Linear Support Vector Machine (Geometric / Maximum-Margin):
- Text categorization with 8,000 features is linearly separable. LinearSVM constructs maximum-margin separating hyperplanes between classes.
- Crucially, raw SVM decision functions produce uncalibrated signed distances (-inf to +inf). We applied Platt scaling via CalibratedClassifierCV, which fits a sigmoid function to transform distances into genuine posterior probabilities P(y|x).

2. Multinomial Logistic Regression (Probabilistic Discriminative):
- Minimizes multinomial cross-entropy loss using the Softmax function.
- Uses L-BFGS solver with L2 regularization (C = 2.0). Produces inherently well-calibrated posterior probabilities.

3. Random Forest (Non-Linear Ensemble Tree):
- In our initial baseline, unconstrained trees overfitted noise and collapsed to 7.85%.
- In Phase 2, we constrained max_depth to 25 and set class_weight to 'balanced'. This completely reversed the collapse, achieving 81.98% accuracy.

4. Multinomial Naive Bayes (Probabilistic Generative):
- Evaluates word conditional likelihoods with Laplace smoothing (alpha = 0.1).
- Near-zero execution time (0.01 seconds) and high precision (86.02%) on vocabulary-distinct categories like Ophthalmology and Urology.""")

print("Slide 8 generated.")

# ==============================================================================
# SLIDE 9: Calibrated Soft Voting Ensemble (Dark Luxury Navy Theme for Algorithmic Centerpiece)
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, DARK_BG)
add_header(s9, "ENSEMBLE CONSENSUS SCHEME", "Weighted Soft Voting Ensemble Architecture & Calibration", 9, is_dark=True)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s9, COL2_L, top_pos, COL2_W, col_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=TEAL_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "ENSEMBLE FORMULATION"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_l.add_paragraph()
p.text = "Mathematical Consensus Rule"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

ens_math = [
    ("Soft Probability Averaging", "P_ens(c|x) = \u2211 [w_m \u22c5 P_m(c|x)] / \u2211 w_m across all 4 estimators."),
    ("Empirical Weights: [2, 2, 1, 1]", "w_SVM = 2, w_LR = 2, w_RF = 1, w_MNB = 1 based on validation reliability."),
    ("Variance Reduction", "Condorcet's Jury Theorem: uncorrelated model errors cancel out."),
    ("Unified Posterior Simplex", "Outputs full 8-dimensional probability vector summing to 1.0.")
]
for h, b in ens_math:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = TEXT_SKY
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

c_right = add_card(s9, COL2_R, top_pos, COL2_RW, col_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=CYAN_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.28)
p = tf_r.paragraphs[0]
p.text = "SOFT VS HARD VOTING"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = CYAN_ACCENT

p = tf_r.add_paragraph()
p.text = "Why Soft Voting is Essential in Healthcare"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

ens_adv = [
    ("Preserves Confidence Magnitude", "Hard voting discards certainty; treats 99% confident vote like a 51% guess."),
    ("Resolves Split Votes Gracefully", "Eliminates arbitrary tie-breaking when estimators split 2-2."),
    ("Differential Candidate Ranking", "Surfaces top-3 secondary departments for clinical triage context."),
    ("Powers Clinical Safety Gate", "Peak ensemble probability directly feeds our Open-Set Rejection Gate (\u03c4 = 0.48).")
]
for h, b in ens_adv:
    p = tf_r.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u2714 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = CYAN_ACCENT
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

add_slide_notes(s9, """[EXPLANATION NOTES & TALKING POINTS]
Slide 9 explains our Weighted Soft Voting Ensemble consensus scheme.

Why Soft Voting Instead of Hard Voting?
- In Hard Voting, each model casts a single discrete class vote. A model that is 99% certain has the exact same voting weight as a model guessing at 51%. Furthermore, in a 4-model system, a 2-2 vote split requires arbitrary random tie-breaking.
- Soft Voting averages the calibrated continuous probability distributions output by each model: P_ens(c|x) = sum(w_m * P_m) / sum(w_m).

Weighting Rationale [2:2:1:1]:
- Linear SVM and Logistic Regression achieved ~88% cross-validation accuracy due to optimal linear separation in TF-IDF space; they are assigned weight 2.
- Random Forest and Naive Bayes achieved ~81% and 77% accuracy; they are assigned weight 1 to inject non-linear tree diversity and Bayesian prior regularization without dragging down linear precision.

Two Critical Clinical Benefits:
1. Differential Diagnostics: Clinicians are shown the top-3 ranked candidate specialties (e.g., Cardiology: 94%, Gastro: 3%, Ortho: 1%), which mirrors real-world medical differential diagnosis.
2. Foundation for Safety: The peak probability max P_ens directly feeds our Open-Set Rejection Gate to intercept uncertain predictions.""")

print("Slide 9 (Dark Algorithmic Theme) generated.")

# ==============================================================================
# SLIDE 10: Model Performance Comparison & Benchmark Analysis
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, LIGHT_BG)
add_header(s10, "EMPIRICAL BENCHMARK RESULTS", "Model Performance Comparison against 75.0% Target Threshold", 10)

card_chart = add_card(s10, COL2_L, Inches(1.48), Inches(5.90), Inches(5.35), top_accent=TEAL_ACCENT)
tf_ch = card_chart.text_frame
tf_ch.margin_left = tf_ch.margin_right = tf_ch.margin_top = Inches(0.20)
p = tf_ch.paragraphs[0]
p.text = "BENCHMARK PERFORMANCE CHART"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

if os.path.exists(img_perf):
    s10.shapes.add_picture(img_perf, Inches(0.80), Inches(2.05), Inches(5.50), Inches(4.55))

c_rt = add_card(s10, COL2_R, Inches(1.48), Inches(5.93), Inches(5.35), top_accent=BLUE_ACCENT)
tf_rt = c_rt.text_frame
tf_rt.margin_left = tf_rt.margin_right = tf_rt.margin_top = Inches(0.24)
p = tf_rt.paragraphs[0]
p.text = "QUANTITATIVE EVALUATION (N = 333 TEST SAMPLES)"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = BLUE_ACCENT

p = tf_rt.add_paragraph()
p.text = "Comparative Evaluation Metrics"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(3)

t_shape = s10.shapes.add_table(7, 5, Inches(6.95), Inches(2.25), Inches(5.63), Inches(2.70))
t = t_shape.table
t.columns[0].width = Inches(2.23)
t.columns[1].width = Inches(0.85)
t.columns[2].width = Inches(0.85)
t.columns[3].width = Inches(0.85)
t.columns[4].width = Inches(0.85)

cols = ["Model Architecture", "Accuracy", "Macro F1", "Weighted F1", "Train (s)"]
for ci, col_name in enumerate(cols):
    cell = t.cell(0, ci)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TITLE
    p = cell.text_frame.paragraphs[0]
    p.text = col_name
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.CENTER if ci > 0 else PP_ALIGN.LEFT

perf_rows = [
    ("Linear SVM (Calibrated)", "88.59%", "0.8971", "0.8862", "0.12 s"),
    ("Soft Voting Ensemble", "87.99%", "0.8898", "0.8818", "2.49 s"),
    ("Logistic Regression", "87.09%", "0.8846", "0.8730", "0.37 s"),
    ("Hard Voting Ensemble", "87.09%", "0.8846", "0.8730", "2.01 s"),
    ("Random Forest (d=25)", "81.98%", "0.8274", "0.8209", "1.54 s"),
    ("Multinomial NB", "77.48%", "0.7743", "0.7824", "0.01 s"),
]

for ri, row_data in enumerate(perf_rows, start=1):
    bg_col = RGBColor(0xFE, 0xF3, 0xC7) if ri == 1 else (CARD_BG if ri % 2 == 1 else LIGHT_BLUE_BG)
    for ci, val in enumerate(row_data):
        cell = t.cell(ri, ci)
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg_col
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_BODY
        p.font.size = Pt(9)
        p.font.color.rgb = TEXT_DARK
        p.alignment = PP_ALIGN.CENTER if ci > 0 else PP_ALIGN.LEFT
        if ri in (1, 2) or ci == 0:
            p.font.bold = True

t_under = s10.shapes.add_textbox(Inches(6.95), Inches(5.15), Inches(5.63), Inches(1.55))
tf_u = t_under.text_frame
tf_u.margin_left = tf_u.margin_right = tf_u.margin_top = 0
tf_u.word_wrap = True
takeaways = [
    ("Exceeded 75.0% Requirement", "All models exceeded threshold; SVM achieved 88.59% accuracy & 0.8971 Macro F1."),
    ("Ensemble Probability Pooling", "Soft Voting achieved 87.99% accuracy & 90.41% precision with calibrated probabilities."),
    ("Sub-3 Second Total Training", "All models train in under 3 seconds on standard CPU hardware.")
]
for h, b in takeaways:
    p = tf_u.add_paragraph()
    p.space_before = Pt(5)
    r1 = p.add_run()
    r1.text = "\u2714 " + h + ": "
    r1.font.bold = True
    r1.font.size = Pt(10.5)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s10, """[EXPLANATION NOTES & TALKING POINTS]
Slide 10 presents our comprehensive empirical benchmarking on the 333 unobserved test records.

Key Quantitative Findings:
1. Every Single Model Exceeded 75.0% Project Target:
- Linear SVM achieved the highest individual classification accuracy: 88.59%, with a Macro F1 of 0.8971, training in only 0.12 seconds.
- Soft Voting Ensemble delivered the most robust, balanced performance: 87.99% accuracy, 90.41% macro precision, and 0.8898 Macro F1.
- Logistic Regression followed closely with 87.09% accuracy and 0.8846 Macro F1.
- Random Forest achieved 81.98% accuracy, completely recovering from its initial 7.85% unconstrained failure.
- Multinomial Naive Bayes scored 77.48% accuracy with near-instantaneous 0.01-second training.

2. Macro F1 vs Weighted F1 Consistency:
In imbalanced classification, models often exhibit high weighted F1 but low macro F1 because they fail on minority classes. Here, Macro F1 (0.8971) and Weighted F1 (0.8862) are virtually identical. This mathematically proves that our pipeline achieves high clinical precision across both large classes (Cardiology) and smaller classes (Ophthalmology).

3. Speed and Efficiency:
The entire training phase across all estimators finishes in under 3 seconds total on CPU.""")

print("Slide 10 generated.")

# ==============================================================================
# SLIDE 11: Confusion Matrix & Classification Diagnostics
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11, LIGHT_BG)
add_header(s11, "ERROR DIAGNOSTICS & CONFUSION MATRIX", "Confusion Matrix Analysis & Clinical Decision Boundaries", 11)

card_cm = add_card(s11, COL2_L, Inches(1.48), Inches(5.90), Inches(5.35), top_accent=TEAL_ACCENT)
tf_cm = card_cm.text_frame
tf_cm.margin_left = tf_cm.margin_right = tf_cm.margin_top = Inches(0.20)
p = tf_cm.paragraphs[0]
p.text = "SOFT VOTING CONFUSION MATRIX (8x8)"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

if os.path.exists(img_cm):
    s11.shapes.add_picture(img_cm, Inches(0.85), Inches(1.95), Inches(5.40), Inches(4.70))

c_cm_rt = add_card(s11, COL2_R, Inches(1.48), Inches(5.93), Inches(5.35), top_accent=ROSE_ACCENT)
tf_crt = c_cm_rt.text_frame
tf_crt.margin_left = tf_crt.margin_right = tf_crt.margin_top = Inches(0.28)
p = tf_crt.paragraphs[0]
p.text = "CLINICAL ERROR PATTERNS"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = ROSE_ACCENT

p = tf_crt.add_paragraph()
p.text = "Diagnostic Boundary Inspection"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

cm_insights = [
    ("Intense Diagonal Dominance", "295 / 333 True Positives (88.6%) showing clean specialty separation."),
    ("Flawless Ophthalmology", "17 / 17 correct (100% precision & recall) due to unique eye surgery vocabulary."),
    ("Neurology vs Orthopedic Boundary", "6 of 10 false negatives in Neurology were predicted as Orthopedic (shared spine terms)."),
    ("Urology & OB/GYN Specificity", "Urology scored 97% precision (1 FP); OB/GYN achieved 93% precision across 31 cases.")
]
for h, b in cm_insights:
    p = tf_crt.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s11, """[EXPLANATION NOTES & TALKING POINTS]
Slide 11 examines the 8x8 Confusion Matrix of our Soft Voting Ensemble on the unobserved 333 test samples.

Key Diagnostic Observations:
1. Pronounced Diagonal Dominance:
Out of 333 test cases, 295 fall squarely on the main diagonal (True Positives). The off-diagonal dispersion is minimal.

2. Ophthalmology Perfection:
17 out of 17 test cases were classified with 100% precision and 100% recall. Eye surgery terminology (phacoemulsification, cataract, intraocular lens) forms an isolated cluster in TF-IDF space with zero cross-talk.

3. The Neurology vs Orthopedic Boundary Overlap:
Examining the errors reveals that 6 out of 10 false negatives in Neurology were predicted as Orthopedic. When we audited these specific dictations, we found procedures like lumbar laminectomy, cervical spine decompression, and disc herniation.
In medicine, spine surgery is shared between orthopedic surgeons and neurosurgeons. Both dictate words like 'vertebrae', 'bone grafting', 'dural sac', and 'nerve root compression'. This boundary overlap is an authentic clinical reality, not a flaw of the NLP model.

4. High Specificity in Urology and OB/GYN:
Urology scored 97% precision with only a single false positive across 31 records; OB/GYN achieved 93% precision across 31 records.""")

print("Slide 11 generated.")

# ==============================================================================
# SLIDE 12: Granular Specialty-Wise Performance Metrics
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12, LIGHT_BG)
add_header(s12, "CLASS-LEVEL PERFORMANCE BREAKDOWN", "Granular Classification Report across 8 Medical Specialties", 12)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s12, COL2_L, top_pos, COL2_W, col_h, top_accent=TEAL_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.24)
p = tf_l.paragraphs[0]
p.text = "PER-SPECIALTY CLASSIFICATION METRICS"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

t_rep_shape = s12.shapes.add_table(11, 6, Inches(0.80), Inches(1.95), Inches(5.50), Inches(4.70))
t_rep = t_rep_shape.table
t_rep.columns[0].width = Inches(2.20)
t_rep.columns[1].width = Inches(0.65)
t_rep.columns[2].width = Inches(0.65)
t_rep.columns[3].width = Inches(0.65)
t_rep.columns[4].width = Inches(0.65)
t_rep.columns[5].width = Inches(0.70)

rep_headers = ["Specialty", "TP", "Prec", "Recall", "F1", "Support"]
for ci, ch in enumerate(rep_headers):
    cell = t_rep.cell(0, ci)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TITLE
    p = cell.text_frame.paragraphs[0]
    p.text = ch
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.CENTER if ci > 0 else PP_ALIGN.LEFT

rep_rows = [
    ("Cardiovascular / Pulm.", "68", "0.88", "0.92", "0.90", "74"),
    ("ENT - Otolaryngology", "16", "0.94", "0.84", "0.89", "19"),
    ("Gastroenterology", "40", "0.87", "0.89", "0.88", "45"),
    ("Neurology", "35", "0.76", "0.78", "0.77", "45"),
    ("Obstetrics / Gynecology", "28", "0.93", "0.90", "0.92", "31"),
    ("Ophthalmology", "17", "1.00", "1.00", "1.00", "17"),
    ("Orthopedic", "63", "0.89", "0.89", "0.89", "71"),
    ("Urology", "28", "0.97", "0.90", "0.93", "31"),
    ("Macro Average", "295", "0.91", "0.89", "0.90", "333"),
    ("Weighted Average", "---", "0.89", "0.89", "0.89", "333")
]

for ri, rdata in enumerate(rep_rows, start=1):
    bg_col = RGBColor(0xDC, 0xFC, 0xE7) if ri == 6 else (RGBColor(0xFE, 0xF3, 0xC7) if ri >= 9 else (CARD_BG if ri % 2 == 1 else LIGHT_BLUE_BG))
    for ci, cval in enumerate(rdata):
        cell = t_rep.cell(ri, ci)
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg_col
        p = cell.text_frame.paragraphs[0]
        p.text = cval
        p.font.name = FONT_BODY
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_DARK
        p.alignment = PP_ALIGN.CENTER if ci > 0 else PP_ALIGN.LEFT
        if ri in (6, 9, 10) or ci == 0:
            p.font.bold = True

c_right = add_card(s12, COL2_R, top_pos, COL2_RW, col_h, top_accent=BLUE_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.28)
p = tf_r.paragraphs[0]
p.text = "DEPARTMENT PERFORMANCE"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = BLUE_ACCENT

p = tf_r.add_paragraph()
p.text = "Key Clinical Metric Findings"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

findings = [
    ("Ophthalmology: 1.00 F1-Score", "Flawless precision & recall (17/17 correct). Distinct anatomical terms."),
    ("Urology: 0.93 F1-Score", "97% precision with only 1 false positive across 31 test instances."),
    ("Obstetrics / Gynecology: 0.92 F1", "93% precision and 90% recall on maternal and fetal health dictations."),
    ("Cardiovascular: 0.90 F1-Score", "92% recall on largest test cohort (74 records: CABG, catheterization)."),
    ("Overall Macro Average: 0.90 F1", "0.91 Precision, 0.89 Recall, 0.90 Macro F1 across all 8 departments.")
]
for h, b in findings:
    p = tf_r.add_paragraph()
    p.space_before = Pt(11)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s12, """[EXPLANATION NOTES & TALKING POINTS]
Slide 12 breaks down the granular classification report across all eight medical specialties.

Key Departmental Takeaways:
- Ophthalmology: Perfect 1.00 F1-Score (100% precision, 100% recall, 17/17 correct). Eye surgery terminology (phacoemulsification, cataract, intraocular lens) forms an isolated cluster in TF-IDF space.
- Urology: 97% Precision and 0.93 F1-score with only 1 false positive across 31 test records, showing high clinical specificity.
- Obstetrics / Gynecology: 93% Precision, 90% Recall, and 0.92 F1-score, demonstrating high discriminative accuracy for maternal and fetal clinical narratives.
- Cardiovascular / Pulmonary: Maintained 92% Recall and 0.90 F1-score on our largest test cohort (74 records), accurately capturing catheterization, coronary bypass, and pulmonary function tests.
- Orthopedic: 89% Precision, 89% Recall, and 0.89 F1-score across 71 musculoskeletal cases.
- Neurology: 76% Precision and 78% Recall due to the overlapping spinal surgery boundary with orthopedics.

Macro Average:
Across all 8 departments, the unweighted Macro Average is 0.91 Precision, 0.89 Recall, and 0.90 Macro F1-score. This confirms that the model generalizes well across every single hospital specialty.""")

print("Slide 12 generated.")

# ==============================================================================
# SLIDE 13: Clinical Safety: Open-Set Confidence Rejection Gate (Dark Theme for Clinical Safety Priority)
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
set_slide_background(s13, DARK_BG)
add_header(s13, "CLINICAL SAFETY MECHANISM", "Open-Set Confidence Rejection Gate for Out-of-Scope Protection", 13, is_dark=True)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s13, COL2_L, top_pos, COL2_W, col_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=ROSE_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "THE CLOSED-WORLD VULNERABILITY"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = ROSE_ACCENT

p = tf_l.add_paragraph()
p.text = "Why Standard AI Fails in Hospitals"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

fail_modes = [
    ("Closed-World Assumption", "Standard ML models assume all incoming text belongs to trained classes."),
    ("Erroneous Force-Fitting", "A dermatology or psychiatry note will be falsely forced into cardiology or ortho."),
    ("Severe Patient Safety Hazard", "Misdirected referrals waste specialist appointments and delay critical care."),
    ("Need for Selective Classification", "A clinical AI must know when it is uncertain and defer to humans.")
]
for h, b in fail_modes:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u26a0 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = TEXT_SKY
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

c_right = add_card(s13, COL2_R, top_pos, COL2_RW, col_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=AMBER_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.28)
p = tf_r.paragraphs[0]
p.text = "OPEN-SET GATING MECHANICS"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = AMBER_ACCENT

p = tf_r.add_paragraph()
p.text = "Threshold \u03c4 = 0.48 Decision Rule"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

rejection_logic = [
    ("Mathematical Decision Rule", "If max P_ens(c|x) >= 0.48 -> Route; Else -> 'Other / Requires Review'."),
    ("Threshold Derivation (\u03c4 = 0.48)", "92.5% of in-domain cases have P >= 0.65; marginal neuro-ortho edge cases sit at 0.48–0.64."),
    ("100% Out-of-Scope Interception", "Tested out-of-domain notes (dermatology, psychiatry) had P < 0.41, triggering 100% rejection."),
    ("Visual Amber UI Warning Banner", "Alerts triage coders to review document manually, showing differential candidates.")
]
for h, b in rejection_logic:
    p = tf_r.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u2714 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = AMBER_ACCENT
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

add_slide_notes(s13, """[EXPLANATION NOTES & TALKING POINTS]
Slide 13 addresses one of the most critical contributions of this project: the Open-Set Confidence Rejection Gate.

The Hazard of the Closed-World Assumption:
- In clinical hospitals, patients present with conditions outside our 8 trained specialties—such as Dermatology, Psychiatry, or Pediatrics.
- Under naive argmax classification, if an eczema biopsy or depression screening note is submitted, the system will arbitrarily force-fit the patient into an incorrect department (e.g., misrouting a skin rash note to Cardiology).
- In medicine, this causes delayed treatments, wasted specialist appointments, and serious liability.

Our Open-Set Rejection Rule:
We implemented a confidence thresholding gate:
- If max P_ens(c|x) >= tau = 0.48: The prediction is routed automatically.
- If max P_ens(c|x) < tau = 0.48: The document is routed to an operational 9th class: 'Other / Requires Clinical Review'.

Why tau = 0.48?
In an 8-class problem, uniform random guessing is 1/8 = 12.5%. A probability of 48% is nearly four times random chance.
Our validation analysis showed:
- 92.5% of valid in-domain cases exhibited high confidence (P >= 0.65).
- Borderline neuro-orthopedic spine cases clustered between 0.48 and 0.64.
- When tested on out-of-domain clinical notes (dermatology, psychiatry, non-medical text), peak probabilities dispersed across classes (P < 0.41), resulting in 100% successful rejection. This completely safeguards hospital triage.""")

print("Slide 13 (Dark Clinical Safety Theme) generated.")

# ==============================================================================
# SLIDE 14: Production Web Service & Deployment Architecture
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
set_slide_background(s14, LIGHT_BG)
add_header(s14, "SYSTEM ARCHITECTURE & DEPLOYMENT", "Lightweight Flask REST Microservice & In-Memory Pipeline", 14)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s14, COL2_L, top_pos, COL2_W, col_h, top_accent=TEAL_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "BACKEND MICROSERVICE DESIGN"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_l.add_paragraph()
p.text = "Flask RESTful Service Architecture"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(4)

back_props = [
    ("Stateless Flask REST Framework", "Zero runtime session state; seamless horizontal scaling on hospital networks."),
    ("Pre-Loaded Model Weights in RAM", "Frozen TF-IDF (314 KB) & voting ensemble (11.6 MB) loaded once during boot."),
    ("In-Memory PyMuPDF PDF Parsing", "Parses multi-page PDFs in 3.85 ms directly from byte streams; zero disk caching."),
    ("Ultra-Low Memory Footprint", "Entire service runs in <145 MB of RAM on commodity hospital workstations.")
]
for h, b in back_props:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = TEXT_DARK

c_right = add_card(s14, COL2_R, top_pos, COL2_RW, col_h, top_accent=EMERALD_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.24)
p = tf_r.paragraphs[0]
p.text = "LATENCY TELEMETRY PROFILING"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = EMERALD_ACCENT

t_lat_shape = s14.shapes.add_table(8, 3, Inches(6.95), Inches(1.95), Inches(5.63), Inches(3.20))
t_lat = t_lat_shape.table
t_lat.columns[0].width = Inches(2.63)
t_lat.columns[1].width = Inches(1.20)
t_lat.columns[2].width = Inches(1.80)

lat_headers = ["Pipeline Stage", "Mean Latency", "Operational Function"]
for ci, ch in enumerate(lat_headers):
    cell = t_lat.cell(0, ci)
    cell.fill.solid()
    cell.fill.fore_color.rgb = NAVY_TITLE
    p = cell.text_frame.paragraphs[0]
    p.text = ch
    p.font.name = FONT_BODY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.alignment = PP_ALIGN.CENTER if ci == 1 else PP_ALIGN.LEFT

lat_rows = [
    ("HTTP Payload Ingestion", "0.42 ms", "Stream deserialization"),
    ("PyMuPDF PDF Extraction", "3.85 ms", "In-memory page text parsing"),
    ("Regex Text Normalization", "0.81 ms", "Sanitization & lowercase"),
    ("TF-IDF Vectorization", "1.24 ms", "Sparse matrix multiplication"),
    ("Base Model Inference (4 Models)", "2.15 ms", "SVM, LR, RF, MNB scoring"),
    ("Soft Voting & Thresholding", "0.38 ms", "Consensus & \u03c4=0.48 gating"),
    ("Total End-to-End Latency", "9.20 ms", "Sub-10 ms Real-Time Turnaround")
]

for ri, rdata in enumerate(lat_rows, start=1):
    bg_col = RGBColor(0xDC, 0xFC, 0xE7) if ri == 7 else (CARD_BG if ri % 2 == 1 else LIGHT_BLUE_BG)
    for ci, cval in enumerate(rdata):
        cell = t_lat.cell(ri, ci)
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg_col
        p = cell.text_frame.paragraphs[0]
        p.text = cval
        p.font.name = FONT_BODY
        p.font.size = Pt(9)
        p.font.color.rgb = TEXT_DARK
        p.alignment = PP_ALIGN.CENTER if ci == 1 else PP_ALIGN.LEFT
        if ri == 7 or ci == 0:
            p.font.bold = True

t_under_lat = s14.shapes.add_textbox(Inches(6.95), Inches(5.30), Inches(5.63), Inches(1.40))
tf_ulat = t_under_lat.text_frame
tf_ulat.margin_left = tf_ulat.margin_right = tf_ulat.margin_top = 0
tf_ulat.word_wrap = True
lat_bullets = [
    ("Throughput: >100 TPS on CPU", "Processes over 100 clinical records per second on a single commodity quad-core CPU."),
    ("100% HIPAA Data Privacy", "In-memory byte parsing guarantees zero unencrypted patient data leaks to disk.")
]
for h, b in lat_bullets:
    p = tf_ulat.add_paragraph()
    p.space_before = Pt(5)
    r1 = p.add_run()
    r1.text = "\u2714 " + h + ": "
    r1.font.bold = True
    r1.font.size = Pt(10.5)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

add_slide_notes(s14, """[EXPLANATION NOTES & TALKING POINTS]
Slide 14 details our production deployment architecture.

Backend Architectural Highlights:
1. Lightweight Flask Microservice:
We deployed the pipeline as a stateless REST service using Flask. Statelessness ensures that consecutive client requests are decoupled, allowing seamless horizontal scaling across hospital intranet nodes.
2. RAM Model Loading:
The frozen TF-IDF vectorizer (314 KB) and voting ensemble (11.6 MB) are deserialized into memory during application boot. This eliminates disk I/O bottlenecks during live patient triage.
3. In-Memory PyMuPDF PDF Ingestion:
Clinical consultation letters frequently arrive as PDF documents. PyMuPDF (fitz) extracts text directly from in-memory byte buffers in 3.85 milliseconds. Because no files are written to disk, patient privacy (HIPAA compliance) is strictly maintained.

Latency Telemetry Profile (Table):
We profiled 500 consecutive requests on an ordinary Intel quad-core processor (no GPU):
- HTTP ingestion: 0.42 ms
- PDF parsing: 3.85 ms
- Regex cleaning: 0.81 ms
- TF-IDF sparse matrix multiplication: 1.24 ms
- Concurrent 4-model evaluation: 2.15 ms
- Soft voting & thresholding: 0.38 ms
- Total end-to-end latency: exactly 9.20 milliseconds!
This supports over 100 transactions per second on a single CPU core.""")

print("Slide 14 generated.")

# ==============================================================================
# SLIDE 15: UI Design Philosophy & Healthcare UX Design System (Dark Theme Matching Actual UI)
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
set_slide_background(s15, DARK_BG)
add_header(s15, "HEALTHCARE USER INTERFACE DESIGN", "UI Design System, Cognitive Ergonomics & Usability Tokens", 15, is_dark=True)

top_pos = Inches(1.48)
col_h = Inches(5.35)

c_left = add_card(s15, COL2_L, top_pos, COL2_W, col_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=TEAL_ACCENT)
tf_l = c_left.text_frame
tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.28)
p = tf_l.paragraphs[0]
p.text = "DESIGN PHILOSOPHY"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_l.add_paragraph()
p.text = "Cognitive Ergonomics for Healthcare"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

ux_principles = [
    ("Mitigating Cognitive Fatigue", "Dark slate-navy palette (#0A192F) reduces ocular glare during long shifts."),
    ("Definitive Status Signposting", "Emerald green (Definitive), Amber orange (Review), Crimson red (Error)."),
    ("Explainable Clinical Feedback", "Displays matched TF-IDF keywords, candidate spreads, and model consensus."),
    ("Zero-Friction Responsiveness", "Pure Vanilla JS & CSS Grid for instantaneous UI transitions without reloads.")
]
for h, b in ux_principles:
    p = tf_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = TEXT_SKY
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

c_right = add_card(s15, COL2_R, top_pos, COL2_RW, col_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=CYAN_ACCENT)
tf_r = c_right.text_frame
tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.28)
p = tf_r.paragraphs[0]
p.text = "FRONTEND ARCHITECTURE"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = CYAN_ACCENT

p = tf_r.add_paragraph()
p.text = "Four Integrated Dashboard Modules"
p.font.name = FONT_TITLE
p.font.size = Pt(16.5)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

front_arch = [
    ("Dual Input Modalities", "Supports direct keyboard entry, clipboard paste, and drag-and-drop PDF upload."),
    ("Pre-Loaded Clinical Samples", "Quick-test buttons populated with authentic held-out test dictations."),
    ("Persistent Top Navigation", "Allows fluid switching across Triage, Workflow, Benchmarks, and Vocabulary."),
    ("Zero Framework Bloat", "Built with semantic HTML5, CSS3 Grid/Flexbox, and vanilla async JavaScript.")
]
for h, b in front_arch:
    p = tf_r.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u2714 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = CYAN_ACCENT
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

add_slide_notes(s15, """[EXPLANATION NOTES & TALKING POINTS]
Slide 15 addresses the user interface design philosophy—a vital feature that was missing in our interim review and is now fully realized in our final project.

Cognitive Ergonomics in Clinical Informatics:
Physicians and medical triage coders work in high-stress, time-sensitive environments. Cluttered user interfaces cause cognitive fatigue, which directly leads to diagnostic oversights.
We designed MedSpecialty AI adhering to four strict design principles:
1. Visual Palette & Eye Comfort: Built upon a deep slate-navy background (#0A192F, #0F2444) accented with clinical teal. This eliminates the harsh glare of all-white screens during night shifts.
2. Definitive Status Signposting: Standardized color psychology confirms triage status instantly: emerald green for definitive automated routing, amber orange for open-set human review warnings, and crimson red for invalid input.
3. Clinical Explainability: Rather than showing a raw label, the UI reveals the exact matched clinical keywords and differential probability percentages.
4. Pure Vanilla Client: Engineered with semantic HTML5, CSS3, and vanilla asynchronous JavaScript. It eliminates heavy framework dependencies like React or Angular, ensuring the dashboard loads instantaneously.""")

print("Slide 15 (Dark UI UX Theme) generated.")

# ==============================================================================
# SLIDE 16: UI Screen 1: Clinical Triage & Prediction Console
# ==============================================================================
s16 = prs.slides.add_slide(blank_layout)
set_slide_background(s16, LIGHT_BG)
add_header(s16, "UI SCREEN 1: PREDICTION CONSOLE", "Interactive Clinical Specialty Prediction & Triage Dashboard", 16)

c_s16_l = add_card(s16, Inches(0.60), Inches(1.48), Inches(4.70), Inches(5.35), top_accent=TEAL_ACCENT)
tf_s16_l = c_s16_l.text_frame
tf_s16_l.margin_left = tf_s16_l.margin_right = tf_s16_l.margin_top = Inches(0.25)
p = tf_s16_l.paragraphs[0]
p.text = "TRIAGE CONSOLE FEATURES"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_s16_l.add_paragraph()
p.text = "Operational Capabilities"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(3)

s16_features = [
    ("Live Narrative Textarea", "Spacious editor with auto-resizing & placeholder clinical guidance."),
    ("Drag-and-Drop PDF Zone", "Accepts digital consultation summaries with in-memory extraction."),
    ("Pre-Loaded Sample Buttons", "One-click access to held-out cardiac, laparoscopic, and ortho notes."),
    ("Specialty Hero Card", "Prominently displays routed specialty with confidence score (94.2%)."),
    ("Differential Candidates", "Horizontal bars rendering top-3 candidate specialty probabilities."),
    ("Explainability Chips", "Highlighted diagnostic tokens: coronary, stenosis, catheter, myocardial.")
]
for h, b in s16_features:
    p = tf_s16_l.add_paragraph()
    p.space_before = Pt(8)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

card_img1 = add_card(s16, Inches(5.50), Inches(1.48), Inches(7.23), Inches(5.35), bg_color=CARD_BG, border_color=CARD_BORDER, top_accent=BLUE_ACCENT)
if os.path.exists(img_ui_prediction):
    s16.shapes.add_picture(img_ui_prediction, Inches(5.60), Inches(1.58), Inches(7.03), Inches(5.15))

add_slide_notes(s16, """[EXPLANATION NOTES & TALKING POINTS]
Slide 16 presents Screen 1: our primary Clinical Specialty Prediction and Triage Console.

Walkthrough of the Screen:
The interface is structured into two balanced columns:
1. Left Input Column:
- Clinicians can paste consultation text directly, or drag-and-drop a multi-page PDF document into the dashed drop-zone.
- Below the input box, quick-load buttons allow instant testing of authentic held-out cases—such as Cardiac Catheterization, Laparoscopic Cholecystectomy, or Lumbar Discectomy.

2. Right Output Column (Active Prediction):
Upon clicking 'Analyze & Classify', the system executes in 9.2 milliseconds and displays:
- Specialty Hero Card: In this active example, routing the patient to 'Cardiovascular / Pulmonary' with a calibrated confidence of 94.2%.
- Clinical Action Status Banner: An emerald green banner confirming 'Definitive Routing' and explaining clinical workflow implications.
- Differential Candidates: Horizontal progress bars showing the top-3 candidate departments (Cardiovascular: 94.2%, Gastroenterology: 3.1%, Orthopedic: 1.2%).
- Explainability Keyword Chips: Diagnostic tokens extracted from the text ('coronary', 'stenosis', 'catheter', 'myocardial') that contributed the highest positive TF-IDF weight toward the prediction.""")

print("Slide 16 generated.")

# ==============================================================================
# SLIDE 17: UI Screen 2: 7-Stage End-to-End Operational Pipeline
# ==============================================================================
s17 = prs.slides.add_slide(blank_layout)
set_slide_background(s17, LIGHT_BG)
add_header(s17, "UI SCREEN 2: OPERATIONAL WORKFLOW", "7-Stage End-to-End Algorithmic Dataflow Visualizer", 17)

c_s17_l = add_card(s17, Inches(0.60), Inches(1.48), Inches(4.70), Inches(5.35), top_accent=TEAL_ACCENT)
tf_s17_l = c_s17_l.text_frame
tf_s17_l.margin_left = tf_s17_l.margin_right = tf_s17_l.margin_top = Inches(0.25)
p = tf_s17_l.paragraphs[0]
p.text = "7-PHASE ARCHITECTURAL FLOW"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_s17_l.add_paragraph()
p.text = "Dataflow Pipeline Phases"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(3)

s17_phases = [
    ("Phase 1: Ingestion", "Free-text narrative or in-memory PyMuPDF PDF stream."),
    ("Phase 2: Text Normalization", "Regex cleaning [^a-zA-Z\\\\s] & contraction expansion."),
    ("Phase 3: Lemmatization", "WordNet morphological reduction to base anatomical lemma."),
    ("Phase 4: TF-IDF Vectorization", "Sublinear unigram/bigram mapping across 8,000 features."),
    ("Phase 5: Multi-Model Scoring", "Concurrent inference across SVM, LR, RF, and MNB."),
    ("Phase 6: Soft Voting Consensus", "Weighted probability averaging [2:2:1:1]."),
    ("Phase 7: Open-Set Rejection", "Threshold verification (\u03c4 = 0.48) routing to triage or review.")
]
for h, b in s17_phases:
    p = tf_s17_l.add_paragraph()
    p.space_before = Pt(6)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

card_img2 = add_card(s17, Inches(5.50), Inches(1.48), Inches(7.23), Inches(5.35), bg_color=CARD_BG, border_color=CARD_BORDER, top_accent=INDIGO_ACCENT)
if os.path.exists(img_ui_how_it_works):
    s17.shapes.add_picture(img_ui_how_it_works, Inches(5.60), Inches(1.58), Inches(7.03), Inches(5.15))

add_slide_notes(s17, """[EXPLANATION NOTES & TALKING POINTS]
Slide 17 demonstrates Screen 2: the Operational Dataflow Visualizer (How It Works).

Educational & Audit Significance:
Medical practitioners are often skeptical of automated systems. To build clinical trust, our application includes an interactive visualizer detailing the 7 discrete mathematical transformations applied to patient data:

1. Phase 1 (Ingestion): Ingests raw narrative text or extracts text from uploaded PDF files in-memory.
2. Phase 2 (Text Sanitization): Removes noise characters, numbers, and expands clinical contractions.
3. Phase 3 (Lemmatization): Standardizes inflected medical terms using the WordNet morphological engine.
4. Phase 4 (Vectorization): Maps the clean tokens into an 8,000-dimensional sparse numeric space using sublinear TF-IDF.
5. Phase 5 (Model Scoring): Dispatches the vector concurrently across all four trained estimators (Linear SVM, Logistic Regression, Random Forest, and Naive Bayes).
6. Phase 6 (Consensus): Combines posterior probabilities using our [2:2:1:1] soft voting consensus rule.
7. Phase 7 (Clinical Rejection): Evaluates the peak probability against tau = 0.48. If confident, it assigns the specialty; if ambiguous, it safely refers the file to human review.""")

print("Slide 17 generated.")

# ==============================================================================
# SLIDE 18: UI Screen 3: Multi-Model Consensus & Performance Analytics
# ==============================================================================
s18 = prs.slides.add_slide(blank_layout)
set_slide_background(s18, LIGHT_BG)
add_header(s18, "UI SCREEN 3: PERFORMANCE ANALYTICS", "Model Benchmarks, Comparative Metrics & Confusion Matrix", 18)

c_s18_l = add_card(s18, Inches(0.60), Inches(1.48), Inches(4.70), Inches(5.35), top_accent=TEAL_ACCENT)
tf_s18_l = c_s18_l.text_frame
tf_s18_l.margin_left = tf_s18_l.margin_right = tf_s18_l.margin_top = Inches(0.25)
p = tf_s18_l.paragraphs[0]
p.text = "ANALYTICS DASHBOARD MODULE"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_s18_l.add_paragraph()
p.text = "Validation Telemetry"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(3)

s18_features = [
    ("Top-Line KPI Metric Cards", "Live validation statistics: 88.59% Acc, 0.8971 F1, 0.9051 Prec."),
    ("Comparative Benchmark Matrix", "Side-by-side comparison of SVM, Ensemble, LR, RF, and MNB."),
    ("Interactive Confusion Matrix", "Heatmap rendering True Positives & misclassification counts across 333 test records."),
    ("REST Telemetry Endpoint", "Served dynamically via 'GET /api/model-info' for live auditing.")
]
for h, b in s18_features:
    p = tf_s18_l.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

card_img3 = add_card(s18, Inches(5.50), Inches(1.48), Inches(7.23), Inches(5.35), bg_color=CARD_BG, border_color=CARD_BORDER, top_accent=EMERALD_ACCENT)
if os.path.exists(img_ui_performance):
    s18.shapes.add_picture(img_ui_performance, Inches(5.60), Inches(1.58), Inches(7.03), Inches(5.15))

add_slide_notes(s18, """[EXPLANATION NOTES & TALKING POINTS]
Slide 18 presents Screen 3: the Model Performance Analytics Dashboard.

Purpose and Functionality:
This module allows hospital data scientists, chief medical officers, and department heads to monitor the mathematical validity of the deployed model directly in production.

Dashboard Components:
1. Top-Line KPI Cards: Prominently displays the holdout validation metrics: 88.59% Accuracy, 0.8971 Macro F1-Score, 0.9051 Precision, and 0.8902 Recall.
2. Comparative Benchmark Table: Displays a side-by-side evaluation of all five model configurations across Accuracy, Precision, Recall, Macro-F1, Weighted-F1, and Training Execution Time.
3. Interactive Confusion Matrix Heatmap: Renders exact True Positive counts and off-diagonal misclassification boundaries across all 333 test samples.
4. Backend Integration: The screen is dynamically fed by our Flask REST endpoint 'GET /api/model-info', decoupling model metrics from presentation logic.""")

print("Slide 18 generated.")

# ==============================================================================
# SLIDE 19: UI Screen 4: Feature Space & Clinical Vocabulary Explorer
# ==============================================================================
s19 = prs.slides.add_slide(blank_layout)
set_slide_background(s19, LIGHT_BG)
add_header(s19, "UI SCREEN 4: VOCABULARY INSPECTOR", "Feature Space Explorer & Diagnostic Clinical Vocabulary Analysis", 19)

c_s19_l = add_card(s19, Inches(0.60), Inches(1.48), Inches(4.70), Inches(5.35), top_accent=TEAL_ACCENT)
tf_s19_l = c_s19_l.text_frame
tf_s19_l.margin_left = tf_s19_l.margin_right = tf_s19_l.margin_top = Inches(0.25)
p = tf_s19_l.paragraphs[0]
p.text = "FEATURE SPACE INSPECTOR"
p.font.name = FONT_BODY
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_s19_l.add_paragraph()
p.text = "Clinical Lexical Transparency"
p.font.name = FONT_TITLE
p.font.size = Pt(15.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE
p.space_before = Pt(3)

s19_features = [
    ("Specialty Dropdown Selector", "Select any of the 8 departments to audit top-weighted n-grams."),
    ("Ophthalmology Vocabulary", "cataract, lens, phacoemulsification, intraocular, visual acuity."),
    ("Cardiology Vocabulary", "coronary, stenosis, catheter, myocardial, angioplasty, stent."),
    ("Orthopedic Vocabulary", "fracture, fixation, femur, tibia, joint, arthroplasty, graft."),
    ("Spurious Correlation Audit", "Validates that models learned true anatomy, not clerical noise.")
]
for h, b in s19_features:
    p = tf_s19_l.add_paragraph()
    p.space_before = Pt(9)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = NAVY_TITLE
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10)
    r2.font.color.rgb = TEXT_DARK

card_img4 = add_card(s19, Inches(5.50), Inches(1.48), Inches(7.23), Inches(5.35), bg_color=CARD_BG, border_color=CARD_BORDER, top_accent=AMBER_ACCENT)
if os.path.exists(img_ui_features):
    s19.shapes.add_picture(img_ui_features, Inches(5.60), Inches(1.58), Inches(7.03), Inches(5.15))

add_slide_notes(s19, """[EXPLANATION NOTES & TALKING POINTS]
Slide 19 presents Screen 4: the Feature Space and Vocabulary Inspector.

Clinical Explainability & Auditing Bias:
In medical artificial intelligence, verifying that the model has not learned 'spurious correlations' (such as hospital phone numbers, doctor names, or clerical timestamps) is vital for patient safety and regulatory approval.

Feature Inspection:
This module allows clinical experts to select any department from a dropdown menu and inspect its highest-weighted diagnostic n-gram features:
- Ophthalmology: cataract, phacoemulsification, lens, cornea, intraocular, visual acuity.
- Cardiovascular: coronary, stenosis, catheter, myocardial, angioplasty, stent.
- Orthopedics: fracture, fixation, femur, tibia, joint, arthroplasty, graft.

Each term is accompanied by a horizontal bar reflecting its mathematical weight derived from the linear hyperplane coefficients. This proves that MedSpecialty AI bases its decisions strictly on authentic anatomical, surgical, and pharmacological terminology.""")

print("Slide 19 generated.")

# ==============================================================================
# SLIDE 20: Conclusion, Key Contributions, Future Scope & Acknowledgements (Dark Luxury Navy Theme)
# ==============================================================================
s20 = prs.slides.add_slide(blank_layout)
set_slide_background(s20, DARK_BG)
add_header(s20, "CONCLUSION & FUTURE HORIZONS", "Project Deliverables, Research Contributions, Future Scope & Thanks", 20, is_dark=True)

card_w = Inches(3.80)
card_h = Inches(5.35)
top_pos = Inches(1.48)

# Col 1: Project Achievements (Teal Accent)
c_c1 = add_card(s20, get_col3_left(0), top_pos, card_w, card_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=TEAL_ACCENT)
tf_c1 = c_c1.text_frame
tf_c1.margin_left = tf_c1.margin_right = tf_c1.margin_top = Inches(0.28)
p = tf_c1.paragraphs[0]
p.text = "1. ACHIEVEMENTS"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT

p = tf_c1.add_paragraph()
p.text = "Milestones Met"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

achieve_b = [
    ("Accuracy Target Exceeded", "SVM: 88.59% (0.8971 F1); Ensemble: 87.99% (0.8898 F1) vs 75% target."),
    ("Clean 8-Class Benchmark", "1,663 records resolving administrative contamination."),
    ("Sub-10ms CPU Latency", "9.20 ms total turnaround (>100 TPS without GPU)."),
    ("Open-Set Clinical Safety", "100% out-of-domain interception via threshold \u03c4 = 0.48.")
]
for h, b in achieve_b:
    p = tf_c1.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u2714 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = TEAL_ACCENT
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

# Col 2: Deliverables & Engineering (Cyan Accent)
c_c2 = add_card(s20, get_col3_left(1), top_pos, card_w, card_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=CYAN_ACCENT)
tf_c2 = c_c2.text_frame
tf_c2.margin_left = tf_c2.margin_right = tf_c2.margin_top = Inches(0.28)
p = tf_c2.paragraphs[0]
p.text = "2. DELIVERABLES"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = CYAN_ACCENT

p = tf_c2.add_paragraph()
p.text = "Software Artifacts"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

deliv_b = [
    ("Production Web App", "MedSpecialty AI dashboard with 4 interactive modules."),
    ("In-Memory PDF Parsing", "3.85 ms PyMuPDF extraction with zero disk residue."),
    ("Serialized ML Binaries", "Joblib compressed 8,000-term TF-IDF & 4-model ensemble."),
    ("IEEE LaTeX Final Report", "Comprehensive documentation prepared with academic rigor.")
]
for h, b in deliv_b:
    p = tf_c2.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u25aa " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = CYAN_ACCENT
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

# Col 3: Future Scope & Acknowledgements (Emerald Accent)
c_c3 = add_card(s20, get_col3_left(2), top_pos, card_w, card_h, bg_color=DARK_CARD, border_color=DARK_CARD_BORDER, top_accent=EMERALD_ACCENT)
tf_c3 = c_c3.text_frame
tf_c3.margin_left = tf_c3.margin_right = tf_c3.margin_top = Inches(0.28)
p = tf_c3.paragraphs[0]
p.text = "3. FUTURE WORK & THANKS"
p.font.name = FONT_BODY
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = EMERALD_ACCENT

p = tf_c3.add_paragraph()
p.text = "Expansion & Acknowledgements"
p.font.name = FONT_TITLE
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_before = Pt(4)

future_b = [
    ("HL7 / FHIR Integration", "Direct connection to hospital EHR message queues."),
    ("Active Learning Loop", "Physician feedback loop to refine borderline predictions."),
    ("Multilingual NLP", "Extension to regional Indian languages (Malayalam, Hindi)."),
    ("Heartfelt Acknowledgements", "Gratitude to Guide Prof. Biju Skaria, HOD Dr. Sonia Abraham, Dr. Manu John, & faculty.")
]
for h, b in future_b:
    p = tf_c3.add_paragraph()
    p.space_before = Pt(12)
    r1 = p.add_run()
    r1.text = "\u2728 " + h + "\n"
    r1.font.bold = True
    r1.font.size = Pt(12)
    r1.font.color.rgb = EMERALD_ACCENT
    r2 = p.add_run()
    r2.text = b
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

add_slide_notes(s20, """[EXPLANATION NOTES & TALKING POINTS]
In conclusion, this mini project has successfully conceptualized, validated, and deployed an end-to-end clinical machine learning decision support platform.

Summary of Contributions:
1. Performance Excellence: Linear SVM achieved 88.59% accuracy and 0.8971 Macro F1; our Soft Voting Ensemble achieved 87.99% accuracy and 0.8898 Macro F1 across eight major hospital specialties, vastly exceeding the project requirement of 75.0%.
2. Clinical Safety Guardrail: By integrating our Open-Set Confidence Rejection Gate (tau = 0.48), we solved the closed-world failure mode of conventional AI, guaranteeing that ambiguous and out-of-scope notes are intercepted for human review.
3. Operational Deployment: We delivered a lightweight, sub-10 millisecond web service with in-memory PyMuPDF extraction, providing complete clinical explainability and high responsiveness on commodity CPU hardware.

Future Scope:
- Interfacing with hospital HL7/FHIR message buses for real-time EHR ingestion.
- Implementing an active learning loop where clinician overrides continuously retrain models.
- Extending tokenizers to support regional Indian languages such as Malayalam and Hindi for primary health centers.

Acknowledgements:
I express my deepest gratitude to my esteemed project guide Prof. Biju Skaria for his continuous guidance, Dr. Sonia Abraham for departmental leadership, Dr. Manu John for project coordination, and the respected examiners. Thank you very much. I am now ready for viva voce questions.""")

print("Slide 20 (Dark Closing Theme) generated.")

# Save presentation
output_dir = r'D:\Antigravity Projects\Mini Project S3 MCA\Final Presentation PPT'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'Medical_Specialty_Classification_Final_Project_Presentation.pptx')
try:
    prs.save(output_path)
    print(f"Presentation successfully updated and saved to: {output_path}")
except PermissionError:
    alt_path = os.path.join(output_dir, 'Medical_Specialty_Classification_Final_Presentation_Themed.pptx')
    prs.save(alt_path)
    print(f"PermissionError on original file (locked). Saved to alternate path: {alt_path}")
