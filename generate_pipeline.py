import matplotlib.pyplot as plt
import matplotlib.patches as patches

# High-resolution, clean-contrast diagram
fig, ax = plt.subplots(figsize=(15.8, 12.6), dpi=300)
ax.set_xlim(0, 15.8)
ax.set_ylim(0, 12.6)
ax.axis('off')

# Crisp, dark academic color scheme
BORDER_COLOR = '#111827'  # Deep obsidian black
LINE_COLOR = '#111827'
TITLE_COLOR = '#000000'   # Pure black for crisp maximum contrast
SUBTITLE_COLOR = '#1F2937' # Dark charcoal (easily readable, non-washed-out)

def draw_container(ax, x, y, w, h, title):
    # Main container box
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.22',
                                  facecolor='#FFFFFF', edgecolor=BORDER_COLOR, linewidth=2.0)
    ax.add_patch(rect)
    
    # Title badge / tab centered on top border
    tw, th = 3.8, 0.48
    tx = x + (w - tw) / 2
    ty = y + h - th / 2
    tab = patches.FancyBboxPatch((tx, ty), tw, th, boxstyle='round,pad=0.02,rounding_size=0.12',
                                 facecolor='#FFFFFF', edgecolor=BORDER_COLOR, linewidth=2.0)
    ax.add_patch(tab)
    ax.text(tx + tw/2, ty + th/2, title, ha='center', va='center',
            fontsize=13.0, fontweight='bold', color=TITLE_COLOR)

def draw_box(ax, x, y, w, h, title, subtitle=''):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.15',
                                  facecolor='#FFFFFF', edgecolor=BORDER_COLOR, linewidth=1.6)
    ax.add_patch(rect)
    if subtitle:
        ax.text(x + w/2, y + h*0.65, title, ha='center', va='center',
                fontsize=11.2, fontweight='bold', color=TITLE_COLOR, linespacing=1.22)
        ax.text(x + w/2, y + h*0.28, subtitle, ha='center', va='center',
                fontsize=9.2, fontweight='medium', color=SUBTITLE_COLOR, linespacing=1.20)
    else:
        ax.text(x + w/2, y + h/2, title, ha='center', va='center',
                fontsize=10.0, fontweight='bold', color=TITLE_COLOR, linespacing=1.20)

# ======================== CONTAINER 1: DATA ========================
c1_x, c1_y, c1_w, c1_h = 0.5, 9.1, 14.8, 2.9
draw_container(ax, c1_x, c1_y, c1_w, c1_h, 'DATA')

b_w = 2.52
b_h = 2.05
b_y = 9.48
gaps = (c1_w - 0.7 - 5 * b_w) / 4
xs = [c1_x + 0.35 + i * (b_w + gaps) for i in range(5)]

draw_box(ax, xs[0], b_y, b_w, b_h, 'Kaggle MTSamples\nDataset', 'Clinical Transcription\nCorpus')
draw_box(ax, xs[1], b_y, b_w, b_h, 'Raw Clinical\nTranscriptions', '4,966 Cleaned Reports\n40 Specialties')
draw_box(ax, xs[2], b_y, b_w, b_h, 'Text\nPreprocessing', 'Lowercasing, Stop-words,\nLemmatization')
draw_box(ax, xs[3], b_y, b_w, b_h, 'TF-IDF Feature\nExtraction', 'Unigram & Bigram\nSublinear Frequency')
draw_box(ax, xs[4], b_y, b_w, b_h, 'Feature Dataset\nCreation', 'Sparse Feature Matrix\n(features_final.csv)')

for i in range(4):
    ax.annotate('', xy=(xs[i+1], b_y + b_h/2), xytext=(xs[i] + b_w, b_y + b_h/2),
                arrowprops=dict(arrowstyle='->,head_width=0.45,head_length=0.6', color=LINE_COLOR, lw=1.8))

# ======================== CONTAINER 2: MODEL BUILDING ========================
c2_x, c2_y, c2_w, c2_h = 0.5, 4.75, 14.8, 3.0
draw_container(ax, c2_x, c2_y, c2_w, c2_h, 'MODEL BUILDING')

# Box 1: Train-Test Split
m1_x = c2_x + 0.35
m1_w = 2.20
m1_h = 2.10
m1_y = 5.15
draw_box(ax, m1_x, m1_y, m1_w, m1_h, 'Train–Test\nSplit', '80% Training\n20% Testing')

# Route from Container 1 (Feature Dataset) to Container 2 (Train-Test Split)
# Generous space in Channel 1 (between 8.00 and 9.10), passes at y = 8.50 (well above MODEL BUILDING tab at y = 7.99)
p1_start = (xs[4] + b_w/2, b_y)
m1_top_center = (m1_x + m1_w/2, m1_y + m1_h)
ax.plot([p1_start[0], p1_start[0], m1_top_center[0], m1_top_center[0]],
        [p1_start[1], 8.50, 8.50, m1_top_center[1] + 0.05], color=LINE_COLOR, lw=1.8)
ax.annotate('', xy=m1_top_center, xytext=(m1_top_center[0], m1_top_center[1] + 0.1),
            arrowprops=dict(arrowstyle='->,head_width=0.45,head_length=0.6', color=LINE_COLOR, lw=1.8))

# 4 Models Stack: 3.15 width comfortably accommodates full text strings with generous padding
c_x = m1_x + m1_w + 0.65
c_w = 3.15
c_h = 0.44
c_ys = [6.85, 6.25, 5.65, 5.05]
draw_box(ax, c_x, c_ys[0], c_w, c_h, 'Support Vector Machine (SVM)')
draw_box(ax, c_x, c_ys[1], c_w, c_h, 'Random Forest')
draw_box(ax, c_x, c_ys[2], c_w, c_h, 'Logistic Regression')
draw_box(ax, c_x, c_ys[3], c_w, c_h, 'Multinomial Naive Bayes')

# Orthogonal Bus from Train-Test Split to 4 Models
bus1_x = m1_x + m1_w + 0.32
mid_y = 6.20
ax.plot([m1_x + m1_w, bus1_x], [mid_y, mid_y], color=LINE_COLOR, lw=1.6)
ax.plot([bus1_x, bus1_x], [c_ys[3] + c_h/2, c_ys[0] + c_h/2], color=LINE_COLOR, lw=1.6)
for cy in c_ys:
    ax.annotate('', xy=(c_x, cy + c_h/2), xytext=(bus1_x, cy + c_h/2),
                arrowprops=dict(arrowstyle='->,head_width=0.35,head_length=0.5', color=LINE_COLOR, lw=1.6))

# Box 3: Soft Voting Ensemble
ens_x = c_x + c_w + 0.65
ens_w = 2.40
ens_h = 2.10
draw_box(ax, ens_x, m1_y, ens_w, ens_h, 'Soft Voting\nEnsemble', 'Probability-Based\nAggregation')

# Orthogonal Bus from 4 Models to Voting Ensemble
bus2_x = c_x + c_w + 0.32
ax.plot([bus2_x, bus2_x], [c_ys[3] + c_h/2, c_ys[0] + c_h/2], color=LINE_COLOR, lw=1.6)
for cy in c_ys:
    ax.plot([c_x + c_w, bus2_x], [cy + c_h/2, cy + c_h/2], color=LINE_COLOR, lw=1.6)
ax.annotate('', xy=(ens_x, mid_y), xytext=(bus2_x, mid_y),
            arrowprops=dict(arrowstyle='->,head_width=0.45,head_length=0.6', color=LINE_COLOR, lw=1.8))

# Box 4: Model Evaluation & Comparison
eval_x = ens_x + ens_w + 0.45
eval_w = 2.40
draw_box(ax, eval_x, m1_y, eval_w, ens_h, 'Model Evaluation\n& Comparison', 'Accuracy, Precision,\nRecall, F1-Score')
ax.annotate('', xy=(eval_x, mid_y), xytext=(ens_x + ens_w, mid_y),
            arrowprops=dict(arrowstyle='->,head_width=0.45,head_length=0.6', color=LINE_COLOR, lw=1.8))

# Box 5: Model Selection & Serialization
best_x = eval_x + eval_w + 0.45
best_w = 2.35
draw_box(ax, best_x, m1_y, best_w, ens_h, 'Model Selection\n& Serialization', 'Save Selected Model\n(Pickle / Joblib)')
ax.annotate('', xy=(best_x, mid_y), xytext=(eval_x + eval_w, mid_y),
            arrowprops=dict(arrowstyle='->,head_width=0.45,head_length=0.6', color=LINE_COLOR, lw=1.8))

# ======================== CONTAINER 3: DEPLOYMENT ========================
c3_x, c3_y, c3_w, c3_h = 0.5, 0.45, 14.8, 2.9
draw_container(ax, c3_x, c3_y, c3_w, c3_h, 'DEPLOYMENT')

# 5 Boxes in Deployment
dep_w = 2.22
dep_h = 2.05
dep_y = 0.85
dep_gaps = (c3_w - 0.7 - 5 * dep_w - 1.25) / 4
dep_xs = [c3_x + 0.35 + i * (dep_w + dep_gaps) for i in range(5)]

draw_box(ax, dep_xs[0], dep_y, dep_w, dep_h, 'Flask Web\nApplication', 'User-Friendly\nWeb Interface')
draw_box(ax, dep_xs[1], dep_y, dep_w, dep_h, 'Input Clinical\nTranscription', 'Paste Text Narrative\nor Upload File')
draw_box(ax, dep_xs[2], dep_y, dep_w, dep_h, 'Text Preprocessing\n& Feature Extraction', 'Using Serialized\nTF-IDF Pipeline')
draw_box(ax, dep_xs[3], dep_y, dep_w, dep_h, 'Specialty\nPrediction', 'Trained Ensemble\n40 Categories')
draw_box(ax, dep_xs[4], dep_y, dep_w, dep_h, 'Prediction\nResult', 'Predicted Specialty +\nConfidence Score')

for i in range(4):
    ax.annotate('', xy=(dep_xs[i+1], dep_y + dep_h/2), xytext=(dep_xs[i] + dep_w, dep_y + dep_h/2),
                arrowprops=dict(arrowstyle='->,head_width=0.45,head_length=0.6', color=LINE_COLOR, lw=1.8))

# Route from Container 2 (Model Selection) to Container 3 (Flask App)
# Channel 2: between 3.59 (DEPLOYMENT tab top) and 4.75 (Container 2 bottom), passes at y = 4.15
p2_start = (best_x + best_w/2, m1_y)
dep1_top_center = (dep_xs[0] + dep_w/2, dep_y + dep_h)
ax.plot([p2_start[0], p2_start[0], dep1_top_center[0], dep1_top_center[0]],
        [p2_start[1], 4.15, 4.15, dep1_top_center[1] + 0.05], color=LINE_COLOR, lw=1.8)
ax.annotate('', xy=dep1_top_center, xytext=(dep1_top_center[0], dep1_top_center[1] + 0.1),
            arrowprops=dict(arrowstyle='->,head_width=0.45,head_length=0.6', color=LINE_COLOR, lw=1.8))

# Clinician / User Icon & Label at far right of Deployment
user_x = dep_xs[4] + dep_w + 0.38
user_y = dep_y + dep_h/2
circle = patches.Circle((user_x + 0.36, user_y + 0.36), 0.22, facecolor='#FFFFFF', edgecolor=BORDER_COLOR, lw=1.6)
ax.add_patch(circle)
arc = patches.Arc((user_x + 0.36, user_y - 0.16), 0.65, 0.55, theta1=0, theta2=180, edgecolor=BORDER_COLOR, lw=1.6)
ax.add_patch(arc)
ax.text(user_x + 0.36, user_y - 0.55, 'Clinician / User', ha='center', va='center',
        fontsize=10.5, fontweight='bold', color=TITLE_COLOR)
ax.annotate('', xy=(user_x, user_y), xytext=(dep_xs[4] + dep_w, user_y),
            arrowprops=dict(arrowstyle='->,head_width=0.45,head_length=0.6', color=LINE_COLOR, lw=1.8))

plt.tight_layout()
plt.savefig('Inital Report/EDA_Diagrams/07_project_pipeline.png', dpi=300, bbox_inches='tight')
print('Successfully regenerated 07_project_pipeline.png with spacious boxes and readable text.')
