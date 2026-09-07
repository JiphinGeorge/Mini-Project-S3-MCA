import pymupdf

pdf_path = r"D:\Antigravity Projects\Mini Project S3 MCA\Inital Report\Mini_Project_Inital_report.pdf"
doc = pymupdf.open(pdf_path)

pages_to_check = [25, 27, 29, 30, 32, 33, 35]

for p_num in pages_to_check:
    page = doc[p_num - 1]
    blocks = page.get_text("blocks")
    print(f"\n--- PAGE {p_num} ---")
    for b in blocks:
        t = b[4].strip().replace('\n', ' ')
        if b[1] < 120 or b[1] > 400 or 'figure' in t.lower():
            print(f"y0={b[1]:.1f}, y1={b[3]:.1f} (x0={b[0]:.1f}, x1={b[2]:.1f}): {t[:60]}")
