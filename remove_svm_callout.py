import pptx

SRC_PATH = r"D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation_v6.pptx"
prs = pptx.Presentation(SRC_PATH)

s12 = prs.slides[11] # Slide 12
sp_tree = s12.shapes._spTree

# Identify Shape 35 and Text 36
shapes_to_remove = []
for sh in s12.shapes:
    if sh.has_text_frame and "SVM is used as one of the base machine learning classifiers" in sh.text:
        shapes_to_remove.append(sh)
    elif not sh.has_text_frame and sh.top > pptx.util.Inches(5.5) and sh.top < pptx.util.Inches(6.0) and sh.width > pptx.util.Inches(10.0):
        shapes_to_remove.append(sh)

print(f"Removing {len(shapes_to_remove)} shapes from Slide 12...")
for sh in shapes_to_remove:
    sp_tree.remove(sh._element)
    print(f"Removed: {sh.name}")

# Let's adjust the vertical layout of Slide 12 to make it balanced
# The 3 horizontal cards (FEATURE EXTRACTION, CLASSIFICATION, ENSEMBLE) can be slightly expanded in height
for sh in s12.shapes:
    # If it's the 3 bottom banner cards
    if sh.top >= pptx.util.Inches(4.5) and sh.top < pptx.util.Inches(5.6):
        # Slightly increase height from ~1.0 in to 1.35 in for better visual weight
        sh.top = pptx.util.Inches(4.70)
        sh.height = pptx.util.Inches(1.50)

# Save to destination paths
V7_LOCAL = r"D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation_v7.pptx"
V7_DOWNLOADS = r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation_v7.pptx"

prs.save(V7_LOCAL)
print(f"Saved: {V7_LOCAL}")
prs.save(V7_DOWNLOADS)
print(f"Saved: {V7_DOWNLOADS}")

# Also update the canonical filenames
for path in [
    r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation.pptx",
    r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation_updated.pptx",
    r"D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation_updated.pptx",
    r"D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation_v6.pptx"
]:
    try:
        prs.save(path)
        print(f"Also updated: {path}")
    except Exception as e:
        print(f"Note: {path} is locked: {e}")

print("All done successfully.")
