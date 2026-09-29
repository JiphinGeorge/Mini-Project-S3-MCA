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
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.32), Inches(4.3), Inches(0.34))
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

# ==============================================================================
# SLIDE 1: Title Slide (Dark Theme)
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, DARK_BG)

# College Banner
t1 = s1.shapes.add_textbox(Inches(0.9), Inches(0.50), Inches(11.53), Inches(0.40))
tf1 = t1.text_frame
p1 = tf1.paragraphs[0]
p1.text = "MAR ATHANASIUS COLLEGE OF ENGINEERING, KOTHAMANGALAM"
p1.font.name = FONT_BODY
p1.font.size = Pt(13)
p1.font.bold = True
p1.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

# Badge Pill
pill1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.05), Inches(5.2), Inches(0.42))
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

# Project Title
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
p_sub.text = "Phase 2: Model Training, Ensemble Evaluation & Empirical Findings"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(18)
p_sub.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8) # Bright Sky Blue
p_sub.space_before = Pt(8)

# Presenter Card (Left)
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
p_reg.text = "Register No: MAC25MCA-2033\nCourse: Master of Computer Applications (MCA)\nSemester: 3 | Academic Year: 2026-2027"
p_reg.font.name = FONT_BODY
p_reg.font.size = Pt(12)
p_reg.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)
p_reg.space_before = Pt(6)

# Guide Card (Right)
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
p_gdept.text = "Department of Computer Applications\nMar Athanasius College of Engineering, Kothamangalam\nAffiliated to APJ Abdul Kalam Technological University"
p_gdept.font.name = FONT_BODY
p_gdept.font.size = Pt(12)
p_gdept.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)
p_gdept.space_before = Pt(6)

# Bottom Feature Badges
tags = ["Clinical NLP", "TF-IDF (8k Features)", "4 Base Classifiers", "Soft Voting Ensemble", "Milestone: 30-09-2026"]
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
# SLIDE 2: Project Recap & Phase 2 Objectives
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2, LIGHT_BG)
add_header(s2, "MCA MINI PROJECT | RECAP & OBJECTIVES", "Project Recap & Phase 2 Objectives", 2)

# Left Column: Phase 1 Recap & Baseline Challenge
add_card(s2, Inches(0.6), Inches(1.5), Inches(5.9), Inches(5.3))
t_s2_l = s2.shapes.add_textbox(Inches(0.85), Inches(1.7), Inches(5.4), Inches(4.9))
tf_s2_l = t_s2_l.text_frame
tf_s2_l.word_wrap = True

p = tf_s2_l.paragraphs[0]
p.text = "Phase 1: Exploration & The 40-Class Baseline"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

bullets_l = [
    ("Exploratory Foundation (Phase 1)", "Analyzed Kaggle MTSamples clinical transcriptions (4,999 raw records) and built text cleaning, tokenization, and stop-word filtering routines."),
    ("The 40-Class Baseline Barrier", "Initial candidate model training across all 40 raw categories yielded poor accuracy, ranging between 7.85% and 27.39%."),
    ("Root Causes of Baseline Collapse", "1. Extreme Class Skew: 1,103 Surgery records vs 2 Autopsy records.\n2. Document Format Artifacts: SOAP notes, consults, and discharge summaries masquerading as specialties.\n3. High Dimensionality: Over 310,000 unconstrained TF-IDF n-grams diluting clinical signal.")
]
for title, desc in bullets_l:
    p_b = tf_s2_l.add_paragraph()
    p_b.text = f"• {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(11.5)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(8)
    
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Right Column: Phase 2 Objectives
add_card(s2, Inches(6.8), Inches(1.5), Inches(5.93), Inches(5.3))
t_s2_r = s2.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.43), Inches(4.9))
tf_s2_r = t_s2_r.text_frame
tf_s2_r.word_wrap = True

p = tf_s2_r.paragraphs[0]
p.text = "Phase 2: Refinement, Training & Evaluation"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

bullets_r = [
    ("Curate Mutually Exclusive Specialties", "Refine the dataset to 8 core clinical specialties (1,663 records) eliminating procedural overlap and administrative formats."),
    ("Constrain TF-IDF Representation", "Fit an 8,000-feature unigram/bigram vectorizer strictly on training data with sublinear term-frequency scaling and L2 normalization."),
    ("Train 4 Core Supervised ML Models", "Train and tune Linear SVM, Logistic Regression, Random Forest, and Multinomial Naive Bayes using balanced class weighting."),
    ("Ensemble Probability Calibration", "Calibrate SVM via Platt scaling and formulate Hard Voting and Weighted Soft Voting (weights: LR=2, SVM=2, RF=1, MNB=1)."),
    ("Target Benchmark", "Exceed the required 75.0% target accuracy threshold with robust macro/weighted F1-scores on 333 held-out test records.")
]
for title, desc in bullets_r:
    p_b = tf_s2_r.add_paragraph()
    p_b.text = f"✓ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(11.5)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_GREEN
    p_b.space_before = Pt(8)
    
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 3: Dataset Refinement & Clinical Specialty Selection
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, LIGHT_BG)
add_header(s3, "MCA MINI PROJECT | DATASET CURATION", "Dataset Refinement & Clinical Specialty Selection", 3)

# 3 Column Cards
c_w = Inches(3.85)
gap = Inches(0.28)

# Col 1: Cleaned Dataset
add_card(s3, Inches(0.6), Inches(1.5), c_w, Inches(5.3))
t_c1 = s3.shapes.add_textbox(Inches(0.75), Inches(1.7), c_w - Inches(0.3), Inches(4.9))
tf_c1 = t_c1.text_frame
tf_c1.word_wrap = True
p = tf_c1.paragraphs[0]
p.text = "1. Cleaned Dataset (MTSamples)"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

col1_points = [
    ("4,966 Cleaned Records", "Filtered from 4,999 after removing 33 empty transcription records."),
    ("40 Original Categories", "Encompassed entire range of dictation types in hospital archives."),
    ("Massive Majority Class", "Surgery contained 1,103 records (22.2% of the entire corpus)."),
    ("Target Whitespace Sanitization", "Leading/trailing whitespace in category strings stripped to ensure clean categorical indexing.")
]
for title, desc in col1_points:
    p_b = tf_c1.add_paragraph()
    p_b.text = f"• {title}:\n"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Col 2: Identified Problems
add_card(s3, Inches(0.6 + c_w + gap), Inches(1.5), c_w, Inches(5.3))
t_c2 = s3.shapes.add_textbox(Inches(0.75 + c_w + gap), Inches(1.7), c_w - Inches(0.3), Inches(4.9))
tf_c2 = t_c2.text_frame
tf_c2.word_wrap = True
p = tf_c2.paragraphs[0]
p.text = "2. Structural Data Issues"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = RED_ACCENT

col2_points = [
    ("Severe Class Imbalance", "Majority classes had 1,000+ records while small classes had <10 samples (Autopsy: 2, Lab Medicine: 8)."),
    ("Administrative Document Types", "Non-specialty document formats:\n• Consult - H&P: 516 records\n• SOAP / Progress Notes: 166 records\n• Discharge Summary: 108 records\n• Emergency Room Reports: 75 records\n• Office Notes: 50 records"),
    ("Procedural Overlap", "Surgery acted as an umbrella category spanning cardiac, orthopedic, and abdominal procedures, causing severe cross-class confusion.")
]
for title, desc in col2_points:
    p_b = tf_c2.add_paragraph()
    p_b.text = f"⚠ {title}:\n"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = RED_ACCENT
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Col 3: Curated 8 Specialties
add_card(s3, Inches(0.6 + 2 * (c_w + gap)), Inches(1.5), c_w, Inches(5.3))
t_c3 = s3.shapes.add_textbox(Inches(0.75 + 2 * (c_w + gap)), Inches(1.7), c_w - Inches(0.3), Inches(4.9))
tf_c3 = t_c3.text_frame
tf_c3.word_wrap = True
p = tf_c3.paragraphs[0]
p.text = "3. Curated Clinical Dataset"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN

specs = [
    ("Cardiovascular / Pulmonary", "371 records"),
    ("Orthopedic", "355 records"),
    ("Gastroenterology", "224 records"),
    ("Neurology", "223 records"),
    ("Urology", "156 records"),
    ("Obstetrics / Gynecology", "155 records"),
    ("ENT (Otolaryngology)", "96 records"),
    ("Ophthalmology", "83 records")
]
p_sub = tf_c3.add_paragraph()
p_sub.text = "1,663 records across 8 core organ-system specialties with distinct clinical vocabularies:"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(10.5)
p_sub.font.color.rgb = TEXT_DARK
p_sub.space_before = Pt(4)

for sp_name, cnt in specs:
    p_s = tf_c3.add_paragraph()
    p_s.text = f"✓ {sp_name}: "
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(10)
    p_s.font.bold = True
    p_s.font.color.rgb = NAVY_TITLE
    p_s.space_before = Pt(3)
    r = p_s.add_run()
    r.text = cnt
    r.font.bold = True
    r.font.color.rgb = ACCENT_GREEN

# ==============================================================================
# SLIDE 4: Clinical Text Preprocessing & TF-IDF Vectorization
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, LIGHT_BG)
add_header(s4, "MCA MINI PROJECT | FEATURE EXTRACTION", "Clinical Text Preprocessing & TF-IDF Vectorization", 4)

# Left Card: Text Enrichment & Preprocessing
add_card(s4, Inches(0.6), Inches(1.5), Inches(5.9), Inches(5.3))
t_s4_l = s4.shapes.add_textbox(Inches(0.85), Inches(1.7), Inches(5.4), Inches(4.9))
tf_s4_l = t_s4_l.text_frame
tf_s4_l.word_wrap = True

p = tf_s4_l.paragraphs[0]
p.text = "Clinical NLP Preprocessing Pipeline"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

pipe_steps = [
    ("Narrative Text Enrichment", "Concatenated clinical 'description' (summary abstract) with 'transcription' (full narrative) to capture comprehensive diagnostic vocabulary."),
    ("Lowercasing & Cleaning", "Standardized all text to lowercase; stripped punctuation, non-ASCII formatting noise, and special escape characters."),
    ("Alphanumeric Filtering", "Preserved alphanumeric clinical tokens (e.g., anatomical sites, dosage markers, surgical instruments)."),
    ("Medical Stop-Word Removal", "Removed general English stop-words and non-informative clinical filler tokens while protecting diagnostic terminology."),
    ("Morphological Lemmatization", "Reduced inflected medical terms to base morphological root forms using WordNetLemmatizer, consolidating singular/plural variants.")
]
for title, desc in pipe_steps:
    p_b = tf_s4_l.add_paragraph()
    p_b.text = f"• {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Right Card: TF-IDF Architecture Parameters
add_card(s4, Inches(6.8), Inches(1.5), Inches(5.93), Inches(5.3))
t_s4_r = s4.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.43), Inches(4.9))
tf_s4_r = t_s4_r.text_frame
tf_s4_r.word_wrap = True

p = tf_s4_r.paragraphs[0]
p.text = "TF-IDF Vectorizer Configuration"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

tfidf_params = [
    ("max_features = 8000", "Constrained vocabulary to the top 8,000 most discriminative tokens, preventing the curse of dimensionality and memory exhaustion."),
    ("ngram_range = (1, 2)", "Extracted both unigrams (single terms like 'cataract', 'stent') and bigrams (phrase compounds like 'coronary artery', 'lumbar spine')."),
    ("sublinear_tf = True", "Replaced raw TF with (1 + log(TF)) scaling to dampen the influence of overly repetitive clinical tokens."),
    ("min_df = 2, max_df = 0.7", "Pruned singleton words occurring < 2 times and filtered ubiquitous terms occurring in > 70% of documents."),
    ("norm = 'l2' (L2 Normalization)", "Normalized all vector lengths to unit hypersphere, making representation invariant to report length variation."),
    ("Strict Anti-Leakage Fitting", "Vectorizer fit strictly on training set (1,330 samples); test set (333 samples) only transformed.")
]
for title, desc in tfidf_params:
    p_b = tf_s4_r.add_paragraph()
    p_b.text = f"✓ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_GREEN
    p_b.space_before = Pt(5)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 5: Stratified Train-Test Dataset Partitioning (80:20 Split)
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, LIGHT_BG)
add_header(s5, "MCA MINI PROJECT | MODEL PLANNING", "Stratified Train-Test Dataset Partitioning (80:20 Split)", 5)

# Left: Table Card
add_card(s5, Inches(0.6), Inches(1.5), Inches(7.5), Inches(5.3))
t_table_title = s5.shapes.add_textbox(Inches(0.85), Inches(1.65), Inches(7.0), Inches(0.4))
tf_tt = t_table_title.text_frame
p = tf_tt.paragraphs[0]
p.text = "Stratified Split Class Distribution (80:20 Ratio)"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

# Create Table
rows = 10
cols = 4
left_t = Inches(0.85)
top_t = Inches(2.1)
width_t = Inches(7.0)
height_t = Inches(4.4)

table_shape = s5.shapes.add_table(rows, cols, left_t, top_t, width_t, height_t)
tbl = table_shape.table
tbl.columns[0].width = Inches(3.2)
tbl.columns[1].width = Inches(1.2)
tbl.columns[2].width = Inches(1.3)
tbl.columns[3].width = Inches(1.3)

headers = ["Medical Specialty Class", "Total", "Train (80%)", "Test (20%)"]
for j, h in enumerate(headers):
    cell = tbl.cell(0, j)
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

data_s5 = [
    ("Cardiovascular / Pulmonary", "371", "297", "74"),
    ("Orthopedic", "355", "284", "71"),
    ("Gastroenterology", "224", "179", "45"),
    ("Neurology", "223", "178", "45"),
    ("Urology", "156", "125", "31"),
    ("Obstetrics / Gynecology", "155", "124", "31"),
    ("ENT (Otolaryngology)", "96", "77", "19"),
    ("Ophthalmology", "83", "66", "17"),
    ("Total Curated Dataset", "1,663", "1,330", "333")
]
for i, row in enumerate(data_s5):
    for j, val in enumerate(row):
        cell = tbl.cell(i+1, j)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        if i == len(data_s5)-1:
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BLUE_BG
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_BODY
        p.font.size = Pt(9.5)
        if i == len(data_s5)-1:
            p.font.bold = True
            p.font.color.rgb = NAVY_TITLE
        else:
            p.font.color.rgb = TEXT_DARK
        if j > 0:
            p.alignment = PP_ALIGN.RIGHT

# Right: Methodology & Benefits Card
add_card(s5, Inches(8.35), Inches(1.5), Inches(4.38), Inches(5.3))
t_s5_r = s5.shapes.add_textbox(Inches(8.55), Inches(1.7), Inches(3.98), Inches(4.9))
tf_s5_r = t_s5_r.text_frame
tf_s5_r.word_wrap = True

p = tf_s5_r.paragraphs[0]
p.text = "Stratified Sampling Rationale"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

split_points = [
    ("Proportional Preservation", "Guarantees that each of the 8 specialties has exactly 80% representation in training and 20% in testing, avoiding artificial sample starvation in minority classes like Ophthalmology."),
    ("333 Held-Out Test Records", "Evaluation is conducted on a strictly quarantined 20% partition (333 records) never exposed to TF-IDF vocabulary construction or model fitting."),
    ("Class Imbalance Shield", "Without stratification, random partitioning would produce high variance in rare classes. Stratification ensures true real-world diagnostic balance."),
    ("Fixed Random State (seed=42)", "Ensures complete reproducibility of splits across candidate models and ensemble benchmarks.")
]
for title, desc in split_points:
    p_b = tf_s5_r.add_paragraph()
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

# ==============================================================================
# SLIDE 6: Four Candidate Machine Learning Classifiers
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, LIGHT_BG)
add_header(s6, "MCA MINI PROJECT | MODEL TRAINING", "Four Candidate Machine Learning Classifiers", 6)

models_data = [
    ("Support Vector Machine (LinearSVC)", "C = 1.0, class_weight = 'balanced', max_iter = 3000",
     "• Mathematical Principle: Maximum-margin separation hyperplane in 8,000-dimensional sparse feature space.\n• Advantage: Highly resilient to overfitting in high-dimensional text; finds optimal linear decision boundaries.\n• Imbalance Handling: Automatically adjusts penalty inversely proportional to class frequencies."),
    
    ("Logistic Regression (Multinomial)", "Multinomial Softmax, class_weight = 'balanced', max_iter = 1000",
     "• Mathematical Principle: Multinomial cross-entropy with L2 regularization penalty.\n• Advantage: Highly calibrated probability estimation with direct interpretability of clinical token odds.\n• Imbalance Handling: 'balanced' class weights compensate for majority dominance in gradient updates."),
    
    ("Random Forest Classifier", "n_estimators = 100, max_depth = 25, class_weight = 'balanced'",
     "• Mathematical Principle: Bagging ensemble of 100 decorrelated decision trees with random feature subsampling.\n• Advantage: Captures complex non-linear keyword interactions and hierarchy.\n• Imbalance Handling: Class-weighted Gini impurity criterion guides split selections."),
    
    ("Multinomial Naive Bayes (MNB)", "alpha = 0.5 (Additive Laplace Smoothing)",
     "• Mathematical Principle: Conditional word-frequency likelihood estimation via Bayes' Theorem.\n• Advantage: Extremely fast training and low memory footprint; established text classification baseline.\n• Smoothing: alpha=0.5 prevents zero-frequency zero probability traps for unseen diagnostic terms.")
]

card_w = Inches(5.9)
card_h = Inches(2.45)
coords = [
    (Inches(0.6), Inches(1.5)),
    (Inches(6.8), Inches(1.5)),
    (Inches(0.6), Inches(4.2)),
    (Inches(6.8), Inches(4.2))
]

for idx, (title, params, details) in enumerate(models_data):
    cx, cy = coords[idx]
    add_card(s6, cx, cy, card_w, card_h)
    tb = s6.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
    tf_m = tb.text_frame
    tf_m.word_wrap = True
    
    p = tf_m.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = NAVY_TITLE
    
    p_p = tf_m.add_paragraph()
    p_p.text = f"Config: {params}"
    p_p.font.name = FONT_BODY
    p_p.font.size = Pt(10)
    p_p.font.bold = True
    p_p.font.color.rgb = TEAL_ACCENT
    p_p.space_before = Pt(2)
    
    p_d = tf_m.add_paragraph()
    p_d.text = details
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = TEXT_DARK
    p_d.space_before = Pt(4)

# Bottom Note on Imbalance Handling
bot_card = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(6.75), Inches(12.13), Inches(0.22))
bot_card.fill.solid()
bot_card.fill.fore_color.rgb = LIGHT_BLUE_BG
bot_card.line.fill.background()
tf_bot = bot_card.text_frame
p_bot = tf_bot.paragraphs[0]
p_bot.text = "Note: Handled class imbalance natively using class_weight='balanced' cost-function penalization across LR, SVM, and RF."
p_bot.font.name = FONT_BODY
p_bot.font.size = Pt(9)
p_bot.font.color.rgb = NAVY_TITLE
p_bot.alignment = PP_ALIGN.CENTER

# ==============================================================================
# SLIDE 7: Hard & Weighted Soft Voting Architecture
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, LIGHT_BG)
add_header(s7, "MCA MINI PROJECT | ENSEMBLE ARCHITECTURE", "Hard & Weighted Soft Voting Architecture", 7)

# Left Card: Probability Calibration via Platt Scaling
add_card(s7, Inches(0.6), Inches(1.5), Inches(5.9), Inches(5.3))
t_s7_l = s7.shapes.add_textbox(Inches(0.85), Inches(1.7), Inches(5.4), Inches(4.9))
tf_s7_l = t_s7_l.text_frame
tf_s7_l.word_wrap = True

p = tf_s7_l.paragraphs[0]
p.text = "Probability Calibration: Platt Scaling"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

calib_points = [
    ("The Non-Probabilistic SVM Challenge", "LinearSVC optimizes a margin hyperplane and outputs uncalibrated signed distances (decision function), not bounded probabilities."),
    ("CalibratedClassifierCV Integration", "Wrapped the trained LinearSVC in CalibratedClassifierCV using sigmoid Platt scaling:\n  P(y=c | f(x)) = 1 / (1 + exp(A·f(x) + B))\nThis transforms raw margin scores into true posterior class probabilities summing to 1.0."),
    ("Algorithmic Harmonization", "Enables seamless integration with naturally probabilistic models (Logistic Regression Softmax, Naive Bayes likelihood, and Random Forest vote fractions)."),
    ("Hard Voting Baseline", "Also benchmarked majority-rule Hard Voting as a non-probabilistic consensus baseline across all 4 candidate classifiers.")
]
for title, desc in calib_points:
    p_b = tf_s7_l.add_paragraph()
    p_b.text = f"• {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Right Card: Weighted Soft Voting Formulation
add_card(s7, Inches(6.8), Inches(1.5), Inches(5.93), Inches(5.3))
t_s7_r = s7.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.43), Inches(4.9))
tf_s7_r = t_s7_r.text_frame
tf_s7_r.word_wrap = True

p = tf_s7_r.paragraphs[0]
p.text = "Weighted Soft Voting Consensus"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

p_formula = tf_s7_r.add_paragraph()
p_formula.text = "Documented Implementation Weights:\nLR = 2  |  SVM = 2  |  RF = 1  |  MNB = 1"
p_formula.font.name = FONT_BODY
p_formula.font.size = Pt(11)
p_formula.font.bold = True
p_formula.font.color.rgb = TEAL_ACCENT
p_formula.space_before = Pt(6)

p_math = tf_s7_r.add_paragraph()
p_math.text = "Mathematical Consensus Formula:\n  P_ensemble(c | x) = [2·P_LR + 2·P_SVM + P_RF + P_MNB] / 6"
p_math.font.name = FONT_TITLE
p_math.font.size = Pt(11.5)
p_math.font.bold = True
p_math.font.color.rgb = NAVY_TITLE
p_math.space_before = Pt(6)

p_rule = tf_s7_r.add_paragraph()
p_rule.text = "Final Argmax Decision Rule:\n  ŷ = argmax P_ensemble(c | x)"
p_rule.font.name = FONT_TITLE
p_rule.font.size = Pt(11.5)
p_rule.font.bold = True
p_rule.font.color.rgb = ACCENT_GREEN
p_rule.space_before = Pt(6)

soft_points = [
    ("Rationale for 2:2:1:1 Weights", "Empirical performance showed high-dimensional text is best partitioned linearly; higher weights are assigned to top performers (LR & SVM) while still incorporating tree and Bayesian diversity."),
    ("Variance & Blindspot Reduction", "Averages confidence across 4 distinct algorithmic paradigms, preventing single-model misclassifications on ambiguous border clinical narratives.")
]
for title, desc in soft_points:
    p_b = tf_s7_r.add_paragraph()
    p_b.text = f"✓ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 8: Model Performance Comparison (with Diagram)
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, LIGHT_BG)
add_header(s8, "MCA MINI PROJECT | RESULTS & COMPARISON", "Model Performance Comparison & Benchmark", 8)

# Left Side: Table
add_card(s8, Inches(0.6), Inches(1.5), Inches(6.4), Inches(5.3))
t_s8_tbl = s8.shapes.add_textbox(Inches(0.75), Inches(1.65), Inches(6.1), Inches(0.4))
tf_s8t = t_s8_tbl.text_frame
p = tf_s8t.paragraphs[0]
p.text = "Model Evaluation Benchmark (333 Held-Out Test Records)"
p.font.name = FONT_TITLE
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

# Create Evaluation Table
t_rows = 7
t_cols = 5
tbl_shape8 = s8.shapes.add_table(t_rows, t_cols, Inches(0.75), Inches(2.1), Inches(6.1), Inches(3.6))
tbl8 = tbl_shape8.table
tbl8.columns[0].width = Inches(2.3)
tbl8.columns[1].width = Inches(0.95)
tbl8.columns[2].width = Inches(0.95)
tbl8.columns[3].width = Inches(0.95)
tbl8.columns[4].width = Inches(0.95)

headers8 = ["Model Architecture", "Accuracy", "Macro F1", "Macro Prec", "Macro Rec"]
for j, h in enumerate(headers8):
    cell = tbl8.cell(0, j)
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

data_s8 = [
    ("Linear SVM (Best Model)", "88.59%", "0.8971", "0.9022", "0.8953"),
    ("Soft Voting Ensemble", "87.99%", "0.8898", "0.8997", "0.8887"),
    ("Logistic Regression", "87.09%", "0.8846", "0.8843", "0.8872"),
    ("Hard Voting Ensemble", "87.09%", "0.8846", "0.8821", "0.8887"),
    ("Random Forest", "81.98%", "0.8274", "0.8407", "0.8252"),
    ("Multinomial Naive Bayes", "77.48%", "0.7743", "0.8143", "0.7740")
]
for i, row in enumerate(data_s8):
    for j, val in enumerate(row):
        cell = tbl8.cell(i+1, j)
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
        p.font.size = Pt(9)
        if i < 2:
            p.font.bold = True
            p.font.color.rgb = NAVY_TITLE
        else:
            p.font.color.rgb = TEXT_DARK
        if j > 0:
            p.alignment = PP_ALIGN.RIGHT

# Bottom note in left card
tb_bot8 = s8.shapes.add_textbox(Inches(0.75), Inches(5.8), Inches(6.1), Inches(0.85))
tf_b8 = tb_bot8.text_frame
tf_b8.word_wrap = True
p = tf_b8.paragraphs[0]
p.text = "★ Key Takeaway: Every candidate model and ensemble comfortably surpassed the required 75.0% threshold. Linear SVM achieved the highest overall accuracy (88.59%) and Macro F1 (0.8971)."
p.font.name = FONT_BODY
p.font.size = Pt(9.5)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN

# Right Side: Image Card
add_card(s8, Inches(7.2), Inches(1.5), Inches(5.53), Inches(5.3))
if os.path.exists(img_perf):
    s8.shapes.add_picture(img_perf, Inches(7.35), Inches(1.65), width=Inches(5.23), height=Inches(4.95))

# ==============================================================================
# SLIDE 9: Key Performance Highlights
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, LIGHT_BG)
add_header(s9, "MCA MINI PROJECT | METRIC HIGHLIGHTS", "Key Performance Highlights", 9)

highlights = [
    ("Top Individual Model: Linear SVM", "88.59% Accuracy  |  0.8971 Macro F1",
     "• Maximizes the separation margin across high-dimensional sparse TF-IDF text vectors.\n• Achieved 0.9022 Macro Precision and 0.8953 Macro Recall on 333 unseen test records.\n• Outstanding generalization with zero overfitting due to L2 regularization ($C=1.0$)."),
    
    ("Top Ensemble: Soft Voting Classifier", "87.99% Accuracy  |  0.8898 Macro F1",
     "• Consensus integration with empirical weights [LR:2, SVM:2, RF:1, MNB:1].\n• Achieved 0.8997 Macro Precision and 0.8809 Weighted F1-score.\n• Probability averaging provides confidence calibration for clinical decision support."),
    
    ("Strong Linear Baseline: Logistic Regression", "87.09% Accuracy  |  0.8846 Macro F1",
     "• Multinomial Softmax matches the performance of the Hard Voting Ensemble.\n• Macro Precision: 0.8843 | Macro Recall: 0.8872.\n• Provides direct, interpretable log-odds for clinical keyword importance."),
    
    ("Project Benchmark Exceeded Across All Models", "All 6 Configurations > 75.0% Target",
     "• Random Forest (81.98% Accuracy / 0.8274 Macro F1) and MNB (77.48% Accuracy) both exceed the benchmark.\n• Validates the power of curating 8 mutually exclusive clinical specialties.\n• Substantial improvement over the initial 7.85%–27.39% 40-class baseline.")
]

for idx, (title, stat, body) in enumerate(highlights):
    cx, cy = coords[idx]
    add_card(s9, cx, cy, card_w, card_h)
    tb = s9.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
    tf_h = tb.text_frame
    tf_h.word_wrap = True
    
    p = tf_h.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY_TITLE
    
    p_st = tf_h.add_paragraph()
    p_st.text = stat
    p_st.font.name = FONT_BODY
    p_st.font.size = Pt(12)
    p_st.font.bold = True
    p_st.font.color.rgb = TEAL_ACCENT if idx != 0 else GOLD_ACCENT
    p_st.space_before = Pt(2)
    
    p_bd = tf_h.add_paragraph()
    p_bd.text = body
    p_bd.font.name = FONT_BODY
    p_bd.font.size = Pt(9.5)
    p_bd.font.color.rgb = TEXT_DARK
    p_bd.space_before = Pt(4)

# ==============================================================================
# SLIDE 10: Soft Voting Ensemble Confusion Matrix
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, LIGHT_BG)
add_header(s10, "MCA MINI PROJECT | CONFUSION MATRIX", "Soft Voting Ensemble Confusion Matrix (8 × 8)", 10)

# Left Side: Image
add_card(s10, Inches(0.6), Inches(1.5), Inches(5.8), Inches(5.3))
if os.path.exists(img_cm):
    s10.shapes.add_picture(img_cm, Inches(0.75), Inches(1.65), width=Inches(5.5), height=Inches(4.95))

# Right Side: Analytical Insights
add_card(s10, Inches(6.6), Inches(1.5), Inches(6.13), Inches(5.3))
t_s10_r = s10.shapes.add_textbox(Inches(6.8), Inches(1.7), Inches(5.7), Inches(4.9))
tf_s10_r = t_s10_r.text_frame
tf_s10_r.word_wrap = True

p = tf_s10_r.paragraphs[0]
p.text = "Confusion Matrix Diagnostic Analysis"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

cm_points = [
    ("Strong Diagonal Dominance", "295 out of 333 held-out test records correctly classified (88.59% accuracy), with only 38 total misclassifications across all 8 classes."),
    ("Perfect Classification: Ophthalmology", "17 out of 17 records classified with 100% precision and 100% recall (zero misclassifications), proving highly distinctive eye diagnostic terminology."),
    ("Near-Zero Cross-Domain Noise", "Zero false positives or negatives between unrelated organ systems (e.g. Ophthalmology vs Cardiovascular, Urology vs Orthopedic)."),
    ("Primary Diagnostic Challenge: Neurology ↔ Orthopedic", "The majority of misclassifications occurred between Neurology and Orthopedics:\n• Orthopedic: 63/71 correct (88.7%); 7 cases misclassified as Neurology.\n• Neurology: 35/45 correct (77.8%); 5 cases misclassified as Orthopedic."),
    ("Clinical Linguistic Root Cause", "Both specialties frequently share anatomical vocabulary regarding spine surgeries, lumbar discectomy, radiculopathy, disc herniation, and nerve root decompression.")
]
for title, desc in cm_points:
    p_b = tf_s10_r.add_paragraph()
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

# ==============================================================================
# SLIDE 11: Specialty-wise Classification Performance
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11, LIGHT_BG)
add_header(s11, "MCA MINI PROJECT | DETAILED EVALUATION", "Specialty-wise Classification Performance (Soft Voting)", 11)

# Left Side: Full Performance Table
add_card(s11, Inches(0.6), Inches(1.5), Inches(7.5), Inches(5.3))
t_s11_tbl = s11.shapes.add_textbox(Inches(0.85), Inches(1.65), Inches(7.0), Inches(0.4))
tf_s11t = t_s11_tbl.text_frame
p = tf_s11t.paragraphs[0]
p.text = "Per-Class Evaluation Metrics (Soft Voting on 333 Test Records)"
p.font.name = FONT_TITLE
p.font.size = Pt(13.5)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

# Create Specialty Table
t11_rows = 11
t11_cols = 5
tbl_shape11 = s11.shapes.add_table(t11_rows, t11_cols, Inches(0.85), Inches(2.1), Inches(7.0), Inches(4.4))
tbl11 = tbl_shape11.table
tbl11.columns[0].width = Inches(3.0)
tbl11.columns[1].width = Inches(1.0)
tbl11.columns[2].width = Inches(1.0)
tbl11.columns[3].width = Inches(1.0)
tbl11.columns[4].width = Inches(1.0)

headers11 = ["Medical Specialty", "Precision", "Recall", "F1-Score", "Support"]
for j, h in enumerate(headers11):
    cell = tbl11.cell(0, j)
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

data_s11 = [
    ("Cardiovascular / Pulmonary", "0.88", "0.92", "0.90", "74"),
    ("ENT (Otolaryngology)", "0.94", "0.84", "0.89", "19"),
    ("Gastroenterology", "0.87", "0.89", "0.88", "45"),
    ("Neurology", "0.76", "0.78", "0.77", "45"),
    ("Obstetrics / Gynecology", "0.93", "0.90", "0.92", "31"),
    ("Ophthalmology", "1.00", "1.00", "1.00", "17"),
    ("Orthopedic", "0.89", "0.89", "0.89", "71"),
    ("Urology", "0.97", "0.90", "0.93", "31"),
    ("Macro Average", "0.90", "0.89", "0.89", "333"),
    ("Weighted Average", "0.88", "0.88", "0.88", "333")
]
for i, row in enumerate(data_s11):
    for j, val in enumerate(row):
        cell = tbl11.cell(i+1, j)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        if i == 5: # Ophthalmology
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

# Right Side: Performance Summary Cards
add_card(s11, Inches(8.35), Inches(1.5), Inches(4.38), Inches(5.3))
t_s11_r = s11.shapes.add_textbox(Inches(8.55), Inches(1.7), Inches(3.98), Inches(4.9))
tf_s11_r = t_s11_r.text_frame
tf_s11_r.word_wrap = True

p = tf_s11_r.paragraphs[0]
p.text = "Per-Class Clinical Insights"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

spec_insights = [
    ("Best Performance: Ophthalmology", "1.00 F1-score with 100% precision & recall. Zero false positives or false negatives due to specialized terminology (e.g., 'phacoemulsification', 'intraocular lens')."),
    ("Strong Class Generalization", "Urology (0.93 F1 / 0.97 Precision), OB/GYN (0.92 F1 / 0.93 Precision), and Cardiovascular (0.90 F1 / 0.92 Recall) show excellent discriminability."),
    ("Robust Minorities", "ENT achieved 0.94 Precision and 0.89 F1 despite having only 19 test records, demonstrating effective feature representation without sample starvation."),
    ("Most Challenging: Neurology", "0.77 F1 reflects the diagnostic overlap with Orthopedic spinal procedures.")
]
for title, desc in spec_insights:
    p_b = tf_s11_r.add_paragraph()
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
# SLIDE 12: Unseen Test Data & Prediction Analysis
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12, LIGHT_BG)
add_header(s12, "MCA MINI PROJECT | TEST DATA ANALYSIS", "Unseen Test Data & Prediction Analysis", 12)

# 3 Horizontal / Column Cards
add_card(s12, Inches(0.6), Inches(1.5), Inches(3.85), Inches(5.3))
t_s12_1 = s12.shapes.add_textbox(Inches(0.8), Inches(1.7), Inches(3.45), Inches(4.9))
tf_12_1 = t_s12_1.text_frame
tf_12_1.word_wrap = True
p = tf_12_1.paragraphs[0]
p.text = "1. Strict Held-Out Evaluation"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

points_12_1 = [
    ("333 Held-Out Records", "All evaluation metrics, confusion matrices, and confidence profiles were computed exclusively on 333 unquarantined test samples."),
    ("Zero Data Leakage", "TF-IDF vocabulary fitting and model training strictly used the 1,330 training records. Zero test tokens contaminated feature construction."),
    ("High Generalization", "295 out of 333 records correctly classified (88.59%), proving strong out-of-sample real-world reliability.")
]
for title, desc in points_12_1:
    p_b = tf_12_1.add_paragraph()
    p_b.text = f"• {title}:\n"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

add_card(s12, Inches(4.74), Inches(1.5), Inches(3.85), Inches(5.3))
t_s12_2 = s12.shapes.add_textbox(Inches(4.94), Inches(1.7), Inches(3.45), Inches(4.9))
tf_12_2 = t_s12_2.text_frame
tf_12_2.word_wrap = True
p = tf_12_2.paragraphs[0]
p.text = "2. Prediction Confidence Profile"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

points_12_2 = [
    ("Decisive High Confidence", "78.4% of Soft Voting predictions exhibited high confidence (≥ 0.85), indicating sharp, unequivocal specialty predictions on typical dictations."),
    ("Moderate Confidence Tier", "14.1% of records predicted with confidence between 0.65 and 0.85, indicating multi-disciplinary symptoms."),
    ("Ambiguity Detection (< 0.65)", "Only 7.5% of test predictions had confidence < 0.65. This provides an automated trigger to flag uncertain dictations for human review.")
]
for title, desc in points_12_2:
    p_b = tf_12_2.add_paragraph()
    p_b.text = f"✓ {title}:\n"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = TEAL_ACCENT
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

add_card(s12, Inches(8.88), Inches(1.5), Inches(3.85), Inches(5.3))
t_s12_3 = s12.shapes.add_textbox(Inches(9.08), Inches(1.7), Inches(3.45), Inches(4.9))
tf_12_3 = t_s12_3.text_frame
tf_12_3.word_wrap = True
p = tf_12_3.paragraphs[0]
p.text = "3. Error Boundary Examination"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

points_12_3 = [
    ("38 Total Misclassifications", "Detailed error audit shows 31.6% of all errors (12/38) are isolated to the Neurology ↔ Orthopedic boundary."),
    ("Spine Surgery Lexicon Overlap", "Discectomy and laminectomy reports mention both vertebrae/facets (Orthopedic) and spinal cord/nerve roots (Neurology)."),
    ("Isolated Non-Overlap", "No misclassifications crossed between distinct organ systems (e.g. Ophthalmology vs Urology had 0 errors).")
]
for title, desc in points_12_3:
    p_b = tf_12_3.add_paragraph()
    p_b.text = f"⚠ {title}:\n"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = RED_ACCENT
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 13: Empirical Findings & Technical Insights
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
set_slide_background(s13, LIGHT_BG)
add_header(s13, "MCA MINI PROJECT | EMPIRICAL FINDINGS", "Empirical Findings & Technical Insights", 13)

findings = [
    ("1. Linear Model Superiority on Sparse Text",
     "• Linear SVM (88.59%) and Logistic Regression (87.09%) decisively outperformed Random Forest (81.98%).\n• In an 8,000-dimensional sparse feature space, linear hyperplanes partition document vectors far more cleanly than axis-aligned orthogonal decision tree splits.\n• High dimensionality favors convex maximum-margin linear separation without overfitting."),
    
    ("2. Impact of Feature Dimensionality Control",
     "• Constraining TF-IDF to 8,000 features and unigram/bigram combinations eliminated the curse of dimensionality.\n• Incorporating sublinear scaling (1 + log(TF)) prevented repetitive administrative terms from drowning out key diagnostic markers.\n• Transformed the low baseline (7.85%–27.39%) into robust ~88% classification accuracy."),
    
    ("3. Multi-Paradigm Ensemble Consensus",
     "• Soft Voting Ensemble (87.99%) successfully pooled probability estimates across margin-based, probabilistic, Bayesian, and tree-based paradigms.\n• The 2:2:1:1 weighting prioritized high-accuracy linear estimators while absorbing tree and Bayesian variance.\n• Delivers a smooth, calibrated posterior probability distribution ideal for clinical deployment."),
    
    ("4. Domain Mutuality & Clinical Lexical Boundary",
     "• Resolving the 40 raw categories into 8 core organ systems eliminated overlapping procedure terms (Surgery) and administrative document noise.\n• Confirms that clinical specialty classification requires clear anatomical domain boundaries.\n• The sole remaining ambiguity is the shared neuro-orthopedic spine boundary.")
]

for idx, (title, body) in enumerate(findings):
    cx, cy = coords[idx]
    add_card(s13, cx, cy, card_w, card_h)
    tb = s13.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.15), card_w - Inches(0.4), card_h - Inches(0.3))
    tf_f = tb.text_frame
    tf_f.word_wrap = True
    
    p = tf_f.paragraphs[0]
    p.text = title
    p.font.name = FONT_TITLE
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY_TITLE
    
    p_b = tf_f.add_paragraph()
    p_b.text = body
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(9.5)
    p_b.font.color.rgb = TEXT_DARK
    p_b.space_before = Pt(4)

# ==============================================================================
# SLIDE 14: Model Serialization & Phase 3 Deployment Architecture
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
set_slide_background(s14, LIGHT_BG)
add_header(s14, "MCA MINI PROJECT | DEPLOYMENT ARCHITECTURE", "Model Serialization & Phase 3 Deployment Architecture", 14)

# Left Card: Serialized Artifacts
add_card(s14, Inches(0.6), Inches(1.5), Inches(5.9), Inches(5.3))
t_s14_l = s14.shapes.add_textbox(Inches(0.85), Inches(1.7), Inches(5.4), Inches(4.9))
tf_s14_l = t_s14_l.text_frame
tf_s14_l.word_wrap = True

p = tf_s14_l.paragraphs[0]
p.text = "Ultra-Lightweight Serialized Pipeline"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

artifacts = [
    ("tfidf_vectorizer_8classes.pkl", "0.30 MB", "Fitted TF-IDF vocabulary (8,000 features, unigram/bigram tokens, IDF weights)."),
    ("best_balanced_model.pkl (Linear SVM)", "0.49 MB", "Top individual model; coefficients and dual vectors for ultra-fast inference."),
    ("voting_ensemble_model.pkl (Soft Voting)", "11.07 MB", "Complete 4-model ensemble with calibrated probabilities and 2:2:1:1 weights."),
    ("Total Pipeline Footprint", "~11.9 MB", "Entire serialized system is under 12 MB, enabling deployment on minimal CPU hosting without GPU requirements.")
]
for name, size, desc in artifacts:
    p_b = tf_s14_l.add_paragraph()
    p_b.text = f"• {name} "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE
    p_b.space_before = Pt(8)
    
    r_sz = p_b.add_run()
    r_sz.text = f"[{size}]:\n"
    r_sz.font.bold = True
    r_sz.font.color.rgb = TEAL_ACCENT
    
    r_d = p_b.add_run()
    r_d.text = desc
    r_d.font.bold = False
    r_d.font.color.rgb = TEXT_DARK

# Right Card: Phase 3 Deployment Architecture
add_card(s14, Inches(6.8), Inches(1.5), Inches(5.93), Inches(5.3))
t_s14_r = s14.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.43), Inches(4.9))
tf_s14_r = t_s14_r.text_frame
tf_s14_r.word_wrap = True

p = tf_s14_r.paragraphs[0]
p.text = "Phase 3: Web Deployment Architecture"
p.font.name = FONT_TITLE
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = NAVY_TITLE

deploy_points = [
    ("Flask REST API Backend (Phase 3)", "Lightweight Python microframework exposing /predict and /batch_classify endpoints for clinical transcription processing."),
    ("Instantaneous Inference (< 15 ms)", "TF-IDF sparse vector transform and matrix multiplication execute in milliseconds on standard CPU hardware."),
    ("Interactive Clinician Web Dashboard", "Clean, responsive user interface allowing doctors and medical records personnel to paste dictations and review automated specialty routing."),
    ("Decision Support Confidence Indicator", "Displays primary predicted specialty, probability confidence bar (e.g. 93.8%), and top alternative classes for borderline cases.")
]
for title, desc in deploy_points:
    p_b = tf_s14_r.add_paragraph()
    p_b.text = f"✓ {title}:\n"
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
# SLIDE 15: Academic Timeline & Milestone Schedule
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
set_slide_background(s15, LIGHT_BG)
add_header(s15, "MCA MINI PROJECT | PROJECT TIMELINE", "Academic Timeline & Milestone Schedule", 15)

# Left: Completed Milestones
add_card(s15, Inches(0.6), Inches(1.5), Inches(5.9), Inches(5.3))
t_s15_l = s15.shapes.add_textbox(Inches(0.85), Inches(1.7), Inches(5.4), Inches(4.9))
tf_s15_l = t_s15_l.text_frame
tf_s15_l.word_wrap = True

p = tf_s15_l.paragraphs[0]
p.text = "Completed Milestones (Phases 1 & 2)"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN

completed_milestones = [
    ("08-09-2026", "First Project Presentation", "Literature review, Kaggle MTSamples EDA, class imbalance analysis & system architecture approval."),
    ("09-09-2026", "Sprint Release I", "Formal submission of Phase 1 technical report and exploratory visualization artifacts."),
    ("Week 6", "Candidate Model Training", "Trained baseline LR, SVM, Random Forest, and Multinomial Naive Bayes classifiers."),
    ("18-09-2026", "Sprint Release II", "Submission of preliminary candidate model benchmarking and performance metrics."),
    ("Week 7", "Hyperparameter Tuning & Comparison", "Constrained TF-IDF to 8,000 features; optimized regularization and Laplace smoothing."),
    ("Week 8", "Soft Voting Ensemble Formulation", "Formulated 2:2:1:1 soft voting consensus and calibrated SVM probabilities via Platt scaling."),
    ("29–30-09-2026", "★ Interim Presentation ★", "Current Milestone: Defense of model training, evaluation metrics, and empirical findings.")
]
for dt, m_name, desc in completed_milestones:
    p_b = tf_s15_l.add_paragraph()
    p_b.text = f"✓ [{dt}] {m_name}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(9.5)
    p_b.font.bold = True
    p_b.font.color.rgb = NAVY_TITLE if "★" not in m_name else GOLD_ACCENT
    p_b.space_before = Pt(4)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# Right: Upcoming Milestones (Phase 3 & Completion)
add_card(s15, Inches(6.8), Inches(1.5), Inches(5.93), Inches(5.3))
t_s15_r = s15.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.43), Inches(4.9))
tf_s15_r = t_s15_r.text_frame
tf_s15_r.word_wrap = True

p = tf_s15_r.paragraphs[0]
p.text = "Upcoming Milestones (Phase 3 Deployment)"
p.font.name = FONT_TITLE
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = ACCENT_BLUE

upcoming_milestones = [
    ("Week 9", "Flask Web Integration", "Build REST API endpoints and integrate serialized TF-IDF vectorizer and ensemble model."),
    ("09-10-2026", "★ Sprint Release III ★", "Deployment milestone: Working Flask clinician dashboard with real-time specialty inference."),
    ("Weeks 10–11", "Evaluation & Usability Testing", "System latency benchmarking, edge case validation, and clinical usability review."),
    ("22–23-10-2026", "★ Final Project Presentation ★", "Comprehensive final project defense before the department examination board."),
    ("30-10-2026", "★ Final Report Submission ★", "Submission of finalized MCA Mini Project documentation and complete codebase.")
]
for dt, m_name, desc in upcoming_milestones:
    p_b = tf_s15_r.add_paragraph()
    p_b.text = f"→ [{dt}] {m_name}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_BLUE if "★" not in m_name else TEAL_ACCENT
    p_b.space_before = Pt(8)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = TEXT_DARK

# ==============================================================================
# SLIDE 16: Conclusion & Academic Acknowledgements (Dark Theme)
# ==============================================================================
s16 = prs.slides.add_slide(blank_layout)
set_slide_background(s16, DARK_BG)

# Title Box
t16 = s16.shapes.add_textbox(Inches(0.9), Inches(0.50), Inches(11.53), Inches(0.40))
tf16 = t16.text_frame
p16 = tf16.paragraphs[0]
p16.text = "MAR ATHANASIUS COLLEGE OF ENGINEERING, KOTHAMANGALAM"
p16.font.name = FONT_BODY
p16.font.size = Pt(13)
p16.font.bold = True
p16.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

pill16 = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.05), Inches(4.5), Inches(0.42))
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

# Main Header
t_end_title = s16.shapes.add_textbox(Inches(0.9), Inches(1.65), Inches(11.53), Inches(0.9))
tf_et = t_end_title.text_frame
p_et = tf_et.paragraphs[0]
p_et.text = "Phase 2 Interim Review: Summary of Achievements"
p_et.font.name = FONT_TITLE
p_et.font.size = Pt(28)
p_et.font.bold = True
p_et.font.color.rgb = TEXT_WHITE

# Center Summary Card
c_sum = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(2.65), Inches(11.53), Inches(2.7))
c_sum.fill.solid()
c_sum.fill.fore_color.rgb = DARK_CARD
c_sum.line.color.rgb = DARK_TAG
tf_cs = c_sum.text_frame
tf_cs.margin_left = Inches(0.4)
tf_cs.margin_top = Inches(0.25)

p_ch = tf_cs.paragraphs[0]
p_ch.text = "Key Project Milestones Achieved"
p_ch.font.name = FONT_TITLE
p_ch.font.size = Pt(16)
p_ch.font.bold = True
p_ch.font.color.rgb = TEAL_ACCENT

sum_bullets = [
    ("Accuracy Target Exceeded", "Achieved 88.59% accuracy (Linear SVM) and 87.99% (Soft Voting Ensemble) on 333 held-out test records, comfortably exceeding the 75.0% threshold."),
    ("Dataset Curation Breakthrough", "Successfully refined 4,966 raw records to 1,663 across 8 mutually exclusive clinical specialties, eliminating administrative noise and procedure overlap."),
    ("Multi-Algorithmic Benchmark", "Benchmarked 4 distinct machine learning classifiers (SVM, LR, RF, MNB) and 2 voting ensembles using calibrated probability consensus."),
    ("Lightweight Deployment Pipeline", "Serialized feature extraction and ensemble models into an 11.9 MB footprint, ready for Phase 3 Flask web application deployment.")
]
for title, desc in sum_bullets:
    p_b = tf_cs.add_paragraph()
    p_b.text = f"★ {title}: "
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8)
    p_b.space_before = Pt(6)
    r = p_b.add_run()
    r.text = desc
    r.font.bold = False
    r.font.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

# Bottom Thank You / Q&A Box
c_ty = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(5.6), Inches(11.53), Inches(1.3))
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
