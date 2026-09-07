import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

PPTX_PATH = r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation.pptx"
prs = pptx.Presentation(PPTX_PATH)

# ==========================================
# PALETTE DEFINITIONS
# ==========================================
NAVY_BG = RGBColor(0x0A, 0x19, 0x2F)       # Deep rich navy
NAVY_CARD = RGBColor(0x11, 0x22, 0x40)     # Luminous navy card
TEAL_ACCENT = RGBColor(0x0E, 0x7C, 0x86)   # Teal primary
CYAN_BRIGHT = RGBColor(0x00, 0xE5, 0xFF)   # Electric cyan
CYAN_LIGHT = RGBColor(0x38, 0xBD, 0xF8)    # Luminous cyan text
WHITE = RGBColor(0xFF, 0xFF, 0xFF)         # Pure white
ICE_WHITE = RGBColor(0xF1, 0xF5, 0xF9)     # Soft white / ice text
MUTED_SLATE = RGBColor(0x94, 0xA3, 0xB8)   # Subdued text
GREEN_CHECK = RGBColor(0x4A, 0xDE, 0x80)   # Vibrant green
GOLD_STAR = RGBColor(0xFB, 0xBF, 0x24)     # Golden star
BLUE_ARROW = RGBColor(0x60, 0xA5, 0xFA)    # Vibrant blue
PURPLE_ACCENT = RGBColor(0xC0, 0x84, 0xFC) # Vibrant lavender
DARK_TEXT = RGBColor(0x0F, 0x17, 0x2A)     # Dark slate for light cards
BODY_TEXT = RGBColor(0x33, 0x41, 0x55)     # Slate body for light cards
SLATE_DARK = RGBColor(0x33, 0x41, 0x55)    # Slate dark text
BORDER_GRAY = RGBColor(0xCB, 0xD5, 0xE1)   # Border for light cards
LIGHT_BOX_BG = RGBColor(0xF8, 0xFA, 0xFC)  # Crisp light background

# =========================================================================
# 1. OVERHAUL SLIDE 1 (TITLE SLIDE - VIBRANT, MODERN, PREMIUM)
# =========================================================================
s1 = prs.slides[0]
sp_tree1 = s1.shapes._spTree
for sh in list(s1.shapes):
    sp_tree1.remove(sh._element)

# Slide 1 Background: Solid Deep Navy
s1.background.fill.solid()
s1.background.fill.fore_color.rgb = NAVY_BG

# Decorative glowing top accent bar
bar1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
bar1.fill.solid()
bar1.fill.fore_color.rgb = CYAN_BRIGHT
bar1.line.fill.background()

# College Header
col_hdr = s1.shapes.add_textbox(Inches(0.90), Inches(0.40), Inches(11.50), Inches(0.40))
tf_ch = col_hdr.text_frame
p = tf_ch.paragraphs[0]
p.text = "MAR ATHANASIUS COLLEGE OF ENGINEERING, KOTHAMANGALAM"
p.font.name = "Calibri"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = CYAN_LIGHT

# Pill Badge
pill1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.90), Inches(0.95), Inches(4.20), Inches(0.38))
pill1.fill.solid()
pill1.fill.fore_color.rgb = TEAL_ACCENT
pill1.line.color.rgb = CYAN_BRIGHT
pill1.line.width = Pt(1)
tf_p1 = pill1.text_frame
p = tf_p1.paragraphs[0]
p.text = "MCA MINI PROJECT  |  FIRST PRESENTATION"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Project Main Title
title_box = s1.shapes.add_textbox(Inches(0.90), Inches(1.50), Inches(11.50), Inches(1.80))
tf_tb = title_box.text_frame
tf_tb.word_wrap = True
p = tf_tb.paragraphs[0]
p.text = "Medical Specialty Classification Using TF-IDF\nand Ensemble Machine Learning"
p.font.name = "Cambria"
p.font.size = Pt(36)
p.font.bold = True
p.font.color.rgb = WHITE

# Two Vibrant Cards: Presenter & Guide (Positioned nicely with balanced spacing)
# Presenter Card (Left)
c_pres = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.90), Inches(3.75), Inches(5.50), Inches(2.35))
c_pres.fill.solid()
c_pres.fill.fore_color.rgb = NAVY_CARD
c_pres.line.color.rgb = CYAN_BRIGHT
c_pres.line.width = Pt(2)

tf_cp = c_pres.text_frame
tf_cp.word_wrap = True
tf_cp.margin_left = Inches(0.30)
tf_cp.margin_top = Inches(0.22)

p = tf_cp.paragraphs[0]
p.text = "PRESENTED BY"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = CYAN_LIGHT
p.space_after = Pt(6)

p = tf_cp.add_paragraph()
p.text = "Jiphin George"
p.font.name = "Cambria"
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_after = Pt(6)

p = tf_cp.add_paragraph()
p.text = "Register No: MAC25MCA-2033"
p.font.name = "Calibri"
p.font.size = Pt(13)
p.font.bold = False
p.font.color.rgb = ICE_WHITE
p.space_after = Pt(3)

p = tf_cp.add_paragraph()
p.text = "Course: Master of Computer Applications (MCA)"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = False
p.font.color.rgb = MUTED_SLATE

# Guide Card (Right)
c_guide = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(3.75), Inches(5.65), Inches(2.35))
c_guide.fill.solid()
c_guide.fill.fore_color.rgb = NAVY_CARD
c_guide.line.color.rgb = GREEN_CHECK
c_guide.line.width = Pt(2)

tf_cg = c_guide.text_frame
tf_cg.word_wrap = True
tf_cg.margin_left = Inches(0.30)
tf_cg.margin_top = Inches(0.22)

p = tf_cg.paragraphs[0]
p.text = "PROJECT GUIDE"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = GREEN_CHECK
p.space_after = Pt(6)

p = tf_cg.add_paragraph()
p.text = "Prof. Biju Skaria"
p.font.name = "Cambria"
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_after = Pt(6)

p = tf_cg.add_paragraph()
p.text = "Department of Computer Applications"
p.font.name = "Calibri"
p.font.size = Pt(13)
p.font.bold = False
p.font.color.rgb = ICE_WHITE
p.space_after = Pt(3)

p = tf_cg.add_paragraph()
p.text = "Mar Athanasius College of Engineering, Kothamangalam"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = False
p.font.color.rgb = MUTED_SLATE

# Domain Badges at bottom
badges = ["Clinical NLP", "TF-IDF Vectorization", "Supervised ML", "Soft Voting Ensemble", "Flask Deployment"]
b_w = Inches(2.20)
b_gap = Inches(0.12)
b_start = Inches(0.90)
for i, badge_txt in enumerate(badges):
    bx = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, b_start + i * (b_w + b_gap), Inches(6.45), b_w, Inches(0.42))
    bx.fill.solid()
    bx.fill.fore_color.rgb = RGBColor(0x13, 0x32, 0x54)
    bx.line.color.rgb = CYAN_BRIGHT
    bx.line.width = Pt(1)
    tf_b = bx.text_frame
    p = tf_b.paragraphs[0]
    p.text = badge_txt
    p.font.name = "Calibri"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER

print("Slide 1 rebuilt with vibrant colors.")

# =========================================================================
# 2. SLIDE 14: ACTIVITY DIAGRAMS - SVM & MULTINOMIAL NAIVE BAYES
# =========================================================================
s14 = prs.slides[13]
sp_tree14 = s14.shapes._spTree
for sh in list(s14.shapes):
    sp_tree14.remove(sh._element)

# Header & Footers
pill14 = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(0.35), Inches(4.60), Inches(0.32))
pill14.fill.solid()
pill14.fill.fore_color.rgb = TEAL_ACCENT
pill14.line.fill.background()
p = pill14.text_frame.paragraphs[0]
p.text = "MCA MINI PROJECT | DETAILS OF ALGORITHMS"
p.font.name = "Calibri"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = WHITE

tbox14 = s14.shapes.add_textbox(Inches(0.50), Inches(0.72), Inches(12.30), Inches(0.68))
p = tbox14.text_frame.paragraphs[0]
p.text = "Algorithm Activity Diagrams: SVM & Multinomial Naive Bayes"
p.font.name = "Cambria"
p.font.size = Pt(26)
p.font.bold = True
p.font.color.rgb = RGBColor(0x0B, 0x1F, 0x3A)

# Footers
f1 = s14.shapes.add_textbox(Inches(0.50), Inches(7.13), Inches(4.60), Inches(0.30))
p1 = f1.text_frame.paragraphs[0]
p1.text = "Department of Computer Applications | MACE"
p1.font.name = "Calibri"
p1.font.size = Pt(9)
p1.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

f2 = s14.shapes.add_textbox(Inches(4.00), Inches(7.13), Inches(5.33), Inches(0.30))
p2 = f2.text_frame.paragraphs[0]
p2.text = "Mar Athanasius College of Engineering, Kothamangalam"
p2.font.name = "Calibri"
p2.font.size = Pt(9)
p2.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

f3 = s14.shapes.add_textbox(Inches(9.90), Inches(7.13), Inches(2.93), Inches(0.30))
p3 = f3.text_frame.paragraphs[0]
p3.text = "Slide 14 of 20"
p3.font.name = "Calibri"
p3.font.size = Pt(9)
p3.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

# Column 1: Support Vector Machine (SVM) Activity Flow
svm_card = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.50), Inches(5.95), Inches(5.45))
svm_card.fill.solid()
svm_card.fill.fore_color.rgb = WHITE
svm_card.line.color.rgb = TEAL_ACCENT
svm_card.line.width = Pt(1.5)

# SVM Header
svm_hdr = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.65), Inches(5.65), Inches(0.55))
svm_hdr.fill.solid()
svm_hdr.fill.fore_color.rgb = RGBColor(0x0E, 0x7C, 0x86)
svm_hdr.line.fill.background()
p = svm_hdr.text_frame.paragraphs[0]
p.text = "SVM (SUPPORT VECTOR MACHINE) ACTIVITY FLOW"
p.font.name = "Calibri"
p.font.size = Pt(11.5)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

svm_steps = [
    ("1. High-Dimensional Input", "Sparse TF-IDF feature vector x ∈ R^V representing clinical narrative vocabulary."),
    ("2. Linear Decision Mapping", "Constructs decision hyperplane w·x + b = 0 in sparse high-dimensional term space."),
    ("3. Maximum Margin Optimization", "Solves quadratic program: min 1/2 ||w||² subject to y_i(w·x_i + b) ≥ 1 - ξ_i."),
    ("4. Support Vector Identification", "Identifies critical borderline transcripts that define category separation margins."),
    ("5. Platt Probability Scaling", "Calibrates decision distances via sigmoid fitting: P(c|x) = 1 / (1 + exp(A·f(x) + B))."),
    ("6. Class Probability Output", "Outputs calibrated probability distribution across all 40 medical specialty categories.")
]

y_pos = Inches(2.35)
step_h = Inches(0.65)
step_gap = Inches(0.12)
for i, (title, desc) in enumerate(svm_steps):
    box = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), y_pos + i * (step_h + step_gap), Inches(5.65), step_h)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0xF0, 0xFD, 0xFA)
    box.line.color.rgb = RGBColor(0x99, 0xF6, 0xE4)
    box.line.width = Pt(1)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.12)
    tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Calibri"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x0F, 0x76, 0x6E)
    p = tf.add_paragraph()
    p.text = desc
    p.font.name = "Calibri"
    p.font.size = Pt(8.5)
    p.font.bold = False
    p.font.color.rgb = SLATE_DARK

# Column 2: Multinomial Naive Bayes (MNB) Activity Flow
mnb_card = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.80), Inches(1.50), Inches(6.00), Inches(5.45))
mnb_card.fill.solid()
mnb_card.fill.fore_color.rgb = WHITE
mnb_card.line.color.rgb = RGBColor(0x25, 0x63, 0xEB)
mnb_card.line.width = Pt(1.5)

mnb_hdr = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), Inches(1.65), Inches(5.70), Inches(0.55))
mnb_hdr.fill.solid()
mnb_hdr.fill.fore_color.rgb = RGBColor(0x25, 0x63, 0xEB)
mnb_hdr.line.fill.background()
p = mnb_hdr.text_frame.paragraphs[0]
p.text = "MULTINOMIAL NAIVE BAYES ACTIVITY FLOW"
p.font.name = "Calibri"
p.font.size = Pt(11.5)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

mnb_steps = [
    ("1. Term Frequency Vector Input", "Vector of clinical token counts and TF-IDF weights for each vocabulary term t_k."),
    ("2. Prior Class Probability P(c)", "Estimates empirical prior for each specialty: P(c) = N_c / N_total from training data."),
    ("3. Feature Likelihood with Smoothing", "Calculates P(t|c) = (count(t,c) + α) / (Σ count(w,c) + α·|V|) using Laplace smoothing (α=1)."),
    ("4. Log Posterior Accumulation", "Computes log P(c|d) = log P(c) + Σ f_t · log P(t|c) to prevent floating-point underflow."),
    ("5. Softmax Normalization", "Converts log-likelihoods into normalized probability distribution: P(c|d) = exp(s_c)/Σ exp(s_k)."),
    ("6. Class Probability Output", "Generates probabilistic score distribution over 40 categories for ensemble soft voting.")
]

for i, (title, desc) in enumerate(mnb_steps):
    box = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), y_pos + i * (step_h + step_gap), Inches(5.70), step_h)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0xEF, 0xF6, 0xFF)
    box.line.color.rgb = RGBColor(0xBF, 0xDB, 0xFE)
    box.line.width = Pt(1)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.12)
    tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Calibri"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)
    p = tf.add_paragraph()
    p.text = desc
    p.font.name = "Calibri"
    p.font.size = Pt(8.5)
    p.font.bold = False
    p.font.color.rgb = SLATE_DARK

print("Slide 14 rebuilt with SVM & MNB Activity Diagrams.")

# =========================================================================
# 3. SLIDE 15: ACTIVITY DIAGRAMS - RANDOM FOREST & LOGISTIC REGRESSION
# =========================================================================
s15 = prs.slides[14]
sp_tree15 = s15.shapes._spTree
for sh in list(s15.shapes):
    sp_tree15.remove(sh._element)

# Header & Footers
pill15 = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(0.35), Inches(4.60), Inches(0.32))
pill15.fill.solid()
pill15.fill.fore_color.rgb = TEAL_ACCENT
pill15.line.fill.background()
p = pill15.text_frame.paragraphs[0]
p.text = "MCA MINI PROJECT | DETAILS OF ALGORITHMS"
p.font.name = "Calibri"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = WHITE

tbox15 = s15.shapes.add_textbox(Inches(0.50), Inches(0.72), Inches(12.30), Inches(0.68))
p = tbox15.text_frame.paragraphs[0]
p.text = "Algorithm Activity Diagrams: Random Forest & Logistic Regression"
p.font.name = "Cambria"
p.font.size = Pt(26)
p.font.bold = True
p.font.color.rgb = RGBColor(0x0B, 0x1F, 0x3A)

# Footers
f1 = s15.shapes.add_textbox(Inches(0.50), Inches(7.13), Inches(4.60), Inches(0.30))
p1 = f1.text_frame.paragraphs[0]
p1.text = "Department of Computer Applications | MACE"
p1.font.name = "Calibri"
p1.font.size = Pt(9)
p1.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

f2 = s15.shapes.add_textbox(Inches(4.00), Inches(7.13), Inches(5.33), Inches(0.30))
p2 = f2.text_frame.paragraphs[0]
p2.text = "Mar Athanasius College of Engineering, Kothamangalam"
p2.font.name = "Calibri"
p2.font.size = Pt(9)
p2.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

f3 = s15.shapes.add_textbox(Inches(9.90), Inches(7.13), Inches(2.93), Inches(0.30))
p3 = f3.text_frame.paragraphs[0]
p3.text = "Slide 15 of 20"
p3.font.name = "Calibri"
p3.font.size = Pt(9)
p3.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

# Column 1: Random Forest Activity Flow
rf_card = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.50), Inches(5.95), Inches(5.45))
rf_card.fill.solid()
rf_card.fill.fore_color.rgb = WHITE
rf_card.line.color.rgb = RGBColor(0x16, 0xA3, 0x4A)
rf_card.line.width = Pt(1.5)

rf_hdr = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), Inches(1.65), Inches(5.65), Inches(0.55))
rf_hdr.fill.solid()
rf_hdr.fill.fore_color.rgb = RGBColor(0x16, 0xA3, 0x4A)
rf_hdr.line.fill.background()
p = rf_hdr.text_frame.paragraphs[0]
p.text = "RANDOM FOREST (RF) ACTIVITY FLOW"
p.font.name = "Calibri"
p.font.size = Pt(11.5)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

rf_steps = [
    ("1. Dataset & Feature Matrix Input", "Receives training matrix X (TF-IDF features) and multi-class labels Y (40 classes)."),
    ("2. Bootstrap Sampling (Bagging)", "Generates B bootstrap sample sets by sampling rows with replacement to induce diversity."),
    ("3. Random Feature Subspace Split", "At each decision node, randomly selects m = √|V| features and finds optimal split."),
    ("4. Decision Tree Induction", "Recursively splits nodes using Gini Impurity: Gini = 1 - Σ p_i² until stopping criterion."),
    ("5. Forest Ensemble Assembly", "Combines B independently trained decision trees into an uncorrelated forest ensemble."),
    ("6. Ensemble Averaged Probability", "Calculates consensus class probabilities: P_RF(c) = (1/B) Σ P_tree_b(c) across all B trees.")
]

for i, (title, desc) in enumerate(rf_steps):
    box = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.65), y_pos + i * (step_h + step_gap), Inches(5.65), step_h)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0xF0, 0xFD, 0xF4)
    box.line.color.rgb = RGBColor(0xBB, 0xF7, 0xD0)
    box.line.width = Pt(1)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.12)
    tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Calibri"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
    p = tf.add_paragraph()
    p.text = desc
    p.font.name = "Calibri"
    p.font.size = Pt(8.5)
    p.font.bold = False
    p.font.color.rgb = SLATE_DARK

# Column 2: Logistic Regression (LR) Activity Flow
lr_card = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.80), Inches(1.50), Inches(6.00), Inches(5.45))
lr_card.fill.solid()
lr_card.fill.fore_color.rgb = WHITE
lr_card.line.color.rgb = RGBColor(0x93, 0x33, 0xEA)
lr_card.line.width = Pt(1.5)

lr_hdr = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), Inches(1.65), Inches(5.70), Inches(0.55))
lr_hdr.fill.solid()
lr_hdr.fill.fore_color.rgb = RGBColor(0x93, 0x33, 0xEA)
lr_hdr.line.fill.background()
p = lr_hdr.text_frame.paragraphs[0]
p.text = "LOGISTIC REGRESSION (LR) ACTIVITY FLOW"
p.font.name = "Calibri"
p.font.size = Pt(11.5)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

lr_steps = [
    ("1. Standardized Vector Input", "Sparse TF-IDF vector x with L2 Euclidean normalization representing clinical narrative."),
    ("2. Linear Logit Computation", "Computes linear combination z_c = w_c · x + b_c for each medical specialty class c ∈ {1..40}."),
    ("3. L2 Ridge Regularization", "Applies L2 penalty λ/2 ||w||² in objective function to shrink weights & prevent overfitting."),
    ("4. Softmax Probability Mapping", "Transforms logits to calibrated probabilities via Softmax: P(y=c|x) = exp(z_c) / Σ exp(z_k)."),
    ("5. Cross-Entropy Loss Optimization", "Optimizes parameter weights using L-BFGS quasi-Newton gradient ascent solver."),
    ("6. Multi-Class Probability Output", "Generates calibrated posterior probability distribution vector across all 40 categories.")
]

for i, (title, desc) in enumerate(lr_steps):
    box = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), y_pos + i * (step_h + step_gap), Inches(5.70), step_h)
    box.fill.solid()
    box.fill.fore_color.rgb = RGBColor(0xFA, 0xF5, 0xFF)
    box.line.color.rgb = RGBColor(0xE9, 0xD5, 0xFF)
    box.line.width = Pt(1)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.12)
    tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Calibri"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x7E, 0x22, 0xCE)
    p = tf.add_paragraph()
    p.text = desc
    p.font.name = "Calibri"
    p.font.size = Pt(8.5)
    p.font.bold = False
    p.font.color.rgb = SLATE_DARK

print("Slide 15 rebuilt with RF & LR Activity Diagrams.")

# =========================================================================
# 4. SLIDE 16: SOFT VOTING ENSEMBLE CONSENSUS ACTIVITY DIAGRAM
# =========================================================================
s16 = prs.slides[15]
sp_tree16 = s16.shapes._spTree
for sh in list(s16.shapes):
    sp_tree16.remove(sh._element)

# Header & Footers
pill16 = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(0.35), Inches(4.60), Inches(0.32))
pill16.fill.solid()
pill16.fill.fore_color.rgb = TEAL_ACCENT
pill16.line.fill.background()
p = pill16.text_frame.paragraphs[0]
p.text = "MCA MINI PROJECT | DETAILS OF ALGORITHMS"
p.font.name = "Calibri"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = WHITE

tbox16 = s16.shapes.add_textbox(Inches(0.50), Inches(0.72), Inches(12.30), Inches(0.68))
p = tbox16.text_frame.paragraphs[0]
p.text = "Soft Voting Ensemble: Architecture & Activity Flow"
p.font.name = "Cambria"
p.font.size = Pt(26)
p.font.bold = True
p.font.color.rgb = RGBColor(0x0B, 0x1F, 0x3A)

# Footers
f1 = s16.shapes.add_textbox(Inches(0.50), Inches(7.13), Inches(4.60), Inches(0.30))
p1 = f1.text_frame.paragraphs[0]
p1.text = "Department of Computer Applications | MACE"
p1.font.name = "Calibri"
p1.font.size = Pt(9)
p1.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

f2 = s16.shapes.add_textbox(Inches(4.00), Inches(7.13), Inches(5.33), Inches(0.30))
p2 = f2.text_frame.paragraphs[0]
p2.text = "Mar Athanasius College of Engineering, Kothamangalam"
p2.font.name = "Calibri"
p2.font.size = Pt(9)
p2.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

f3 = s16.shapes.add_textbox(Inches(9.90), Inches(7.13), Inches(2.93), Inches(0.30))
p3 = f3.text_frame.paragraphs[0]
p3.text = "Slide 16 of 20"
p3.font.name = "Calibri"
p3.font.size = Pt(9)
p3.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

# Top Box: Input & Vectorization Flow
top_box = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.50), Inches(12.30), Inches(0.80))
top_box.fill.solid()
top_box.fill.fore_color.rgb = RGBColor(0xEE, 0xF6, 0xF6)
top_box.line.color.rgb = TEAL_ACCENT
top_box.line.width = Pt(1.5)
tf = top_box.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "STAGE 1: INPUT NARRATIVE & VECTORIZATION INFERENCE"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = TEAL_ACCENT
p = tf.add_paragraph()
p.text = "Unseen Clinical Transcription Text  →  8-Step Preprocessing Pipeline  →  TF-IDF Transformation (V vocabulary features)  →  Normalized Sparse Vector x"
p.font.name = "Calibri"
p.font.size = Pt(10)
p.font.color.rgb = DARK_TEXT

# Middle 4 Model Boxes (Parallel Execution)
m_w = Inches(2.90)
m_gap = Inches(0.23)
m_start = Inches(0.50)
models_info = [
    ("SVM Classifier", "Support Vector Machine", "Platt Calibrated Scaling", "P_SVM(c|x)", RGBColor(0x0E, 0x7C, 0x86), RGBColor(0xF0, 0xFD, 0xFA)),
    ("Random Forest", "Ensemble Decision Trees", "Tree Mean Voting", "P_RF(c|x)", RGBColor(0x16, 0xA3, 0x4A), RGBColor(0xF0, 0xFD, 0xF4)),
    ("Logistic Regression", "Multinomial Softmax", "L2 Regularized Logits", "P_LR(c|x)", RGBColor(0x93, 0x33, 0xEA), RGBColor(0xFA, 0xF5, 0xFF)),
    ("Multinomial NB", "Naïve Bayes Estimator", "Laplace Smoothed Prior", "P_MNB(c|x)", RGBColor(0x25, 0x63, 0xEB), RGBColor(0xEF, 0xF6, 0xFF))
]

for i, (m_title, m_desc, m_sub, m_prob, m_col, m_bg) in enumerate(models_info):
    mbox = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, m_start + i * (m_w + m_gap), Inches(2.45), m_w, Inches(1.65))
    mbox.fill.solid()
    mbox.fill.fore_color.rgb = m_bg
    mbox.line.color.rgb = m_col
    mbox.line.width = Pt(1.5)
    tf = mbox.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.12)
    tf.margin_top = Inches(0.10)
    p = tf.paragraphs[0]
    p.text = f"MODEL {i+1}: {m_title}"
    p.font.name = "Calibri"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = m_col
    p.space_after = Pt(2)
    
    p = tf.add_paragraph()
    p.text = m_desc
    p.font.name = "Calibri"
    p.font.size = Pt(9.5)
    p.font.color.rgb = SLATE_DARK
    
    p = tf.add_paragraph()
    p.text = m_sub
    p.font.name = "Calibri"
    p.font.size = Pt(9)
    p.font.color.rgb = MUTED_SLATE
    p.space_after = Pt(4)
    
    p = tf.add_paragraph()
    p.text = f"Output: {m_prob} ∈ R^40"
    p.font.name = "Calibri"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = m_col

# Consensus Layer Card
cons_box = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(4.30), Inches(12.30), Inches(1.50))
cons_box.fill.solid()
cons_box.fill.fore_color.rgb = WHITE
cons_box.line.color.rgb = RGBColor(0xD9, 0x77, 0x06)
cons_box.line.width = Pt(1.5)
tf = cons_box.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.20)
tf.margin_top = Inches(0.12)

p = tf.paragraphs[0]
p.text = "STAGE 2: SOFT VOTING CONSENSUS & PROBABILITY AGGREGATION"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = RGBColor(0xD9, 0x77, 0x06)
p.space_after = Pt(3)

p = tf.add_paragraph()
p.text = "Formula: P_Ensemble(c | x) = 1/4 · [ P_SVM(c | x) + P_RF(c | x) + P_LR(c | x) + P_MNB(c | x) ]   for all 40 categories c ∈ {1..40}"
p.font.name = "Cambria"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
p.space_after = Pt(3)

p = tf.add_paragraph()
p.text = "Decision Rule: Predicted Medical Specialty c* = argmax_c P_Ensemble(c | x)   with Confidence Score = max_c P_Ensemble(c | x) · 100%"
p.font.name = "Cambria"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = RGBColor(0x0E, 0x7C, 0x86)
p.space_after = Pt(3)

p = tf.add_paragraph()
p.text = "Why Soft Voting? Averages confident probability outputs rather than simple discrete votes; mitigates individual estimator errors and smooths noise."
p.font.name = "Calibri"
p.font.size = Pt(9.5)
p.font.color.rgb = SLATE_DARK

# Bottom Output Bar
out_box = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(5.95), Inches(12.30), Inches(0.95))
out_box.fill.solid()
out_box.fill.fore_color.rgb = RGBColor(0x13, 0x29, 0x4B)
out_box.line.color.rgb = CYAN_BRIGHT
out_box.line.width = Pt(1.5)
tf = out_box.text_frame
tf.word_wrap = True
tf.margin_left = Inches(0.20)
tf.margin_top = Inches(0.12)

p = tf.paragraphs[0]
p.text = "FINAL SYSTEM PREDICTION OUTPUT (STAGE 3)"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = CYAN_LIGHT

p = tf.add_paragraph()
p.text = "• Primary Prediction: Assigned Medical Specialty Class (e.g., 'Cardiovascular / Pulmonary')\n• Confidence Estimate: Aggregated ensemble probability score (%) verifying clinical prediction certainty"
p.font.name = "Calibri"
p.font.size = Pt(10)
p.font.color.rgb = WHITE

print("Slide 16 rebuilt with Soft Voting Ensemble Architecture.")

# =========================================================================
# 5. FIX SLIDE 18 (PROGRESS & ROADMAP - ENSURE PILL SHAPE & CONTRAST)
# =========================================================================
s18 = prs.slides[17]
# Ensure header pill exists
for sh in list(s18.shapes):
    if sh.has_text_frame and "MCA MINI PROJECT" in sh.text:
        sp_tree18 = s18.shapes._spTree
        sp_tree18.remove(sh._element)

pill18 = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(0.35), Inches(4.60), Inches(0.32))
pill18.fill.solid()
pill18.fill.fore_color.rgb = TEAL_ACCENT
pill18.line.fill.background()
p = pill18.text_frame.paragraphs[0]
p.text = "MCA MINI PROJECT | PROGRESS & ROADMAP"
p.font.name = "Calibri"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = WHITE

print("Slide 18 header pill repaired.")

# =========================================================================
# 6. FIX SLIDE 19 (PROJECT TIMELINE - ENSURE PILL SHAPE & CONTRAST)
# =========================================================================
s19 = prs.slides[18]
for sh in list(s19.shapes):
    if sh.has_text_frame and "MCA MINI PROJECT" in sh.text:
        sp_tree19 = s19.shapes._spTree
        sp_tree19.remove(sh._element)

pill19 = s19.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(0.35), Inches(4.60), Inches(0.32))
pill19.fill.solid()
pill19.fill.fore_color.rgb = TEAL_ACCENT
pill19.line.fill.background()
p = pill19.text_frame.paragraphs[0]
p.text = "MCA MINI PROJECT | PROJECT TIMELINE"
p.font.name = "Calibri"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = WHITE

print("Slide 19 header pill repaired.")

# =========================================================================
# 7. OVERHAUL SLIDE 20 (CONCLUSION & THANK YOU - VIBRANT & HIGH CONTRAST)
# =========================================================================
s20 = prs.slides[19]
sp_tree20 = s20.shapes._spTree
for sh in list(s20.shapes):
    sp_tree20.remove(sh._element)

# Slide 20 Background: Solid Deep Navy matching Slide 1
s20.background.fill.solid()
s20.background.fill.fore_color.rgb = NAVY_BG

# Decorative glowing top accent bar
bar20 = s20.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
bar20.fill.solid()
bar20.fill.fore_color.rgb = CYAN_BRIGHT
bar20.line.fill.background()

# Header Pill
pill20 = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(0.35), Inches(4.60), Inches(0.32))
pill20.fill.solid()
pill20.fill.fore_color.rgb = TEAL_ACCENT
pill20.line.color.rgb = CYAN_BRIGHT
pill20.line.width = Pt(1)
p = pill20.text_frame.paragraphs[0]
p.text = "MCA MINI PROJECT | CONCLUSION"
p.font.name = "Calibri"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = WHITE

# Slide Title
tbox20 = s20.shapes.add_textbox(Inches(0.50), Inches(0.72), Inches(12.30), Inches(0.68))
p = tbox20.text_frame.paragraphs[0]
p.text = "Conclusion & Implementation Roadmap"
p.font.name = "Cambria"
p.font.size = Pt(28)
p.font.bold = True
p.font.color.rgb = WHITE

# Footers
f1 = s20.shapes.add_textbox(Inches(0.50), Inches(7.13), Inches(4.60), Inches(0.30))
p1 = f1.text_frame.paragraphs[0]
p1.text = "Department of Computer Applications | MACE"
p1.font.name = "Calibri"
p1.font.size = Pt(9)
p1.font.color.rgb = MUTED_SLATE

f2 = s20.shapes.add_textbox(Inches(4.00), Inches(7.13), Inches(5.33), Inches(0.30))
p2 = f2.text_frame.paragraphs[0]
p2.text = "Mar Athanasius College of Engineering, Kothamangalam"
p2.font.name = "Calibri"
p2.font.size = Pt(9)
p2.font.color.rgb = MUTED_SLATE

f3 = s20.shapes.add_textbox(Inches(9.90), Inches(7.13), Inches(2.93), Inches(0.30))
p3 = f3.text_frame.paragraphs[0]
p3.text = "Slide 20 of 20"
p3.font.name = "Calibri"
p3.font.size = Pt(9)
p3.font.color.rgb = MUTED_SLATE

# Left Card: Key Phase 1 Achievements
card_ach = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(1.50), Inches(5.95), Inches(3.70))
card_ach.fill.solid()
card_ach.fill.fore_color.rgb = NAVY_CARD
card_ach.line.color.rgb = CYAN_BRIGHT
card_ach.line.width = Pt(1.5)

tf_ca = card_ach.text_frame
tf_ca.word_wrap = True
tf_ca.margin_left = Inches(0.22)
tf_ca.margin_right = Inches(0.20)
tf_ca.margin_top = Inches(0.18)

p = tf_ca.paragraphs[0]
p.text = "KEY PHASE 1 ACHIEVEMENTS (SPRINT RELEASE I)"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = CYAN_LIGHT
p.space_after = Pt(6)

achievements = [
    ("✓ Problem Addressed", "Formulated automated routing for unstructured clinical narratives across 40 distinct medical specialties."),
    ("✓ Data Audit Complete", "Cleaned 4,999 MTSamples records; audited nulls and isolated 4,966 validated clinical transcripts."),
    ("✓ In-Depth EDA Executed", "Characterized severe long-tail class skew, document token density, and vocabulary distribution patterns."),
    ("✓ Leakage-Free Pipeline", "Designed modular 8-step NLP cleaner with strict train-only TF-IDF vectorization to avoid data leakage."),
    ("✓ Architecture Established", "Selected 4 diverse classifiers (SVM, RF, LR, MNB) unified under a Soft-Voting probability consensus model.")
]

for title, desc in achievements:
    p = tf_ca.add_paragraph()
    r1 = p.add_run()
    r1.text = title + ": "
    r1.font.name = "Calibri"
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = GREEN_CHECK
    
    r2 = p.add_run()
    r2.text = desc
    r2.font.name = "Calibri"
    r2.font.size = Pt(9.2)
    r2.font.bold = False
    r2.font.color.rgb = ICE_WHITE
    p.space_after = Pt(3)

# Right Card: Planned Next Steps
card_fut = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.80), Inches(1.50), Inches(6.00), Inches(3.70))
card_fut.fill.solid()
card_fut.fill.fore_color.rgb = NAVY_CARD
card_fut.line.color.rgb = PURPLE_ACCENT
card_fut.line.width = Pt(1.5)

tf_cf = card_fut.text_frame
tf_cf.word_wrap = True
tf_cf.margin_left = Inches(0.22)
tf_cf.margin_right = Inches(0.20)
tf_cf.margin_top = Inches(0.18)

p = tf_cf.paragraphs[0]
p.text = "PLANNED NEXT STEPS (PHASES 2 & 3)"
p.font.name = "Calibri"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = PURPLE_ACCENT
p.space_after = Pt(6)

future_steps = [
    ("→ Execute Cleaning Pipeline", "Apply modular character normalization, stop-word pruning, and lemmatization across 4,966 records."),
    ("→ Feature Matrix Extraction", "Fit TF-IDF vectorizer strictly on training split (80:20) with sublinear term-frequency scaling."),
    ("→ Train & Tune Estimators", "Train SVM, Random Forest, Logistic Regression, and MNB classifiers; execute hyperparameter grid tuning."),
    ("→ Build Soft Voting Ensemble", "Implement soft consensus probability aggregation combining calibrated predictive distributions."),
    ("→ Multi-Class Evaluation", "Benchmark Macro/Weighted F1, Recall, Precision, and cross-category Confusion Matrices."),
    ("→ Deployment & Serialization", "Serialize pipeline with Joblib; construct interactive clinician dashboard using Flask.")
]

for title, desc in future_steps:
    p = tf_cf.add_paragraph()
    r1 = p.add_run()
    r1.text = title + ": "
    r1.font.name = "Calibri"
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = BLUE_ARROW
    
    r2 = p.add_run()
    r2.text = desc
    r2.font.name = "Calibri"
    r2.font.size = Pt(9.2)
    r2.font.bold = False
    r2.font.color.rgb = ICE_WHITE
    p.space_after = Pt(3)

# Bottom Card: Big Vibrant "THANK YOU & QUESTIONS" Section
ty_card = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(5.35), Inches(12.30), Inches(1.60))
ty_card.fill.solid()
ty_card.fill.fore_color.rgb = RGBColor(0x0E, 0x2A, 0x54)
ty_card.line.color.rgb = CYAN_BRIGHT
ty_card.line.width = Pt(2)

tf_ty = ty_card.text_frame
tf_ty.word_wrap = True
tf_ty.margin_top = Inches(0.18)

p = tf_ty.paragraphs[0]
p.text = "THANK YOU!"
p.font.name = "Cambria"
p.font.size = Pt(28)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

p = tf_ty.add_paragraph()
p.text = "Questions, Suggestions & Discussions are Welcome"
p.font.name = "Calibri"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = CYAN_LIGHT
p.alignment = PP_ALIGN.CENTER
p.space_after = Pt(4)

p = tf_ty.add_paragraph()
p.text = "Student: Jiphin George (MAC25MCA-2033)  |  Project Guide: Prof. Biju Skaria  |  MCA Mini Project (Semester 3)"
p.font.name = "Calibri"
p.font.size = Pt(11)
p.font.color.rgb = MUTED_SLATE
p.alignment = PP_ALIGN.CENTER

print("Slide 20 rebuilt with vibrant colors and crystal-clear text.")

# Save updated presentation
output_updated = r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation_updated.pptx"
output_local = r"D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation_updated.pptx"

prs.save(output_updated)
print(f"Successfully saved to: {output_updated}")
prs.save(output_local)
print(f"Successfully saved to: {output_local}")

try:
    prs.save(PPTX_PATH)
    print(f"Successfully overwritten: {PPTX_PATH}")
except Exception as e:
    print(f"Notice: {PPTX_PATH} is currently open in PowerPoint: {e}")
    print(f"The updated presentation is saved as: {output_updated}")

