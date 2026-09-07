import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

SRC_PPTX = r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation.pptx"
BACKUP_PPTX = r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation_backup.pptx"
OUTPUT_PPTX = r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation.pptx"

# First, create a backup
prs = pptx.Presentation(SRC_PPTX)
prs.save(BACKUP_PPTX)
print(f"Backup saved to: {BACKUP_PPTX}")

# Colors
DARK_NAVY = RGBColor(0x0B, 0x1F, 0x3A)
CARD_NAVY = RGBColor(0x13, 0x29, 0x4B)
TEAL_ACCENT = RGBColor(0x0E, 0x7C, 0x86)
CYAN_ACCENT = RGBColor(0x00, 0xE5, 0xFF)
LIGHT_TEAL = RGBColor(0x9F, 0xD8, 0xDB)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
SLATE_TEXT = RGBColor(0x33, 0x41, 0x55)
MUTED_TEXT = RGBColor(0x64, 0x74, 0x8B)
BORDER_GRAY = RGBColor(0xE2, 0xE8, 0xF0)
LIGHT_BG = RGBColor(0xF8, 0xFA, 0xFC)
CHECK_GREEN = RGBColor(0x16, 0xA3, 0x4A)
STAR_GOLD = RGBColor(0xD9, 0x77, 0x06)
ARROW_BLUE = RGBColor(0x25, 0x63, 0xEB)

# ==========================================
# 1. UPDATE SLIDE 1 (TITLE & INTRO)
# ==========================================
s1 = prs.slides[0]

# Shapes 8 and 9 were:
# Text 8: "Department of Computer Applications"
# Text 9: "Mar Athanasius College of Engineering, Kothamangalam"
# We will remove them or clear them so they don't overlap with cards
for sh in list(s1.shapes):
    if sh.has_text_frame:
        t = sh.text.strip()
        if t in ["Department of Computer Applications", "Mar Athanasius College of Engineering, Kothamangalam"]:
            # Clear text and minimize shape
            sh.text = ""
            sh.left = Inches(0)
            sh.top = Inches(0)
            sh.width = Inches(0)
            sh.height = Inches(0)

# Adjust badges position if needed
# Badges are shapes with left around 0.90 to 4.70 and top around 6.85
# Let's move them slightly down to top=6.75 in to leave plenty of room for the cards
for sh in s1.shapes:
    if sh.top >= Inches(6.5):
        sh.top = Inches(6.75)

# Add Presenter Card
card1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.90), Inches(4.70), Inches(5.40), Inches(1.75))
card1.fill.solid()
card1.fill.fore_color.rgb = RGBColor(0x10, 0x28, 0x4A)
card1.line.color.rgb = TEAL_ACCENT
card1.line.width = Pt(1.5)

tf1 = card1.text_frame
tf1.word_wrap = True
tf1.margin_left = Inches(0.25)
tf1.margin_right = Inches(0.25)
tf1.margin_top = Inches(0.20)
tf1.margin_bottom = Inches(0.20)

# Presenter Header
p = tf1.paragraphs[0]
p.text = "PRESENTED BY"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = LIGHT_TEAL
p.space_after = Pt(4)

# Presenter Name
p = tf1.add_paragraph()
p.text = "Jiphin George"
p.font.name = "Cambria"
p.font.size = Pt(19)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_after = Pt(4)

# Presenter Reg No
p = tf1.add_paragraph()
p.text = "Register No: MAC25MCA-2033"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = False
p.font.color.rgb = RGBColor(0xEE, 0xF2, 0xF6)
p.space_after = Pt(2)

# Presenter Course
p = tf1.add_paragraph()
p.text = "Master of Computer Applications (MCA)"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = False
p.font.color.rgb = RGBColor(0xBD, 0xCB, 0xDD)

# Add Project Guide Card
card2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.60), Inches(4.70), Inches(5.80), Inches(1.75))
card2.fill.solid()
card2.fill.fore_color.rgb = RGBColor(0x10, 0x28, 0x4A)
card2.line.color.rgb = TEAL_ACCENT
card2.line.width = Pt(1.5)

tf2 = card2.text_frame
tf2.word_wrap = True
tf2.margin_left = Inches(0.25)
tf2.margin_right = Inches(0.25)
tf2.margin_top = Inches(0.20)
tf2.margin_bottom = Inches(0.20)

# Guide Header
p = tf2.paragraphs[0]
p.text = "PROJECT GUIDE"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = LIGHT_TEAL
p.space_after = Pt(4)

# Guide Name
p = tf2.add_paragraph()
p.text = "Prof. Biju Skaria"
p.font.name = "Cambria"
p.font.size = Pt(19)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_after = Pt(4)

# Guide Dept
p = tf2.add_paragraph()
p.text = "Department of Computer Applications"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = False
p.font.color.rgb = RGBColor(0xEE, 0xF2, 0xF6)
p.space_after = Pt(2)

# Guide College
p = tf2.add_paragraph()
p.text = "Mar Athanasius College of Engineering, Kothamangalam"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = False
p.font.color.rgb = RGBColor(0xBD, 0xCB, 0xDD)

print("Slide 1 updated with student and guide cards.")

# ==========================================
# 2. UPDATE SLIDE 13 (SVM WORDING)
# ==========================================
s13 = prs.slides[12]
for sh in s13.shapes:
    if sh.has_text_frame and "Standard Linear SVM" in sh.text:
        sh.text = "SVM is used as one of the base machine learning classifiers for medical specialty classification. It learns optimal decision boundaries between different medical specialty categories using the TF-IDF feature representation within the soft-voting ensemble."
        if sh.text_frame.paragraphs:
            p = sh.text_frame.paragraphs[0]
            p.font.name = "Calibri"
            p.font.size = Pt(11.5)
            p.font.color.rgb = RGBColor(0x16, 0x21, 0x3E)
print("Slide 13 SVM note updated.")

# ==========================================
# 3. REBUILD SLIDE 18: PROGRESS & ROADMAP
# ==========================================
s18 = prs.slides[17]
# Keep header and footer, clear inner shapes
header_footer_texts = [
    "MCA MINI PROJECT | GUI DESIGN",
    "Proposed Web Application",
    "Department of Computer Applications | MACE",
    "Mar Athanasius College of Engineering, Kothamangalam",
    "Slide 18 of 20"
]

# Identify shapes to delete or update
shapes_to_remove = []
for sh in s18.shapes:
    is_hf = False
    if sh.has_text_frame:
        for t in header_footer_texts:
            if t in sh.text:
                is_hf = True
                break
    if not is_hf:
        shapes_to_remove.append(sh)

# Remove inner shapes
sp_tree = s18.shapes._spTree
for sh in shapes_to_remove:
    sp_tree.remove(sh._element)

# Update header and title on Slide 18
for sh in s18.shapes:
    if sh.has_text_frame:
        if "MCA MINI PROJECT | GUI DESIGN" in sh.text:
            sh.text = "MCA MINI PROJECT | PROGRESS & ROADMAP"
            p = sh.text_frame.paragraphs[0]
            p.font.name = "Calibri"
            p.font.size = Pt(10.5)
            p.font.bold = True
            p.font.color.rgb = WHITE
        elif "Proposed Web Application" in sh.text:
            sh.text = "Current Project Progress & Implementation Roadmap"
            p = sh.text_frame.paragraphs[0]
            p.font.name = "Cambria"
            p.font.size = Pt(27)
            p.font.bold = True
            p.font.color.rgb = DARK_NAVY

# Add Slide 18 Cards: Left (Completed Deliverables) & Right (Upcoming Milestones)
# Left Card
card_prog = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.60), Inches(5.95), Inches(4.50))
card_prog.fill.solid()
card_prog.fill.fore_color.rgb = WHITE
card_prog.line.color.rgb = BORDER_GRAY
card_prog.line.width = Pt(1.2)

tf_cp = card_prog.text_frame
tf_cp.word_wrap = True
tf_cp.margin_left = Inches(0.20)
tf_cp.margin_right = Inches(0.20)
tf_cp.margin_top = Inches(0.18)
tf_cp.margin_bottom = Inches(0.15)

p = tf_cp.paragraphs[0]
p.text = "CURRENT PROGRESS (PHASE 1 / SPRINT RELEASE I)"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT
p.space_after = Pt(6)

items_phase1 = [
    ("✓ Literature Review & Paper Benchmarking", "Surveyed clinical NLP literature (Omar et al., Zhang et al., Blanchard et al.), establishing preprocessing standards."),
    ("✓ Dataset Acquisition & Cleaning Audit", "Acquired Kaggle MTSamples (4,999 cases); identified and removed 33 empty transcription records."),
    ("✓ Exploratory Data Analysis & Visualization", "Executed 6 statistical distributions covering missing values, token lengths, and specialty frequencies."),
    ("✓ Class Imbalance Characterization", "Audited extreme long-tail class skew across 40 medical specialties; formulated stratified sampling strategy."),
    ("✓ NLP Cleaning Pipeline Design", "Finalized sequence: Cleaning, Lowercasing, Alphanumeric Filtering, Stop-word Removal, and Lemmatization."),
    ("✓ TF-IDF Architecture Formulation", "Configured unigram/bigram tokenization with sublinear TF scaling and Euclidean L2 normalization."),
    ("✓ Model & Ensemble Formulation", "Selected SVM, Random Forest, Logistic Regression, and MNB combined via Soft Voting probability consensus.")
]

for title, desc in items_phase1:
    p = tf_cp.add_paragraph()
    r1 = p.add_run()
    r1.text = title + ": "
    r1.font.name = "Calibri"
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = DARK_NAVY
    
    r2 = p.add_run()
    r2.text = desc
    r2.font.name = "Calibri"
    r2.font.size = Pt(9.5)
    r2.font.bold = False
    r2.font.color.rgb = SLATE_TEXT
    p.space_after = Pt(3)

# Right Card
card_road = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.80), Inches(1.60), Inches(6.00), Inches(4.50))
card_road.fill.solid()
card_road.fill.fore_color.rgb = WHITE
card_road.line.color.rgb = BORDER_GRAY
card_road.line.width = Pt(1.2)

tf_rd = card_road.text_frame
tf_rd.word_wrap = True
tf_rd.margin_left = Inches(0.20)
tf_rd.margin_right = Inches(0.20)
tf_rd.margin_top = Inches(0.18)
tf_rd.margin_bottom = Inches(0.15)

p = tf_rd.paragraphs[0]
p.text = "PLANNED NEXT STEPS (PHASE 2 / SPRINT RELEASE II & III)"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = ARROW_BLUE
p.space_after = Pt(6)

items_phase2 = [
    ("→ Full Text Preprocessing Implementation", "Execute the 8-step cleaning module across 4,966 records to produce normalized narrative corpus."),
    ("→ TF-IDF Feature Matrix Generation", "Fit vectorizer strictly on training partition (80:20 split) to eliminate data leakage; transform test set."),
    ("→ Candidate Model Training & Optimization", "Train SVM, Random Forest, Logistic Regression, and Multinomial Naive Bayes classifiers."),
    ("→ Soft Voting Ensemble Development", "Implement weighted/soft probability aggregation combining decision outputs across all base estimators."),
    ("→ Multi-Class Performance Evaluation", "Benchmark multi-class Macro/Weighted Precision, Recall, F1-score, and cross-class Confusion Matrices."),
    ("→ Pipeline Serialization & Web Deployment", "Serialize end-to-end pipeline with Joblib; construct interactive clinician dashboard using Flask."),
    ("→ Validation & Clinical Usability Testing", "Validate latency, prediction confidence calibration, and reliability on unseen clinical records.")
]

for title, desc in items_phase2:
    p = tf_rd.add_paragraph()
    r1 = p.add_run()
    r1.text = title + ": "
    r1.font.name = "Calibri"
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = DARK_NAVY
    
    r2 = p.add_run()
    r2.text = desc
    r2.font.name = "Calibri"
    r2.font.size = Pt(9.5)
    r2.font.bold = False
    r2.font.color.rgb = SLATE_TEXT
    p.space_after = Pt(3)

# Bottom Status Banner
banner18 = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(6.20), Inches(12.30), Inches(0.70))
banner18.fill.solid()
banner18.fill.fore_color.rgb = RGBColor(0xEE, 0xF6, 0xF6)
banner18.line.color.rgb = TEAL_ACCENT
banner18.line.width = Pt(1)

tf_b18 = banner18.text_frame
tf_b18.word_wrap = True
tf_b18.margin_left = Inches(0.20)
tf_b18.margin_right = Inches(0.20)
tf_b18.margin_top = Inches(0.12)
tf_b18.margin_bottom = Inches(0.10)

p = tf_b18.paragraphs[0]
r = p.add_run()
r.text = "Phase 1 Status: "
r.font.name = "Calibri"
r.font.size = Pt(11)
r.font.bold = True
r.font.color.rgb = TEAL_ACCENT

r = p.add_run()
r.text = "Literature Review, Data Exploration, Preprocessing Pipeline, and Ensemble Architecture are fully completed (Sprint Release I). The project is on schedule to commence candidate model training."
r.font.name = "Calibri"
r.font.size = Pt(10.5)
r.font.bold = False
r.font.color.rgb = DARK_NAVY

print("Slide 18 rebuilt as Progress & Implementation Roadmap.")

# ==========================================
# 4. REBUILD SLIDE 19: PROJECT TIMELINE
# ==========================================
s19 = prs.slides[18]
header_footer_texts_19 = [
    "MCA MINI PROJECT | GUI DESIGN",
    "GUI Components & Current Project Progress",
    "Department of Computer Applications | MACE",
    "Mar Athanasius College of Engineering, Kothamangalam",
    "Slide 19 of 20"
]

shapes_to_remove_19 = []
for sh in s19.shapes:
    is_hf = False
    if sh.has_text_frame:
        for t in header_footer_texts_19:
            if t in sh.text:
                is_hf = True
                break
    if not is_hf:
        shapes_to_remove_19.append(sh)

sp_tree_19 = s19.shapes._spTree
for sh in shapes_to_remove_19:
    sp_tree_19.remove(sh._element)

# Update header and title on Slide 19
for sh in s19.shapes:
    if sh.has_text_frame:
        if "MCA MINI PROJECT | GUI DESIGN" in sh.text:
            sh.text = "MCA MINI PROJECT | PROJECT TIMELINE"
            p = sh.text_frame.paragraphs[0]
            p.font.name = "Calibri"
            p.font.size = Pt(10.5)
            p.font.bold = True
            p.font.color.rgb = WHITE
        elif "GUI Components" in sh.text:
            sh.text = "Project Timeline & Milestone Schedule"
            p = sh.text_frame.paragraphs[0]
            p.font.name = "Cambria"
            p.font.size = Pt(27)
            p.font.bold = True
            p.font.color.rgb = DARK_NAVY

# Sub-banner for Timeline
subbanner = s19.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.50), Inches(12.30), Inches(0.40))
subbanner.fill.solid()
subbanner.fill.fore_color.rgb = RGBColor(0xEE, 0xF6, 0xF6)
subbanner.line.color.rgb = TEAL_ACCENT
subbanner.line.width = Pt(1)

tf_sb = subbanner.text_frame
tf_sb.margin_top = Inches(0.06)
tf_sb.margin_bottom = Inches(0.06)
p = tf_sb.paragraphs[0]
p.text = "ACADEMIC TIMELINE & PRESENTATION MILESTONES (SEMESTER 3 MCA MINI PROJECT)"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT
p.alignment = PP_ALIGN.CENTER

# Two Milestone Cards: Left (Phase 1) & Right (Phases 2 & 3)
# Left Card (Phase 1)
tl_card1 = s19.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(2.00), Inches(5.95), Inches(4.90))
tl_card1.fill.solid()
tl_card1.fill.fore_color.rgb = WHITE
tl_card1.line.color.rgb = BORDER_GRAY
tl_card1.line.width = Pt(1.2)

tf_tl1 = tl_card1.text_frame
tf_tl1.word_wrap = True
tf_tl1.margin_left = Inches(0.18)
tf_tl1.margin_right = Inches(0.18)
tf_tl1.margin_top = Inches(0.15)
tf_tl1.margin_bottom = Inches(0.12)

p = tf_tl1.paragraphs[0]
p.text = "PHASE 1: FOUNDATION & SPRINT RELEASE I"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT
p.space_after = Pt(4)

milestones_p1 = [
    ("✓  [17.07.2026]  Project Proposal & Synopsis Approval by Guide", "Formal approval of project scope, objectives, and feasibility by faculty guide.", CHECK_GREEN),
    ("✓  [20.07.2026 – 21.07.2026]  Project Proposal Presentation", "Presented proposal before Department Project Approval Committee.", CHECK_GREEN),
    ("✓  [Weeks 1–2]  Dataset Collection & Exploratory Data Analysis", "Acquired Kaggle MTSamples (4,999 records); audited nulls and generated 6 EDA plots.", CHECK_GREEN),
    ("✓  [Weeks 3–4]  Clinical Text Preprocessing Pipeline", "Designed 5-step sequence: Cleaning, Lowercasing, Tokenization, Stop-words, Lemmatization.", CHECK_GREEN),
    ("✓  [Week 5]  TF-IDF Vectorization Architecture", "Formulated unigram/bigram tokenization with sublinear scaling and sparse matrix layout.", CHECK_GREEN),
    ("★  [08.09.2026]  First Project Presentation ★", "Current Milestone — Phase 1 Faculty Review & Initial Progress Defense.", STAR_GOLD),
    ("★  [09.09.2026]  Sprint Release I ★", "Formal submission: EDA diagrams, architecture specifications, and Phase 1 report.", STAR_GOLD)
]

for title, desc, color in milestones_p1:
    p = tf_tl1.add_paragraph()
    r1 = p.add_run()
    r1.text = title + "\n"
    r1.font.name = "Calibri"
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = color
    
    r2 = p.add_run()
    r2.text = "    " + desc
    r2.font.name = "Calibri"
    r2.font.size = Pt(8.5)
    r2.font.bold = False
    r2.font.color.rgb = SLATE_TEXT
    p.space_after = Pt(3)

# Right Card (Phases 2 & 3)
tl_card2 = s19.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.80), Inches(2.00), Inches(6.00), Inches(4.90))
tl_card2.fill.solid()
tl_card2.fill.fore_color.rgb = WHITE
tl_card2.line.color.rgb = BORDER_GRAY
tl_card2.line.width = Pt(1.2)

tf_tl2 = tl_card2.text_frame
tf_tl2.word_wrap = True
tf_tl2.margin_left = Inches(0.18)
tf_tl2.margin_right = Inches(0.18)
tf_tl2.margin_top = Inches(0.15)
tf_tl2.margin_bottom = Inches(0.12)

p = tf_tl2.paragraphs[0]
p.text = "PHASES 2 & 3: MODEL BUILDING, ENSEMBLE & DEPLOYMENT"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = ARROW_BLUE
p.space_after = Pt(4)

milestones_p2 = [
    ("→  [Week 6]  Candidate Model Training & Baseline Evaluation", "Train SVM, Random Forest, Logistic Regression, and Multinomial Naive Bayes.", ARROW_BLUE),
    ("★  [18.09.2026]  Sprint Release II ★", "Milestone release: Trained baseline classifiers and preliminary metrics.", STAR_GOLD),
    ("→  [Week 7]  Hyperparameter Tuning & Model Comparison", "Systematic tuning and comparative performance profiling across candidate estimators.", ARROW_BLUE),
    ("→  [Week 8]  Soft Voting Ensemble Implementation", "Construct soft voting ensemble; aggregate consensus probability distributions.", ARROW_BLUE),
    ("★  [29.09.2026 – 30.09.2026]  Interim Project Presentation ★", "Progress review and working model demonstration before faculty committee.", STAR_GOLD),
    ("→  [Week 9]  Flask Web Integration & Serialization", "Serialize pipeline with Joblib; build interactive clinician UI for live inference.", ARROW_BLUE),
    ("★  [09.10.2026]  Sprint Release III ★", "Integrated system release: Flask web application and serialized ensemble.", STAR_GOLD),
    ("→  [Weeks 10–11]  Evaluation & System Testing", "Multi-class metrics (Macro F1, Recall), confusion matrix analysis, and validation.", ARROW_BLUE),
    ("★  [22.10.2026 – 23.10.2026]  Final Project Presentation ★", "Comprehensive final project defense before the examination board.", STAR_GOLD),
    ("★  [30.10.2026]  Final Report Submission ★", "Submission of finalized documentation, technical report, and source code.", STAR_GOLD)
]

for title, desc, color in milestones_p2:
    p = tf_tl2.add_paragraph()
    r1 = p.add_run()
    r1.text = title + "\n"
    r1.font.name = "Calibri"
    r1.font.size = Pt(9.2)
    r1.font.bold = True
    r1.font.color.rgb = color
    
    r2 = p.add_run()
    r2.text = "    " + desc
    r2.font.name = "Calibri"
    r2.font.size = Pt(8.2)
    r2.font.bold = False
    r2.font.color.rgb = SLATE_TEXT
    p.space_after = Pt(2)

print("Slide 19 rebuilt as Project Timeline & Milestone Schedule.")

# ==========================================
# 5. UPDATE SLIDE 20 (CONCLUSION SVM NOTE)
# ==========================================
s20 = prs.slides[19]
for sh in s20.shapes:
    if sh.has_text_frame and "Calibrate SVM probabilities" in sh.text:
        sh.text = sh.text.replace("Calibrate SVM probabilities and build the Soft Voting Ensemble", "Build the Soft Voting Ensemble combining SVM, Random Forest, Logistic Regression and MNB")
print("Slide 20 updated.")

# Save modified presentation
prs.save(OUTPUT_PPTX)
print(f"Successfully saved updated presentation to: {OUTPUT_PPTX}")
