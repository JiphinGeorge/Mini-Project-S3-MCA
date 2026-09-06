import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# COLOR PALETTE & DESIGN SYSTEM
# ==============================================================================
NAVY = RGBColor(15, 23, 42)          # #0F172A - Major Headings
DARK_BLUE = RGBColor(30, 41, 59)     # #1E293B - Card Titles & Dark Text
PRIMARY_BLUE = RGBColor(29, 78, 216) # #1D4ED8 - Primary Accent
ACCENT_BLUE = RGBColor(37, 99, 235)  # #2563EB - Highlights & Buttons
TEAL = RGBColor(13, 148, 136)        # #0D9488 - Data Science / ML Accent
DARK_TEAL = RGBColor(15, 118, 110)   # #0F766E - Deep Teal
PURPLE = RGBColor(124, 58, 237)      # #7C3AED - Ensemble Learning Accent
CYAN = RGBColor(6, 182, 212)         # #06B6D4 - Light Accent
SLATE_BODY = RGBColor(51, 65, 85)    # #334155 - Body Text
SLATE_MUTED = RGBColor(100, 116, 139)# #64748B - Headers, Footers, Subtitles
CARD_BG = RGBColor(248, 250, 252)    # #F8FAFC - Card Background
CARD_BORDER = RGBColor(226, 232, 240)# #E2E8F0 - Card Borders
WHITE = RGBColor(255, 255, 255)
GREEN = RGBColor(16, 185, 129)       # #10B981 - Completed Checkmarks
AMBER = RGBColor(217, 119, 6)        # #D97706 - Warning / Imbalance

FONT_HEADING = 'Calibri'
FONT_BODY = 'Calibri'

HEADER_TEXT = "Medical Specialty Classification using TF-IDF and Ensemble Machine Learning"
FOOTER_TEXT = "Department of Computer Applications | MACE"

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================
def create_deck():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_header_footer(slide, title_text, category_badge, slide_num, total_slides=15):
    # Category badge
    tb_badge = slide.shapes.add_textbox(Inches(0.8), Inches(0.28), Inches(6.0), Inches(0.3))
    tf_b = tb_badge.text_frame
    tf_b.word_wrap = False
    tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
    p_b = tf_b.paragraphs[0]
    p_b.text = f"MCA MINI PROJECT  |  {category_badge.upper()}"
    p_b.font.name = FONT_HEADING
    p_b.font.size = Pt(9.5)
    p_b.font.bold = True
    p_b.font.color.rgb = TEAL

    # Header text on top right
    tb_hdr = slide.shapes.add_textbox(Inches(5.5), Inches(0.28), Inches(7.033), Inches(0.3))
    tf_h = tb_hdr.text_frame
    tf_h.word_wrap = False
    tf_h.margin_left = tf_h.margin_top = tf_h.margin_right = tf_h.margin_bottom = 0
    p_h = tf_h.paragraphs[0]
    p_h.alignment = PP_ALIGN.RIGHT
    p_h.text = HEADER_TEXT
    p_h.font.name = FONT_BODY
    p_h.font.size = Pt(9.0)
    p_h.font.color.rgb = SLATE_MUTED

    # Slide Title
    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.733), Inches(0.5))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(21)
    p_t.font.bold = True
    p_t.font.color.rgb = NAVY

    # Header horizontal dividing line
    line_h = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.10), Inches(11.733), Inches(0.015))
    line_h.fill.solid()
    line_h.fill.fore_color.rgb = CARD_BORDER
    line_h.line.color.rgb = CARD_BORDER

    # Footer horizontal dividing line
    line_f = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.95), Inches(11.733), Inches(0.015))
    line_f.fill.solid()
    line_f.fill.fore_color.rgb = CARD_BORDER
    line_f.line.color.rgb = CARD_BORDER

    # Footer Left: Department
    tb_fl = slide.shapes.add_textbox(Inches(0.8), Inches(7.02), Inches(6.0), Inches(0.3))
    tf_fl = tb_fl.text_frame
    tf_fl.margin_left = tf_fl.margin_top = tf_fl.margin_right = tf_fl.margin_bottom = 0
    p_fl = tf_fl.paragraphs[0]
    p_fl.text = FOOTER_TEXT
    p_fl.font.name = FONT_BODY
    p_fl.font.size = Pt(9.5)
    p_fl.font.color.rgb = SLATE_MUTED

    # Footer Center: College
    tb_fc = slide.shapes.add_textbox(Inches(4.5), Inches(7.02), Inches(4.5), Inches(0.3))
    tf_fc = tb_fc.text_frame
    tf_fc.margin_left = tf_fc.margin_top = tf_fc.margin_right = tf_fc.margin_bottom = 0
    p_fc = tf_fc.paragraphs[0]
    p_fc.alignment = PP_ALIGN.CENTER
    p_fc.text = "Mar Athanasius College of Engineering, Kothamangalam"
    p_fc.font.name = FONT_BODY
    p_fc.font.size = Pt(9.0)
    p_fc.font.color.rgb = SLATE_MUTED

    # Footer Right: Slide Number
    tb_fr = slide.shapes.add_textbox(Inches(9.533), Inches(7.02), Inches(3.0), Inches(0.3))
    tf_fr = tb_fr.text_frame
    tf_fr.margin_left = tf_fr.margin_top = tf_fr.margin_right = tf_fr.margin_bottom = 0
    p_fr = tf_fr.paragraphs[0]
    p_fr.alignment = PP_ALIGN.RIGHT
    p_fr.text = f"Slide {slide_num} of {total_slides}"
    p_fr.font.name = FONT_BODY
    p_fr.font.size = Pt(9.5)
    p_fr.font.bold = True
    p_fr.font.color.rgb = PRIMARY_BLUE

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER, border_width=1.0):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(border_width)
    return shape

# ==============================================================================
# SLIDE BUILDERS
# ==============================================================================

def build_slide_1(prs):
    """SLIDE 1: TITLE SLIDE"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Elegant Left Accent Bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(0.2), Inches(5.9))
    bar.fill.solid()
    bar.fill.fore_color.rgb = PRIMARY_BLUE
    bar.line.fill.background()

    # Super-title / College
    tb_inst = slide.shapes.add_textbox(Inches(1.25), Inches(0.85), Inches(11.0), Inches(0.4))
    tf_i = tb_inst.text_frame
    tf_i.margin_left = tf_i.margin_top = tf_i.margin_right = tf_i.margin_bottom = 0
    p_i = tf_i.paragraphs[0]
    p_i.text = "MAR ATHANASIUS COLLEGE OF ENGINEERING, KOTHAMANGALAM"
    p_i.font.name = FONT_HEADING
    p_i.font.size = Pt(11)
    p_i.font.bold = True
    p_i.font.color.rgb = TEAL

    # Department
    tb_dept = slide.shapes.add_textbox(Inches(1.25), Inches(1.15), Inches(11.0), Inches(0.35))
    tf_d = tb_dept.text_frame
    tf_d.margin_left = tf_d.margin_top = tf_d.margin_right = tf_d.margin_bottom = 0
    p_d = tf_d.paragraphs[0]
    p_d.text = "Department of Computer Applications  |  MCA Mini Project (Semester 3)"
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11)
    p_d.font.color.rgb = SLATE_MUTED

    # Project Title
    tb_title = slide.shapes.add_textbox(Inches(1.25), Inches(1.75), Inches(11.2), Inches(1.4))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = "Medical Specialty Classification using TF-IDF and Ensemble Machine Learning"
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(28)
    p_t.font.bold = True
    p_t.font.color.rgb = NAVY

    # Subtitle Badge
    tb_sub = slide.shapes.add_textbox(Inches(1.25), Inches(3.25), Inches(11.0), Inches(0.45))
    tf_s = tb_sub.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
    p_s = tf_s.paragraphs[0]
    p_s.text = "FIRST PROJECT PRESENTATION — SPRINT RELEASE I"
    p_s.font.name = FONT_HEADING
    p_s.font.size = Pt(14)
    p_s.font.bold = True
    p_s.font.color.rgb = ACCENT_BLUE

    # Domain Badges
    badges = ["Clinical NLP", "TF-IDF Vectorization", "Supervised ML", "Soft Voting Ensemble", "Flask Deployment"]
    bw = Inches(2.05)
    bgap = Inches(0.18)
    for idx, b_text in enumerate(badges):
        bx = Inches(1.25) + idx * (bw + bgap)
        b_shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, Inches(3.85), bw, Inches(0.35))
        b_shp.fill.solid()
        b_shp.fill.fore_color.rgb = RGBColor(239, 246, 255)
        b_shp.line.color.rgb = RGBColor(191, 219, 254)
        tf_b = b_shp.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.alignment = PP_ALIGN.CENTER
        p_b.text = b_text
        p_b.font.name = FONT_BODY
        p_b.font.size = Pt(9.0)
        p_b.font.bold = True
        p_b.font.color.rgb = PRIMARY_BLUE

    # Student & Guide Cards Container
    c1 = add_card(slide, Inches(1.25), Inches(4.55), Inches(5.3), Inches(2.0), bg_color=RGBColor(248, 250, 252))
    tb_c1 = slide.shapes.add_textbox(Inches(1.5), Inches(4.7), Inches(4.8), Inches(1.7))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True
    p1 = tf_c1.paragraphs[0]
    p1.text = "PRESENTED BY"
    p1.font.size = Pt(9.5)
    p1.font.bold = True
    p1.font.color.rgb = TEAL

    p2 = tf_c1.add_paragraph()
    p2.text = "Jiphin George"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = NAVY

    p3 = tf_c1.add_paragraph()
    p3.text = "Register No: MAC25MCA-2033\nCourse: Master of Computer Applications (MCA)"
    p3.font.size = Pt(10.5)
    p3.font.color.rgb = SLATE_BODY

    c2 = add_card(slide, Inches(6.8), Inches(4.55), Inches(5.65), Inches(2.0), bg_color=RGBColor(248, 250, 252))
    tb_c2 = slide.shapes.add_textbox(Inches(7.05), Inches(4.7), Inches(5.15), Inches(1.7))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True
    p4 = tf_c2.paragraphs[0]
    p4.text = "PROJECT GUIDE"
    p4.font.size = Pt(9.5)
    p4.font.bold = True
    p4.font.color.rgb = TEAL

    p5 = tf_c2.add_paragraph()
    p5.text = "Mr. Biju Skaria"
    p5.font.size = Pt(17)
    p5.font.bold = True
    p5.font.color.rgb = NAVY

    p6 = tf_c2.add_paragraph()
    p6.text = "Associate Professor, Department of Computer Applications\nMar Athanasius College of Engineering, Kothamangalam"
    p6.font.size = Pt(10.5)
    p6.font.color.rgb = SLATE_BODY


def build_slide_2(prs):
    """SLIDE 2: PROBLEM STATEMENT AND PROJECT OVERVIEW"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Problem Statement & Project Overview", "Introduction", 2)

    # Top Pipeline Indicator Cards
    steps = [
        ("1. Clinical Text", "Unstructured medical narratives & patient records"),
        ("2. Text Preprocessing", "Cleaning, lemmatization & medical stop-words"),
        ("3. TF-IDF Extraction", "Unigram/bigram numerical vectorization"),
        ("4. Ensemble ML", "Calibrated soft-voting classification"),
        ("5. Medical Specialty", "Automated prediction across 40 departments")
    ]
    step_w = Inches(2.22)
    step_gap = Inches(0.15)
    for idx, (title, sub) in enumerate(steps):
        sx = Inches(0.8) + idx * (step_w + step_gap)
        c = add_card(slide, sx, Inches(1.3), step_w, Inches(1.05), bg_color=RGBColor(240, 249, 255), border_color=RGBColor(186, 230, 253))
        tb = slide.shapes.add_textbox(sx + Inches(0.1), Inches(1.35), step_w - Inches(0.2), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = PRIMARY_BLUE
        p2 = tf.add_paragraph()
        p2.text = sub
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = SLATE_BODY

    # Two Main Cards: Problem (Left) vs Solution (Right)
    # Left Card: Problem
    card_w = Inches(5.72)
    add_card(slide, Inches(0.8), Inches(2.55), card_w, Inches(4.2), bg_color=WHITE, border_color=RGBColor(254, 202, 202))
    # Accent top banner on problem card
    tb_pr_hdr = slide.shapes.add_textbox(Inches(1.05), Inches(2.7), card_w - Inches(0.5), Inches(0.45))
    tf_pr = tb_pr_hdr.text_frame
    p = tf_pr.paragraphs[0]
    p.text = "THE CLINICAL CHALLENGE: MANUAL CLASSIFICATION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38)

    tb_pr_body = slide.shapes.add_textbox(Inches(1.05), Inches(3.2), card_w - Inches(0.5), Inches(3.4))
    tf_pb = tb_pr_body.text_frame
    tf_pb.word_wrap = True
    items_pr = [
        ("Unstructured Clinical Narratives", "Modern hospitals generate thousands of medical dictations, discharge summaries, and consult notes daily stored entirely as unstructured free text."),
        ("High Vocabulary Diversity & Jargon", "Medical terminology varies drastically between subdomains, containing dense Latin roots, complex clinical abbreviations, and doctor-specific phrasing."),
        ("Labor-Intensive & Error-Prone Tagging", "Manual review and indexing across 40+ medical specialties is severely time-consuming, expensive, and subject to human cognitive fatigue."),
        ("Inconsistent Cross-Department Labeling", "Different human annotators assign conflicting specialty tags to overlapping patient cases, impairing hospital record retrieval and patient workflow.")
    ]
    for idx, (head, body) in enumerate(items_pr):
        p_h = tf_pb.paragraphs[0] if idx == 0 else tf_pb.add_paragraph()
        p_h.text = f"•  {head}: "
        p_h.font.size = Pt(10.5)
        p_h.font.bold = True
        p_h.font.color.rgb = NAVY
        p_h.space_before = Pt(6) if idx > 0 else Pt(0)
        
        # Add body run
        r = p_h.add_run()
        r.text = body
        r.font.bold = False
        r.font.size = Pt(9.5)
        r.font.color.rgb = SLATE_BODY

    # Right Card: Proposed Solution
    add_card(slide, Inches(6.8), Inches(2.55), card_w, Inches(4.2), bg_color=WHITE, border_color=RGBColor(187, 247, 208))
    tb_sol_hdr = slide.shapes.add_textbox(Inches(7.05), Inches(2.7), card_w - Inches(0.5), Inches(0.45))
    tf_sol = tb_sol_hdr.text_frame
    p_s = tf_sol.paragraphs[0]
    p_s.text = "THE PROPOSED SOLUTION: AUTOMATED ML PIPELINE"
    p_s.font.size = Pt(12)
    p_s.font.bold = True
    p_s.font.color.rgb = RGBColor(22, 101, 52)

    tb_sol_body = slide.shapes.add_textbox(Inches(7.05), Inches(3.2), card_w - Inches(0.5), Inches(3.4))
    tf_sb = tb_sol_body.text_frame
    tf_sb.word_wrap = True
    items_sol = [
        ("Automated NLP & TF-IDF Extraction", "Transforms unstructured medical text through lowercasing, stop-word removal, and lemmatization into standardized, high-dimensional TF-IDF feature vectors."),
        ("Multi-Classifier Supervised Learning", "Evaluates four distinct algorithms: SVM, Random Forest, Logistic Regression, and Multinomial Naive Bayes."),
        ("Soft Consensus Voting Ensemble", "Synthesizes calibrated class probability distributions across all candidate models to mitigate individual classifier bias and reduce variance."),
        ("Live Interactive Web Deployment", "Integrates the serialized pipeline into a lightweight Flask web application, delivering instant specialty predictions and confidence scores for clinicians.")
    ]
    for idx, (head, body) in enumerate(items_sol):
        p_h = tf_sb.paragraphs[0] if idx == 0 else tf_sb.add_paragraph()
        p_h.text = f"✓  {head}: "
        p_h.font.size = Pt(10.5)
        p_h.font.bold = True
        p_h.font.color.rgb = NAVY
        p_h.space_before = Pt(6) if idx > 0 else Pt(0)
        
        r = p_h.add_run()
        r.text = body
        r.font.bold = False
        r.font.size = Pt(9.5)
        r.font.color.rgb = SLATE_BODY


def build_slide_3(prs):
    """SLIDE 3: LITERATURE REVIEW - OVERVIEW & LANDSCAPE"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Literature Review: Background & Research Landscape", "Literature Review", 3)

    # Top Flow Banner
    flow_steps = [
        ("1. Prior Literature", "Validation of ML for clinical text"),
        ("2. Key Methodologies", "TF-IDF vectorization & linear classifiers"),
        ("3. Identified Gap", "High variance & heavy GPU requirements"),
        ("4. Proposed Architecture", "Lightweight soft voting ensemble on web")
    ]
    f_w = Inches(2.78)
    f_gap = Inches(0.2)
    for idx, (t1, t2) in enumerate(flow_steps):
        fx = Inches(0.8) + idx * (f_w + f_gap)
        c = add_card(slide, fx, Inches(1.25), f_w, Inches(0.85), bg_color=RGBColor(241, 245, 249), border_color=CARD_BORDER)
        tb = slide.shapes.add_textbox(fx + Inches(0.1), Inches(1.3), f_w - Inches(0.2), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = t1
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = PRIMARY_BLUE
        p2 = tf.add_paragraph()
        p2.text = t2
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = SLATE_MUTED

    # 4 Thematic Pillars in 2x2 layout
    cards_data = [
        ("Clinical NLP & Preprocessing", TEAL, [
            "Medical text contains distinct lexical noise: contractions, special characters, and non-informative clinical stops.",
            "Studies establish a standard 5-step sequence: Cleaning, Lowercasing, Stop-word removal, Lemmatization, and Tokenization.",
            "Domain-specific lemmatization normalizes inflected clinical roots without losing diagnostic context."
        ]),
        ("TF-IDF Feature Representation", PRIMARY_BLUE, [
            "Clinical notes exhibit high dimensional vocabulary with extreme word frequency variance across specialties.",
            "TF-IDF with sublinear scaling (1 + log(TF)) dampens repetitive clinical terms ('patient', 'procedure').",
            "Significantly faster and more lightweight than Word2Vec or deep embeddings, enabling instant local web deployment."
        ]),
        ("Supervised ML Classifiers", ACCENT_BLUE, [
            "Literature demonstrates that SVM and Logistic Regression excel at high-dimensional sparse text vectors.",
            "Random Forest introduces non-linear feature interactions and bagging robustness.",
            "Multinomial Naive Bayes provides strong, rapid probabilistic likelihoods for word frequency text representations."
        ]),
        ("Ensemble Learning & Research Gap", PURPLE, [
            "Individual models show variable recall across the 40 imbalanced medical specialties in clinical practice.",
            "Deep transformer models (BioBERT) require heavy GPU servers, unsuitable for lightweight hospital web apps.",
            "Research Gap: Need for a fast, accessible Soft Voting Ensemble combining calibrated base estimators."
        ])
    ]

    col_w = Inches(5.72)
    card_h = Inches(2.15)
    for idx, (title, color, bullets) in enumerate(cards_data):
        cx = Inches(0.8) if idx % 2 == 0 else Inches(6.8)
        cy = Inches(2.35) if idx < 2 else Inches(4.65)
        
        c = add_card(slide, cx, cy, col_w, card_h, bg_color=WHITE, border_color=CARD_BORDER)
        # Colored accent stripe on left of card
        stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, cy, Inches(0.08), card_h)
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = color
        stripe.line.fill.background()

        tb = slide.shapes.add_textbox(cx + Inches(0.25), cy + Inches(0.12), col_w - Inches(0.4), card_h - Inches(0.25))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(11.5)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"•  {b}"
            pb.font.size = Pt(9.0)
            pb.font.color.rgb = SLATE_BODY
            pb.space_before = Pt(3)


def build_slide_4(prs):
    """SLIDE 4: SUMMARY OF RESEARCH PAPERS"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Summary of Key Research Papers", "Literature Review", 4)

    papers = [
        {
            "num": "PAPER 1",
            "title": "Clinical Text Classification using Machine Learning",
            "authors": "Almazaydeh et al. (2023)",
            "badge": "MTSamples & Preprocessing",
            "color": PRIMARY_BLUE,
            "method": "Kaggle MTSamples Dataset | 5-Stage Modular NLP Pipeline (Cleaning, Lowering, Stop-words, Lemmatization, Tokenization) + TF-IDF Vectorization.",
            "finding": "Demonstrated that thorough clinical text preprocessing and TF-IDF feature weighting are critical to prevent sparse lexical noise and boost classification accuracy.",
            "relevance": "Establishes our exact 5-step NLP preprocessing pipeline and proves the efficacy of the public Kaggle MTSamples benchmark dataset."
        },
        {
            "num": "PAPER 2",
            "title": "Clinical Vectorization and Multi-Class Supervised Learning",
            "authors": "Omar et al. (2023)",
            "badge": "Feature Spaces & Estimators",
            "color": TEAL,
            "method": "EMR Narrative Records | Evaluated Logistic Regression, SVM, Multinomial Naive Bayes, and k-NN across clinical categories.",
            "finding": "SVM and Logistic Regression outperformed complex non-linear models on high-dimensional text vectors, achieving peak accuracy (92%) with rapid convergence.",
            "relevance": "Directly justifies our selection of SVM and Logistic Regression as core candidate estimators for sparse TF-IDF text matrices."
        },
        {
            "num": "PAPER 3",
            "title": "Medical Subdomain Classification & Ensemble Aggregation",
            "authors": "Weng et al. (2017) / Al-Garadi et al.",
            "badge": "Ensemble Methods",
            "color": PURPLE,
            "method": "Multi-Specialty Clinical Narratives | Multi-estimator aggregation, probability consensus, and tree-based decision ensembles.",
            "finding": "Ensemble voting across complementary classifiers significantly mitigates individual estimator variance and improves multi-class minority specialty recognition.",
            "relevance": "Provides the foundational justification for our proposed Soft Consensus Voting Ensemble combining SVM, Random Forest, LR, and MNB."
        }
    ]

    p_w = Inches(3.75)
    p_gap = Inches(0.24)
    for idx, p_info in enumerate(papers):
        px = Inches(0.8) + idx * (p_w + p_gap)
        py = Inches(1.3)
        p_h = Inches(5.4)

        # Card container
        c = add_card(slide, px, py, p_w, p_h, bg_color=WHITE, border_color=CARD_BORDER)
        # Top color accent bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, px, py, p_w, Inches(0.12))
        bar.fill.solid()
        bar.fill.fore_color.rgb = p_info['color']
        bar.line.fill.background()

        tb = slide.shapes.add_textbox(px + Inches(0.2), py + Inches(0.22), p_w - Inches(0.4), p_h - Inches(0.35))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = p_info['num']
        p0.font.size = Pt(9.5)
        p0.font.bold = True
        p0.font.color.rgb = p_info['color']

        p1 = tf.add_paragraph()
        p1.text = p_info['title']
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = NAVY
        p1.space_before = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = f"Authors: {p_info['authors']}"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = SLATE_MUTED
        p2.space_before = Pt(2)

        # Methodology Box
        p_m_lbl = tf.add_paragraph()
        p_m_lbl.text = "METHODOLOGY & DATASET:"
        p_m_lbl.font.size = Pt(9)
        p_m_lbl.font.bold = True
        p_m_lbl.font.color.rgb = PRIMARY_BLUE
        p_m_lbl.space_before = Pt(10)

        p_m = tf.add_paragraph()
        p_m.text = p_info['method']
        p_m.font.size = Pt(9)
        p_m.font.color.rgb = SLATE_BODY
        p_m.space_before = Pt(2)

        # Key Finding Box
        p_f_lbl = tf.add_paragraph()
        p_f_lbl.text = "KEY RESEARCH FINDING:"
        p_f_lbl.font.size = Pt(9)
        p_f_lbl.font.bold = True
        p_f_lbl.font.color.rgb = TEAL
        p_f_lbl.space_before = Pt(10)

        p_f = tf.add_paragraph()
        p_f.text = p_info['finding']
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = SLATE_BODY
        p_f.space_before = Pt(2)

        # Relevance Box
        p_r_lbl = tf.add_paragraph()
        p_r_lbl.text = "DIRECT RELEVANCE TO OUR SYSTEM:"
        p_r_lbl.font.size = Pt(9)
        p_r_lbl.font.bold = True
        p_r_lbl.font.color.rgb = PURPLE
        p_r_lbl.space_before = Pt(10)

        p_r = tf.add_paragraph()
        p_r.text = p_info['relevance']
        p_r.font.size = Pt(9)
        p_r.font.color.rgb = SLATE_BODY
        p_r.space_before = Pt(2)


def build_slide_5(prs):
    """SLIDE 5: DATASET OVERVIEW"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Dataset Overview: Kaggle MTSamples Corpus", "Data Exploration", 5)

    # 4 Statistic Cards Across Top
    kpis = [
        ("4,999", "INITIAL RAW RECORDS", "Total transcription files in Kaggle dataset", PRIMARY_BLUE),
        ("~40", "MEDICAL SPECIALTIES", "Multi-class medical classification targets", TEAL),
        ("4,966", "USABLE REPORTS AFTER CLEANING", "Complete records after dropping blank nulls", GREEN),
        ("33", "DROPPED NULL SAMPLES", "Zero-length empty text reports identified", AMBER)
    ]
    k_w = Inches(2.78)
    k_gap = Inches(0.2)
    for idx, (stat, title, desc, color) in enumerate(kpis):
        kx = Inches(0.8) + idx * (k_w + k_gap)
        c = add_card(slide, kx, Inches(1.3), k_w, Inches(1.35), bg_color=WHITE, border_color=CARD_BORDER)
        # Top color badge
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, kx, Inches(1.3), k_w, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()

        tb = slide.shapes.add_textbox(kx + Inches(0.15), Inches(1.45), k_w - Inches(0.3), Inches(1.15))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = stat
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = color
        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = NAVY
        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(8.0)
        p3.font.color.rgb = SLATE_MUTED

    # Two Structured Detail Cards Below
    c_w = Inches(5.72)
    # Left: Provenance & Healthcare Context
    add_card(slide, Inches(0.8), Inches(2.85), c_w, Inches(3.9), bg_color=WHITE, border_color=CARD_BORDER)
    tb_left = slide.shapes.add_textbox(Inches(1.05), Inches(3.0), c_w - Inches(0.5), Inches(3.6))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True

    p_lh = tf_l.paragraphs[0]
    p_lh.text = "DATASET PROVENANCE & CLINICAL CONTEXT"
    p_lh.font.size = Pt(12)
    p_lh.font.bold = True
    p_lh.font.color.rgb = PRIMARY_BLUE

    items_l = [
        ("Public Academic Benchmark", "Sourced from the verified Kaggle MTSamples repository, comprising real-world anonymized medical transcription dictations."),
        ("Overcoming HIPAA Constraints", "HIPAA privacy regulations legally restrict distribution of private hospital electronic health records (EHR). MTSamples provides an authentic, ethically validated substitute."),
        ("Diverse Medical Narratives", "Contains actual physician dictations spanning operative notes, discharge summaries, emergency consultations, physical examinations, and patient histories."),
        ("Multi-Class Domain Breadth", "Encompasses 40 distinct specialty disciplines from General Medicine and Surgery to Neurosurgery, Cardiology, and Pediatrics.")
    ]
    for idx, (h, b) in enumerate(items_l):
        p = tf_l.add_paragraph()
        p.text = f"•  {h}: "
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.size = Pt(9)
        r.font.color.rgb = SLATE_BODY

    # Right: Dataset Attributes & Field Breakdown
    add_card(slide, Inches(6.8), Inches(2.85), c_w, Inches(3.9), bg_color=WHITE, border_color=CARD_BORDER)
    tb_right = slide.shapes.add_textbox(Inches(7.05), Inches(3.0), c_w - Inches(0.5), Inches(3.6))
    tf_r = tb_right.text_frame
    tf_r.word_wrap = True

    p_rh = tf_r.paragraphs[0]
    p_rh.text = "KEY DATASET ATTRIBUTES & ROLES"
    p_rh.font.size = Pt(12)
    p_rh.font.bold = True
    p_rh.font.color.rgb = TEAL

    items_r = [
        ("transcription (Primary Feature Input)", "Contains full free-text clinical narrative. Serves as the raw textual input for our 5-step NLP preprocessing and TF-IDF feature extraction pipeline."),
        ("medical_specialty (Target Class Label)", "The ground-truth categorical specialty label (40 distinct classes) to be learned and predicted by the supervised machine learning models."),
        ("description (Secondary Context)", "Short clinician summary of the medical case; utilized during exploratory validation to verify narrative diagnostic alignment."),
        ("keywords (Omitted Attribute)", "Free-form clinician tags containing 21.36% missing values. Omitted from the model pipeline to prevent sparse keyword noise.")
    ]
    for idx, (h, b) in enumerate(items_r):
        p = tf_r.add_paragraph()
        p.text = f"•  {h}: "
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(6)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.size = Pt(9)
        r.font.color.rgb = SLATE_BODY


def build_slide_6(prs):
    """SLIDE 6: DATA EXPLORATION - DATASET QUALITY"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Data Exploration: Dataset Quality & Missing Value Analysis", "Data Exploration", 6)

    # Left: EDA Image
    img_path = "Inital Report/EDA_Diagrams/01_missing_values.png"
    if os.path.exists(img_path):
        # 2964x1767 -> aspect = 1.677. Set width = 6.4 in -> height = 3.81 in
        slide.shapes.add_picture(img_path, Inches(0.8), Inches(1.4), Inches(6.4), Inches(3.81))

    # EDA Caption box below image
    c_img = add_card(slide, Inches(0.8), Inches(5.35), Inches(6.4), Inches(1.35), bg_color=WHITE, border_color=CARD_BORDER)
    tb_cap = slide.shapes.add_textbox(Inches(0.95), Inches(5.45), Inches(6.1), Inches(1.15))
    tf_c = tb_cap.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = "Figure: Missing Value Distribution across Dataset Attributes"
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = NAVY
    p_c2 = tf_c.add_paragraph()
    p_c2.text = "Systematic missing value analysis verifies that transcription has minimal nulls (0.66%), medical_specialty is 100% complete, and keywords has severe sparsity (21.36%)."
    p_c2.font.size = Pt(8.5)
    p_c2.font.color.rgb = SLATE_MUTED

    # Right: Structured Observations
    c_w = Inches(5.0)
    add_card(slide, Inches(7.5), Inches(1.4), c_w, Inches(5.3), bg_color=WHITE, border_color=CARD_BORDER)
    tb_obs = slide.shapes.add_textbox(Inches(7.75), Inches(1.6), c_w - Inches(0.5), Inches(4.9))
    tf_o = tb_obs.text_frame
    tf_o.word_wrap = True

    p_oh = tf_o.paragraphs[0]
    p_oh.text = "CRITICAL DATA QUALITY OBSERVATIONS"
    p_oh.font.size = Pt(12)
    p_oh.font.bold = True
    p_oh.font.color.rgb = PRIMARY_BLUE

    points = [
        ("Transcription Missing Values (33 Records)", "Exploratory audit revealed exactly 33 records (0.66%) with completely blank/null transcription text. Because clinical narrative is the core model input, these 33 rows were safely pruned.", GREEN),
        ("Target Label Completeness (0 Missing)", "The target variable 'medical_specialty' exhibits 100% data integrity with zero null values across all 4,999 records, ensuring dependable supervised classification ground truth.", TEAL),
        ("Keywords Attribute Sparsity (1,068 Missing)", "The 'keywords' field contains 1,068 missing entries (21.36%). To avoid artificial noise and severe missingness imputation, it was excluded from feature vectorization.", AMBER),
        ("Final Usable Dataset (4,966 Records)", "Following systematic data cleaning, a pristine subset of 4,966 high-integrity clinical reports remains, providing robust data for model training and cross-validation.", PRIMARY_BLUE)
    ]

    for h, b, col in points:
        p_h = tf_o.add_paragraph()
        p_h.text = f"✓  {h}"
        p_h.font.size = Pt(10)
        p_h.font.bold = True
        p_h.font.color.rgb = col
        p_h.space_before = Pt(8)

        p_b = tf_o.add_paragraph()
        p_b.text = b
        p_b.font.size = Pt(8.8)
        p_b.font.color.rgb = SLATE_BODY
        p_b.space_before = Pt(2)


def build_slide_7(prs):
    """SLIDE 7: DATA EXPLORATION - MEDICAL SPECIALTY DISTRIBUTION"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Data Exploration: Medical Specialty Class Distribution", "Data Exploration", 7)

    # Left: EDA Image
    img_path = "Inital Report/EDA_Diagrams/02_top10_medical_specialties.png"
    if os.path.exists(img_path):
        # 3565x2068 -> aspect = 1.724. Set width = 6.6 in -> height = 3.83 in
        slide.shapes.add_picture(img_path, Inches(0.8), Inches(1.4), Inches(6.6), Inches(3.83))

    # EDA Caption box below image
    add_card(slide, Inches(0.8), Inches(5.35), Inches(6.6), Inches(1.35), bg_color=WHITE, border_color=CARD_BORDER)
    tb_cap = slide.shapes.add_textbox(Inches(0.95), Inches(5.45), Inches(6.3), Inches(1.15))
    tf_c = tb_cap.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = "Figure: Frequency Distribution of Top 10 Medical Specialties"
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = NAVY
    p_c2 = tf_c.add_paragraph()
    p_c2.text = "Surgery dominates the dataset with 1,088 reports, followed by Consultative Medicine (516) and Cardiovascular (371), creating a classic long-tailed multi-class distribution."
    p_c2.font.size = Pt(8.5)
    p_c2.font.color.rgb = SLATE_MUTED

    # Right: Analytical Insights & Imbalance Strategy
    c_w = Inches(4.8)
    add_card(slide, Inches(7.7), Inches(1.4), c_w, Inches(5.3), bg_color=WHITE, border_color=CARD_BORDER)
    tb_ins = slide.shapes.add_textbox(Inches(7.95), Inches(1.6), c_w - Inches(0.5), Inches(4.9))
    tf_i = tb_ins.text_frame
    tf_i.word_wrap = True

    p_ih = tf_i.paragraphs[0]
    p_ih.text = "DISTRIBUTION INSIGHTS & STRATEGY"
    p_ih.font.size = Pt(12)
    p_ih.font.bold = True
    p_ih.font.color.rgb = PRIMARY_BLUE

    items = [
        ("Prominent Class Imbalance", "Surgery represents 1,088 out of 4,966 records (~21.9%), while minority specialties (e.g., Hospice, Allergy) contain fewer than 20 cases each.", AMBER),
        ("Top 10 High Concentration", "The top 10 medical specialties collectively account for over 70% of all clinical reports, forming a pronounced majority cluster.", NAVY),
        ("Mandatory Stratified Splitting", "To prevent minority classes from being excluded during train-test partitioning, stratified sampling (80% train / 20% test) is strictly required.", TEAL),
        ("Multi-Metric Evaluation Design", "Accuracy alone is misleading on imbalanced data. Evaluation must incorporate Macro-Precision, Macro-Recall, and Weighted F1-Score.", PURPLE)
    ]

    for h, b, col in items:
        p_h = tf_i.add_paragraph()
        p_h.text = f"•  {h}"
        p_h.font.size = Pt(10)
        p_h.font.bold = True
        p_h.font.color.rgb = col
        p_h.space_before = Pt(8)

        p_b = tf_i.add_paragraph()
        p_b.text = b
        p_b.font.size = Pt(8.8)
        p_b.font.color.rgb = SLATE_BODY
        p_b.space_before = Pt(2)


def build_slide_8(prs):
    """SLIDE 8: DATA EXPLORATION - CLINICAL TEXT ANALYSIS"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Data Exploration: Clinical Transcription Text & Lexical Analysis", "Data Exploration", 8)

    # Left Visual: Transcription Length Distribution
    img_len = "Inital Report/EDA_Diagrams/04_transcription_length_distribution.png"
    if os.path.exists(img_len):
        # 3564x1768 -> aspect = 2.016. Width = 5.6 in -> Height = 2.78 in
        slide.shapes.add_picture(img_len, Inches(0.8), Inches(1.3), Inches(5.6), Inches(2.78))

    # Right Visual: Word Cloud
    img_wc = "Inital Report/EDA_Diagrams/06_medical_transcription_wordcloud.png"
    if os.path.exists(img_wc):
        # 4538x2668 -> aspect = 1.701. Width = 5.7 in -> Height = 3.35 in
        # Place at x=6.8, y=1.3, width=5.7, height=3.35
        slide.shapes.add_picture(img_wc, Inches(6.8), Inches(1.3), Inches(5.7), Inches(3.35))

    # Left Caption Box
    c_l = add_card(slide, Inches(0.8), Inches(4.2), Inches(5.6), Inches(2.55), bg_color=WHITE, border_color=CARD_BORDER)
    tb_cl = slide.shapes.add_textbox(Inches(0.95), Inches(4.3), Inches(5.3), Inches(2.35))
    tf_cl = tb_cl.text_frame
    tf_cl.word_wrap = True
    p1 = tf_cl.paragraphs[0]
    p1.text = "KEY FINDINGS: TEXT LENGTH DISTRIBUTION"
    p1.font.size = Pt(10.5)
    p1.font.bold = True
    p1.font.color.rgb = PRIMARY_BLUE

    pts_l = [
        "Right-Skewed Distribution: Most clinical notes span 200 to 700 words, reflecting concise clinical summaries.",
        "Detailed Operative Reports: A long tail extends beyond 1,500+ words for complex surgical procedures and multi-system consults.",
        "Impact on Feature Space: Extreme length disparity necessitates L2 Euclidean vector normalization in TF-IDF."
    ]
    for b in pts_l:
        p = tf_cl.add_paragraph()
        p.text = f"•  {b}"
        p.font.size = Pt(8.8)
        p.font.color.rgb = SLATE_BODY
        p.space_before = Pt(3)

    # Right Caption Box
    c_r = add_card(slide, Inches(6.8), Inches(4.8), Inches(5.7), Inches(1.95), bg_color=WHITE, border_color=CARD_BORDER)
    tb_cr = slide.shapes.add_textbox(Inches(6.95), Inches(4.9), Inches(5.4), Inches(1.75))
    tf_cr = tb_cr.text_frame
    tf_cr.word_wrap = True
    p2 = tf_cr.paragraphs[0]
    p2.text = "KEY FINDINGS: CLINICAL LEXICAL PATTERNS"
    p2.font.size = Pt(10.5)
    p2.font.bold = True
    p2.font.color.rgb = TEAL

    pts_r = [
        "Dominant Clinical Jargon: Pervasive occurrences of terms like 'patient', 'procedure', 'history', 'diagnosis', 'left', 'right'.",
        "Stop-word Removal & Sublinear Scaling: Validates removing non-discriminative medical stopwords and applying sublinear term frequency weighting."
    ]
    for b in pts_r:
        p = tf_cr.add_paragraph()
        p.text = f"•  {b}"
        p.font.size = Pt(8.8)
        p.font.color.rgb = SLATE_BODY
        p.space_before = Pt(3)


def build_slide_9(prs):
    """SLIDE 9: DATA EXPLORATION - SPECIALTY-WISE TEXT LENGTH"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Transcription Length Across Medical Specialties & EDA Summary", "Data Exploration", 9)

    # Left: EDA Boxplot Image
    img_bp = "Inital Report/EDA_Diagrams/05_transcription_length_by_specialty.png"
    if os.path.exists(img_bp):
        # 4140x2368 -> aspect = 1.748. Set width = 6.6 in -> height = 3.78 in
        slide.shapes.add_picture(img_bp, Inches(0.8), Inches(1.4), Inches(6.6), Inches(3.78))

    # Caption under boxplot
    add_card(slide, Inches(0.8), Inches(5.3), Inches(6.6), Inches(1.4), bg_color=WHITE, border_color=CARD_BORDER)
    tb_cap = slide.shapes.add_textbox(Inches(0.95), Inches(5.4), Inches(6.3), Inches(1.2))
    tf_c = tb_cap.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = "Figure: Transcription Length Boxplots Across Top 10 Specialties"
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = NAVY
    p_c2 = tf_c.add_paragraph()
    p_c2.text = "Substantial variance exists between specialties: surgical notes feature high median lengths and widespread upper outliers, whereas consultative and diagnostic notes are comparatively concise."
    p_c2.font.size = Pt(8.5)
    p_c2.font.color.rgb = SLATE_MUTED

    # Right: Analytical Observations + EDA Conclusion
    c_w = Inches(4.8)
    add_card(slide, Inches(7.7), Inches(1.4), c_w, Inches(5.3), bg_color=WHITE, border_color=CARD_BORDER)
    tb_rt = slide.shapes.add_textbox(Inches(7.95), Inches(1.6), c_w - Inches(0.5), Inches(4.9))
    tf_rt = tb_rt.text_frame
    tf_rt.word_wrap = True

    p_rh = tf_rt.paragraphs[0]
    p_rh.text = "SPECIALTY-WISE VARIATION"
    p_rh.font.size = Pt(11.5)
    p_rh.font.bold = True
    p_rh.font.color.rgb = PRIMARY_BLUE

    obs = [
        ("Operational vs Diagnostic Depth", "Specialties like Surgery and Orthopedic require comprehensive documentation of intra-operative procedures, yielding longer texts with heavy technical outliers."),
        ("Concise Clinical Encounters", "Fields like Dermatology and Radiology center around concise focal findings, presenting substantially tighter word count distributions.")
    ]
    for h, b in obs:
        p = tf_rt.add_paragraph()
        p.text = f"•  {h}: "
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(4)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.size = Pt(8.8)
        r.font.color.rgb = SLATE_BODY

    # EDA Phase Conclusion Box inside right card
    p_con_lbl = tf_rt.add_paragraph()
    p_con_lbl.text = "EDA PHASE CONCLUSION"
    p_con_lbl.font.size = Pt(11)
    p_con_lbl.font.bold = True
    p_con_lbl.font.color.rgb = TEAL
    p_con_lbl.space_before = Pt(12)

    p_con = tf_rt.add_paragraph()
    p_con.text = "The comprehensive exploratory analysis confirms that the clinical corpus exhibits diverse document lengths, lexical sparsity, missing values, and severe class imbalance.\n\nThese empirical findings establish the foundation for our 5-step NLP preprocessing, sublinear TF-IDF vectorization, stratified partitioning, and soft voting ensemble modeling."
    p_con.font.size = Pt(8.8)
    p_con.font.color.rgb = SLATE_BODY
    p_con.space_before = Pt(3)


def build_slide_10(prs):
    """SLIDE 10: DETAILS OF THE PROPOSED ALGORITHMS"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Details of Proposed Machine Learning Algorithms", "Proposed Algorithms", 10)

    # Top Distinction Banner
    c_top = add_card(slide, Inches(0.8), Inches(1.25), Inches(11.733), Inches(0.8), bg_color=RGBColor(239, 246, 255), border_color=RGBColor(191, 219, 254))
    tb_top = slide.shapes.add_textbox(Inches(1.0), Inches(1.3), Inches(11.333), Inches(0.7))
    tf_tp = tb_top.text_frame
    tf_tp.word_wrap = True
    p_t1 = tf_tp.paragraphs[0]
    p_t1.text = "FOUNDATIONAL DISTINCTION: FEATURE EXTRACTION vs. CLASSIFICATION ESTIMATORS"
    p_t1.font.size = Pt(10.5)
    p_t1.font.bold = True
    p_t1.font.color.rgb = PRIMARY_BLUE
    p_t2 = tf_tp.add_paragraph()
    p_t2.text = "TF-IDF (Term Frequency–Inverse Document Frequency) is the mathematical feature representation technique that vectorizes text into sparse matrices. The four algorithms below are the distinct Supervised Machine Learning Classifiers evaluated in our pipeline."
    p_t2.font.size = Pt(9.0)
    p_t2.font.color.rgb = SLATE_BODY

    # 4 Algorithm Cards in 2x2 Grid
    algos = [
        ("Logistic Regression (LR)", PRIMARY_BLUE, "Linear Probabilistic Baseline", [
            "Formulation: Multi-class linear model using cross-entropy loss and softmax probability mapping.",
            "High-Dimensional Efficacy: Highly efficient and fast convergence on sparse, high-dimensional TF-IDF vectors.",
            "Calibrated Outputs: Inherently yields smooth, well-calibrated class probability estimates for soft voting."
        ]),
        ("Support Vector Machine (SVM)", TEAL, "Maximum-Margin Hyperplane", [
            "Formulation: Identifies optimal separating hyperplanes maximizing the functional margin between specialty classes.",
            "Sparse Vector Superiority: Consistently recognized in clinical NLP literature as a top performer for text classification.",
            "Decision Boundary Optimization: Effectively establishes robust decision boundaries across high-dimensional clinical feature vectors."
        ]),
        ("Random Forest (RF)", PURPLE, "Bagged Decision Tree Ensemble", [
            "Formulation: Ensemble of decorrelated decision trees trained via bootstrap aggregating and random feature subsets.",
            "Non-Linear Interactions: Effectively captures complex term co-occurrences and non-linear clinical relationships.",
            "Robustness to Overfitting: High resistance to individual feature noise and document length variations."
        ]),
        ("Multinomial Naïve Bayes (MNB)", DARK_BLUE, "Probabilistic Word-Frequency Model", [
            "Formulation: Applies Bayes' theorem with independence assumptions tailored for discrete term frequency vectors.",
            "Laplace Smoothing: Handles zero-probability terms for unobserved medical tokens in test transcriptions.",
            "Computational Efficiency: Exceptionally lightweight and rapid, providing diverse complementary probabilities."
        ])
    ]

    card_w = Inches(5.72)
    card_h = Inches(2.2)
    for idx, (name, col, subtitle, pts) in enumerate(algos):
        ax = Inches(0.8) if idx % 2 == 0 else Inches(6.8)
        ay = Inches(2.25) if idx < 2 else Inches(4.6)

        c = add_card(slide, ax, ay, card_w, card_h, bg_color=WHITE, border_color=CARD_BORDER)
        # Left accent stripe
        stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, ax, ay, Inches(0.08), card_h)
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = col
        stripe.line.fill.background()

        tb = slide.shapes.add_textbox(ax + Inches(0.25), ay + Inches(0.12), card_w - Inches(0.4), card_h - Inches(0.25))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = name
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = subtitle.upper()
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = SLATE_MUTED

        for pt in pts:
            pb = tf.add_paragraph()
            pb.text = f"•  {pt}"
            pb.font.size = Pt(9.0)
            pb.font.color.rgb = SLATE_BODY
            pb.space_before = Pt(3)


def build_slide_11(prs):
    """SLIDE 11: ENSEMBLE MACHINE LEARNING APPROACH"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Ensemble Machine Learning Architecture: Soft Voting Strategy", "Proposed Algorithms", 11)

    # Top Central Architecture Diagram
    # 1. Feature Vector
    bx_w = Inches(2.5)
    c_vec = add_card(slide, Inches(0.8), Inches(1.3), bx_w, Inches(1.3), bg_color=RGBColor(241, 245, 249), border_color=CARD_BORDER)
    tb_v = slide.shapes.add_textbox(Inches(0.9), Inches(1.4), bx_w - Inches(0.2), Inches(1.1))
    tf_v = tb_v.text_frame
    tf_v.word_wrap = True
    p = tf_v.paragraphs[0]
    p.text = "TF-IDF VECTORS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE
    p2 = tf_v.add_paragraph()
    p2.text = "Sublinear frequency\nUnigrams & Bigrams\nSparse Matrix"
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = SLATE_BODY

    # 4 Parallel Model Blocks in Middle Column
    model_names = [
        ("SVM", TEAL),
        ("Random Forest", PURPLE),
        ("Logistic Regression", PRIMARY_BLUE),
        ("Multinomial Naive Bayes", DARK_BLUE)
    ]
    m_w = Inches(3.2)
    m_h = Inches(0.42)
    m_x = Inches(3.7)
    for idx, (m_name, m_col) in enumerate(model_names):
        my = Inches(1.25) + idx * Inches(0.48)
        c_m = add_card(slide, m_x, my, m_w, m_h, bg_color=WHITE, border_color=m_col)
        tb_m = slide.shapes.add_textbox(m_x, my + Inches(0.04), m_w, m_h - Inches(0.08))
        tf_m = tb_m.text_frame
        p_m = tf_m.paragraphs[0]
        p_m.alignment = PP_ALIGN.CENTER
        p_m.text = m_name
        p_m.font.size = Pt(9.5)
        p_m.font.bold = True
        p_m.font.color.rgb = m_col

    # Soft Voting Ensemble Block
    ens_w = Inches(2.9)
    c_ens = add_card(slide, Inches(7.3), Inches(1.3), ens_w, Inches(1.3), bg_color=RGBColor(250, 245, 255), border_color=RGBColor(216, 180, 254))
    tb_e = slide.shapes.add_textbox(Inches(7.4), Inches(1.4), ens_w - Inches(0.2), Inches(1.1))
    tf_e = tb_e.text_frame
    tf_e.word_wrap = True
    pe1 = tf_e.paragraphs[0]
    pe1.text = "SOFT VOTING ENSEMBLE"
    pe1.font.size = Pt(11)
    pe1.font.bold = True
    pe1.font.color.rgb = PURPLE
    pe2 = tf_e.add_paragraph()
    pe2.text = "Probability Consensus\nWeighted / Average Pooling\nVariance Reduction"
    pe2.font.size = Pt(8.5)
    pe2.font.color.rgb = SLATE_BODY

    # Prediction Output Block
    out_w = Inches(2.0)
    c_out = add_card(slide, Inches(10.533), Inches(1.3), out_w, Inches(1.3), bg_color=RGBColor(236, 253, 245), border_color=RGBColor(167, 243, 208))
    tb_o = slide.shapes.add_textbox(Inches(10.633), Inches(1.4), out_w - Inches(0.2), Inches(1.1))
    tf_o = tb_o.text_frame
    tf_o.word_wrap = True
    po1 = tf_o.paragraphs[0]
    po1.text = "FINAL PREDICTION"
    po1.font.size = Pt(11)
    po1.font.bold = True
    po1.font.color.rgb = GREEN
    po2 = tf_o.add_paragraph()
    po2.text = "Predicted Specialty +\nConfidence Score"
    po2.font.size = Pt(8.5)
    po2.font.color.rgb = SLATE_BODY

    # Lower Section: 3 Deep-Dive Architecture Cards
    sub_w = Inches(3.75)
    sub_gap = Inches(0.24)
    cards_ens = [
        ("Why Soft Voting Over Hard Voting?", PRIMARY_BLUE, [
            "Probability Granularity: Hard voting counts binary majority votes, ignoring confidence. Soft voting sums class probabilities.",
            "Weighting Subtle Signals: If an ambiguous clinical note gives 49% probability to Neurology across models, soft voting preserves that critical confidence gradient.",
            "Reduced Misclassification: Mitigates abrupt decision boundary errors common in single-vote deadlocks."
        ]),
        ("SVM in the Ensemble", TEAL, [
            "SVM is used as one of the base machine learning classifiers for medical specialty classification.",
            "It learns decision boundaries between different medical specialty categories using the TF-IDF feature representation.",
            "Its predictions contribute to the overall ensemble decision together with Random Forest, Logistic Regression, and Multinomial Naive Bayes."
        ]),
        ("Expected Ensemble Advantages", PURPLE, [
            "Bias-Variance Trade-off: Combines linear hyperplanes (SVM, LR) with tree-based partitioning (RF) and probabilistic priors (MNB).",
            "Minority Specialty Sensitivity: Improves recognition rates on under-represented medical classes with fewer training notes.",
            "Production Reliability: Ensures robust, dependable inference before serializing the pipeline for Flask web serving."
        ])
    ]

    for idx, (title, col, pts) in enumerate(cards_ens):
        cx = Inches(0.8) + idx * (sub_w + sub_gap)
        c = add_card(slide, cx, Inches(3.45), sub_w, Inches(3.25), bg_color=WHITE, border_color=CARD_BORDER)
        # Top color accent
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(3.45), sub_w, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = col
        bar.line.fill.background()

        tb = slide.shapes.add_textbox(cx + Inches(0.18), Inches(3.6), sub_w - Inches(0.36), Inches(2.95))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = col

        for pt in pts:
            pb = tf.add_paragraph()
            pb.text = f"•  {pt}"
            pb.font.size = Pt(8.8)
            pb.font.color.rgb = SLATE_BODY
            pb.space_before = Pt(4)


def build_slide_12(prs):
    """SLIDE 12: PROPOSED PROJECT PIPELINE"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Proposed End-to-End System Project Pipeline", "Project Pipeline", 12)

    # Main Visual: The finalized 300 DPI Project Pipeline Diagram
    pipeline_img = "Inital Report/EDA_Diagrams/07_project_pipeline.png"
    if os.path.exists(pipeline_img):
        # 4710x3750 -> aspect = 1.256. Height = 5.4 in -> Width = 6.78 in
        # Place on left at x=0.8, y=1.3, width=6.8, height=5.41
        slide.shapes.add_picture(pipeline_img, Inches(0.8), Inches(1.3), Inches(6.8), Inches(5.41))

    # Right Side: Structured Summary Cards for the 3 Containers
    c_w = Inches(4.65)
    r_x = Inches(7.88)
    
    stages = [
        ("CONTAINER 1: DATA STAGE", PRIMARY_BLUE, [
            "Kaggle MTSamples: 4,966 cleaned multi-specialty clinical transcriptions.",
            "Text Preprocessing: Lowercasing, medical stop-word filtering, WordNet lemmatization.",
            "TF-IDF Vectorization: Unigram & bigram features with sublinear scaling (features_final.csv)."
        ]),
        ("CONTAINER 2: MODEL BUILDING", TEAL, [
            "80/20 Stratified Split: Strict preservation of minority class proportions across all 40 specialties.",
            "Parallel Training: SVM (calibrated), Random Forest, Logistic Regression, Multinomial Naive Bayes.",
            "Soft Voting Ensemble: Synthesizes probability consensus, evaluated via multi-class metrics & serialized."
        ]),
        ("CONTAINER 3: DEPLOYMENT STAGE", PURPLE, [
            "Flask Web Application: Interactive clinician-facing dashboard for note entry / file upload.",
            "Live Prediction Pipeline: Transforms input text using serialized TF-IDF vectorizer.",
            "Confidence Output: Returns predicted specialty and classification confidence percentage."
        ])
    ]

    for idx, (title, col, bullets) in enumerate(stages):
        sy = Inches(1.3) + idx * Inches(1.85)
        c = add_card(slide, r_x, sy, c_w, Inches(1.72), bg_color=WHITE, border_color=CARD_BORDER)
        # Left accent stripe
        stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, r_x, sy, Inches(0.08), Inches(1.72))
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = col
        stripe.line.fill.background()

        tb = slide.shapes.add_textbox(r_x + Inches(0.2), sy + Inches(0.1), c_w - Inches(0.35), Inches(1.52))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = col

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"•  {b}"
            pb.font.size = Pt(8.5)
            pb.font.color.rgb = SLATE_BODY
            pb.space_before = Pt(2)


def build_slide_13(prs):
    """SLIDE 13: CURRENT PROGRESS AND NEXT STEPS"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Current Project Progress & Implementation Roadmap", "Progress & Roadmap", 13)

    col_w = Inches(5.72)
    # Left: Current Progress (Completed)
    add_card(slide, Inches(0.8), Inches(1.3), col_w, Inches(4.5), bg_color=WHITE, border_color=RGBColor(187, 247, 208))
    tb_cp = slide.shapes.add_textbox(Inches(1.05), Inches(1.45), col_w - Inches(0.5), Inches(4.2))
    tf_cp = tb_cp.text_frame
    tf_cp.word_wrap = True

    p1 = tf_cp.paragraphs[0]
    p1.text = "CURRENT PROGRESS (PHASE 1 / SPRINT RELEASE I)"
    p1.font.size = Pt(12)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(22, 101, 52)

    progress_items = [
        ("Comprehensive Literature Review", "Surveyed clinical NLP and machine learning papers, establishing preprocessing standards."),
        ("Dataset Acquisition & Cleaning Audit", "Acquired Kaggle MTSamples (4,999 records); identified and pruned 33 blank transcripts."),
        ("Complete Exploratory Data Analysis", "Generated 6 specialized visual distributions covering missing values, class imbalance, and text lengths."),
        ("Class Imbalance Profiling", "Characterized severe class skew across 40 specialties, formulating stratified sampling strategy."),
        ("NLP Preprocessing Pipeline Design", "Finalized 5-step sequence: Lowercasing, character cleaning, stop-word removal, and lemmatization."),
        ("TF-IDF Vectorization Architecture", "Selected unigram/bigram tokenization with sublinear term-frequency scaling and L2 normalization."),
        ("Model & Ensemble Architecture Formulated", "Selected SVM (calibrated), RF, LR, MNB and soft voting probability consensus aggregation.")
    ]

    for h, b in progress_items:
        p = tf_cp.add_paragraph()
        p.text = f"✓  {h}: "
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(4)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.size = Pt(8.5)
        r.font.color.rgb = SLATE_BODY

    # Right: Next Steps (Planned Implementation)
    add_card(slide, Inches(6.8), Inches(1.3), col_w, Inches(4.5), bg_color=WHITE, border_color=RGBColor(191, 219, 254))
    tb_ns = slide.shapes.add_textbox(Inches(7.05), Inches(1.45), col_w - Inches(0.5), Inches(4.2))
    tf_ns = tb_ns.text_frame
    tf_ns.word_wrap = True

    p2 = tf_ns.paragraphs[0]
    p2.text = "PLANNED NEXT STEPS (PHASE 2 / SPRINT RELEASE II)"
    p2.font.size = Pt(12)
    p2.font.bold = True
    p2.font.color.rgb = PRIMARY_BLUE

    next_items = [
        ("Execute Automated Preprocessing Pipeline", "Implement modular Python text cleaner to generate clean tokenized transcripts."),
        ("TF-IDF Matrix Generation & Feature Export", "Fit and persist TF-IDF vectorizer; compile high-dimensional sparse feature matrix."),
        ("Candidate Model Training", "Train SVM, Random Forest, Logistic Regression, and Multinomial Naive Bayes candidate classifiers."),
        ("Soft Voting Ensemble Implementation", "Implement soft consensus probability aggregation combining all four candidate estimators."),
        ("Rigorous Multi-Class Model Evaluation", "Compute multi-class evaluation metrics: Macro/Weighted Precision, Recall, F1, and Confusion Matrices."),
        ("Model Serialization & Web Deployment", "Serialize trained ensemble with Joblib; build interactive clinician dashboard using Flask."),
        ("System Testing & Validation", "Validate inference latency, specialty prediction accuracy, and confidence score reliability.")
    ]

    for h, b in next_items:
        p = tf_ns.add_paragraph()
        p.text = f"→  {h}: "
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = NAVY
        p.space_before = Pt(4)
        r = p.add_run()
        r.text = b
        r.font.bold = False
        r.font.size = Pt(8.5)
        r.font.color.rgb = SLATE_BODY

    # Bottom Milestone Banner
    c_bot = add_card(slide, Inches(0.8), Inches(5.95), Inches(11.72), Inches(0.8), bg_color=RGBColor(240, 253, 250), border_color=RGBColor(153, 246, 228))
    tb_bot = slide.shapes.add_textbox(Inches(1.0), Inches(6.02), Inches(11.32), Inches(0.65))
    tf_b = tb_bot.text_frame
    tf_b.word_wrap = True
    pb1 = tf_b.paragraphs[0]
    pb1.text = "CURRENT STATUS SUMMARY & MILESTONE ALIGNMENT"
    pb1.font.size = Pt(10)
    pb1.font.bold = True
    pb1.font.color.rgb = TEAL
    pb2 = tf_b.add_paragraph()
    pb2.text = "The project has successfully completed the literature review, dataset exploration, and architectural design phases (Sprint Release I). The implementation phase is now commencing according to the project timeline."
    pb2.font.size = Pt(8.5)
    pb2.font.color.rgb = SLATE_BODY


def build_slide_14(prs):
    """SLIDE 14: PROJECT TIMELINE & MILESTONE SCHEDULE"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header_footer(slide, "Project Timeline & Milestone Schedule", "Project Timeline", 14)

    # Subtitle / Summary info banner
    c_top = add_card(slide, Inches(0.8), Inches(1.22), Inches(11.733), Inches(0.52),
                     bg_color=RGBColor(240, 249, 255), border_color=RGBColor(186, 230, 253))
    tb_top = slide.shapes.add_textbox(Inches(0.95), Inches(1.28), Inches(11.4), Inches(0.42))
    tf_top = tb_top.text_frame
    tf_top.word_wrap = True
    p_t = tf_top.paragraphs[0]
    p_t.text = "ACADEMIC TIMELINE & PRESENTATION MILESTONES (SEMESTER 3 MCA MINI PROJECT)"
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(9.5)
    p_t.font.bold = True
    p_t.font.color.rgb = PRIMARY_BLUE

    # 16-row, 2-column Table matching Chapter 3 Table 3.1
    table_shape = slide.shapes.add_table(16, 2, Inches(0.8), Inches(1.85), Inches(11.733), Inches(4.95))
    table = table_shape.table
    table.columns[0].width = Inches(3.0)
    table.columns[1].width = Inches(8.733)

    # Header Row
    headers = ["Period / Date", "Planned Activity / Presentation Milestone"]
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        cell.margin_top = Inches(0.04)
        cell.margin_bottom = Inches(0.04)
        cell.margin_left = Inches(0.12)
        cell.margin_right = Inches(0.12)
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_HEADING
        p.font.size = Pt(10.0)
        p.font.bold = True
        p.font.color.rgb = WHITE

    timeline_data = [
        ("Week 1–2", "Dataset Collection, Exploratory Data Analysis, and Initial Data Cleaning", False, "done"),
        ("21.07.2026", "Project Proposal Approval", True, "done"),
        ("Week 3–4", "Clinical Text Preprocessing, Medical Stop-word Removal, and Lemmatization", False, "done"),
        ("Week 5", "TF-IDF Feature Extraction and Feature Representation Analysis", False, "done"),
        ("08.09.2026", "First Project Presentation (Current Milestone — Phase 1 Faculty Review)", True, "current"),
        ("09.09.2026", "Sprint Release I (Dataset Exploration & Pipeline Architecture Completed)", True, "current"),
        ("Week 6", "Candidate ML Model Training (SVM, Random Forest, Logistic Regression, MNB) and Baseline Evaluation", False, "planned"),
        ("18.09.2026", "Sprint Release II", True, "planned"),
        ("Week 7–8", "Soft Voting Ensemble Formulation, Grid Search Hyperparameter Tuning, and Web UI Design", False, "planned"),
        ("29.09.2026 – 30.09.2026", "Interim Project Presentation", True, "planned"),
        ("Week 9", "Flask Web Application Integration, Route Setup, and Serialized Pipeline Deployment", False, "planned"),
        ("09.10.2026", "Sprint Release III", True, "planned"),
        ("Week 10–11", "Multi-Class Evaluation, Confusion Matrix Analysis, Threshold Tuning, and System Testing", False, "planned"),
        ("22.10.2026 – 23.10.2026", "Final Project Presentation", True, "planned"),
        ("30.10.2026", "Final Report Submission", True, "planned")
    ]

    for row_idx, (period, activity, is_milestone, status) in enumerate(timeline_data, start=1):
        cell_date = table.cell(row_idx, 0)
        cell_act = table.cell(row_idx, 1)

        # Background color
        if status == "current":
            bg_col = RGBColor(239, 246, 255) # Highlight current milestone
        elif row_idx % 2 == 1:
            bg_col = WHITE
        else:
            bg_col = RGBColor(248, 250, 252)

        for cell in (cell_date, cell_act):
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            cell.margin_top = Inches(0.02)
            cell.margin_bottom = Inches(0.02)
            cell.margin_left = Inches(0.12)
            cell.margin_right = Inches(0.12)

        # Date text
        p_d = cell_date.text_frame.paragraphs[0]
        p_d.text = period
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(8.8)
        p_d.font.bold = is_milestone or (status == "current")
        p_d.font.color.rgb = PRIMARY_BLUE if status == "current" else (NAVY if is_milestone else SLATE_BODY)

        # Activity text
        p_a = cell_act.text_frame.paragraphs[0]
        p_a.text = activity
        p_a.font.name = FONT_BODY
        p_a.font.size = Pt(8.8)
        p_a.font.bold = is_milestone or (status == "current")
        p_a.font.color.rgb = PRIMARY_BLUE if status == "current" else (NAVY if is_milestone else SLATE_BODY)


def build_slide_15(prs):
    """SLIDE 15: THANK YOU & QUESTIONS"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Left decorative bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(0.2), Inches(5.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = PRIMARY_BLUE
    bar.line.fill.background()

    # Thank You Main Text
    tb = slide.shapes.add_textbox(Inches(1.3), Inches(1.3), Inches(10.5), Inches(1.3))
    tf = tb.text_frame
    p1 = tf.paragraphs[0]
    p1.text = "Thank You!"
    p1.font.name = FONT_HEADING
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = NAVY

    p2 = tf.add_paragraph()
    p2.text = "Questions & Discussion"
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = TEAL
    p2.space_before = Pt(4)

    # Project Title Card
    c_proj = add_card(slide, Inches(1.3), Inches(2.9), Inches(10.5), Inches(1.2), bg_color=RGBColor(248, 250, 252), border_color=CARD_BORDER)
    tb_pj = slide.shapes.add_textbox(Inches(1.5), Inches(3.0), Inches(10.1), Inches(1.0))
    tf_pj = tb_pj.text_frame
    tf_pj.word_wrap = True
    p_pj1 = tf_pj.paragraphs[0]
    p_pj1.text = "PROJECT TITLE"
    p_pj1.font.size = Pt(9.5)
    p_pj1.font.bold = True
    p_pj1.font.color.rgb = PRIMARY_BLUE
    p_pj2 = tf_pj.add_paragraph()
    p_pj2.text = "Medical Specialty Classification using TF-IDF and Ensemble Machine Learning"
    p_pj2.font.size = Pt(16)
    p_pj2.font.bold = True
    p_pj2.font.color.rgb = NAVY

    # Metadata Grid
    c_meta1 = add_card(slide, Inches(1.3), Inches(4.35), Inches(5.1), Inches(1.8), bg_color=WHITE, border_color=CARD_BORDER)
    tb_m1 = slide.shapes.add_textbox(Inches(1.5), Inches(4.45), Inches(4.7), Inches(1.5))
    tf_m1 = tb_m1.text_frame
    pm1 = tf_m1.paragraphs[0]
    pm1.text = "STUDENT DETAILS"
    pm1.font.size = Pt(9.5)
    pm1.font.bold = True
    pm1.font.color.rgb = TEAL
    pm2 = tf_m1.add_paragraph()
    pm2.text = "Jiphin George  (MAC25MCA-2033)"
    pm2.font.size = Pt(13)
    pm2.font.bold = True
    pm2.font.color.rgb = NAVY
    pm3 = tf_m1.add_paragraph()
    pm3.text = "Master of Computer Applications (MCA - S3)\nDepartment of Computer Applications"
    pm3.font.size = Pt(10)
    pm3.font.color.rgb = SLATE_BODY

    c_meta2 = add_card(slide, Inches(6.6), Inches(4.35), Inches(5.2), Inches(1.8), bg_color=WHITE, border_color=CARD_BORDER)
    tb_m2 = slide.shapes.add_textbox(Inches(6.8), Inches(4.45), Inches(4.8), Inches(1.5))
    tf_m2 = tb_m2.text_frame
    pm4 = tf_m2.paragraphs[0]
    pm4.text = "PROJECT GUIDE & INSTITUTION"
    pm4.font.size = Pt(9.5)
    pm4.font.bold = True
    pm4.font.color.rgb = TEAL
    pm5 = tf_m2.add_paragraph()
    pm5.text = "Mr. Biju Skaria"
    pm5.font.size = Pt(13)
    pm5.font.bold = True
    pm5.font.color.rgb = NAVY
    pm6 = tf_m2.add_paragraph()
    pm6.text = "Associate Professor, Department of Computer Applications\nMar Athanasius College of Engineering, Kothamangalam"
    pm6.font.size = Pt(10)
    pm6.font.color.rgb = SLATE_BODY


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    prs = create_deck()
    print("Building Slide 1: Title Slide...")
    build_slide_1(prs)
    print("Building Slide 2: Problem Statement & Overview...")
    build_slide_2(prs)
    print("Building Slide 3: Literature Review Overview...")
    build_slide_3(prs)
    print("Building Slide 4: Summary of Research Papers...")
    build_slide_4(prs)
    print("Building Slide 5: Dataset Overview...")
    build_slide_5(prs)
    print("Building Slide 6: Dataset Quality & Missing Values...")
    build_slide_6(prs)
    print("Building Slide 7: Medical Specialty Distribution...")
    build_slide_7(prs)
    print("Building Slide 8: Clinical Text Analysis...")
    build_slide_8(prs)
    print("Building Slide 9: Specialty-wise Text Length...")
    build_slide_9(prs)
    print("Building Slide 10: Proposed Algorithms...")
    build_slide_10(prs)
    print("Building Slide 11: Ensemble Learning Approach...")
    build_slide_11(prs)
    print("Building Slide 12: Project Pipeline...")
    build_slide_12(prs)
    print("Building Slide 13: Progress & Next Steps...")
    build_slide_13(prs)
    print("Building Slide 14: Project Timeline & Milestones...")
    build_slide_14(prs)
    print("Building Slide 15: Thank You & Q&A...")
    build_slide_15(prs)

    output_path = "Medical_Specialty_Classification_First_Presentation.pptx"
    try:
        prs.save(output_path)
        print(f"\nSuccessfully generated {len(prs.slides)}-slide presentation: '{output_path}'")
    except PermissionError:
        output_path_alt = "Medical_Specialty_Classification_First_Presentation_v2.pptx"
        prs.save(output_path_alt)
        print(f"\nPrimary file was open in PowerPoint. Successfully saved {len(prs.slides)}-slide presentation to: '{output_path_alt}'")

if __name__ == '__main__':
    main()
