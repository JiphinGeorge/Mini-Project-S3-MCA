import pymupdf

pdf_path = r"D:\Antigravity Projects\Mini Project S3 MCA\Inital Report\Mini_Project_Inital_report.pdf"
doc = pymupdf.open(pdf_path)

target_pages = [25, 27, 29, 30, 32, 33, 35]

for p_num in target_pages:
    page = doc[p_num - 1]
    blocks = page.get_text("blocks")
    print(f"\n=== PAGE {p_num} (width={page.rect.width}, height={page.rect.height}) ===")
    for b in blocks:
        text = b[4].strip().replace('\n', ' ')
        if any(k in text.lower() for k in ["figure", "activity diagram", "support vector", "random forest", "logistic regression", "multinomial", "tf-idf", "voting ensemble", "pipeline"]):
            print(f"  bbox=({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}): {text[:70]}")
