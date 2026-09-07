import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

PPTX_PATH = r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation.pptx"
prs = pptx.Presentation(PPTX_PATH)

# ==========================================
# PALETTE DEFINITIONS
# ==========================================
NAVY_DEEP = RGBColor(0x0A, 0x19, 0x2F)     # Rich dark navy
NAVY_CARD = RGBColor(0x11, 0x22, 0x40)     # Glassmorphic dark card
NAVY_ACCENT = RGBColor(0x1D, 0x35, 0x57)   # Lighter navy
TEAL_PRIMARY = RGBColor(0x0E, 0x7C, 0x86)  # Teal badge
CYAN_BRIGHT = RGBColor(0x00, 0xE5, 0xFF)   # Electric cyan border/highlight
CYAN_LIGHT = RGBColor(0x38, 0xBD, 0xF8)    # Luminous cyan text
ICE_WHITE = RGBColor(0xF1, 0xF5, 0xF9)     # Luminous crisp text
WHITE = RGBColor(0xFF, 0xFF, 0xFF)         # Pure white
SLATE_LIGHT = RGBColor(0x94, 0xA3, 0xB8)   # Muted subtext
PURPLE_LIGHT = RGBColor(0xC0, 0x84, 0xFC)  # Lavender accent
GREEN_BRIGHT = RGBColor(0x4A, 0xDE, 0x80)  # Luminous green check
GOLD_STAR = RGBColor(0xFB, 0xBF, 0x24)     # Golden star
BLUE_ARROW = RGBColor(0x60, 0xA5, 0xFA)    # Luminous blue arrow
DARK_TEXT = RGBColor(0x0F, 0x17, 0x2A)     # Dark text on light cards
SLATE_DARK = RGBColor(0x33, 0x41, 0x55)    # Slate body text on light cards
BORDER_LIGHT = RGBColor(0xCB, 0xD5, 0xE1)  # Light card border

# Helper: remove shapes except header/footer
def clear_slide_contents(slide, keep_header_footer=True):
    sp_tree = slide.shapes._spTree
    shapes_to_keep = []
    if keep_header_footer:
        for sh in slide.shapes:
            if sh.has_text_frame:
                t = sh.text.strip()
                if any(k in t for k in ["MCA MINI PROJECT", "Department of Computer", "Mar Athanasius", "Slide "]):
                    shapes_to_keep.append(sh)
    for sh in list(slide.shapes):
        if sh not in shapes_to_keep:
            sp_tree.remove(sh._element)

# Helper: ensure header pill exists
def ensure_header_pill(slide, category_text, title_text, slide_num_str):
    sp_tree = slide.shapes._spTree
    # Remove existing header & title shapes if corrupted
    for sh in list(slide.shapes):
        if sh.has_text_frame:
            t = sh.text.strip()
            if "MCA MINI PROJECT" in t or t == title_text or "Slide " in t or "Department of" in t or "Mar Athanasius" in t:
                try: sp_tree.remove(sh._element)
                except: pass
        else:
            # check if it's an old pill or circle
            if sh.top < Inches(1.5) and sh.left < Inches(5.0):
                try: sp_tree.remove(sh._element)
                except: pass

    # Add vibrant teal pill
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.50), Inches(0.35), Inches(4.60), Inches(0.32))
    pill.fill.solid()
    pill.fill.fore_color.rgb = TEAL_PRIMARY
    pill.line.fill.background()
    tf = pill.text_frame
    tf.margin_left = Inches(0.15)
    tf.margin_top = Inches(0.04)
    p = tf.paragraphs[0]
    p.text = category_text
    p.font.name = "Calibri"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Add title text box
    tb = slide.shapes.add_textbox(Inches(0.50), Inches(0.72), Inches(12.30), Inches(0.68))
    tf_t = tb.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.name = "Cambria"
    p_t.font.size = Pt(26)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(0x0B, 0x1F, 0x3A)

    # Footers
    f1 = slide.shapes.add_textbox(Inches(0.50), Inches(7.13), Inches(4.60), Inches(0.30))
    p1 = f1.text_frame.paragraphs[0]
    p1.text = "Department of Computer Applications | MACE"
    p1.font.name = "Calibri"
    p1.font.size = Pt(9)
    p1.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

    f2 = slide.shapes.add_textbox(Inches(4.00), Inches(7.13), Inches(5.33), Inches(0.30))
    p2 = f2.text_frame.paragraphs[0]
    p2.text = "Mar Athanasius College of Engineering, Kothamangalam"
    p2.font.name = "Calibri"
    p2.font.size = Pt(9)
    p2.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

    f3 = slide.shapes.add_textbox(Inches(9.90), Inches(7.13), Inches(2.93), Inches(0.30))
    p3 = f3.text_frame.paragraphs[0]
    p3.text = slide_num_str
    p3.font.name = "Calibri"
    p3.font.size = Pt(9)
    p3.font.color.rgb = RGBColor(0x5B, 0x64, 0x72)

print("Helper functions ready.")
