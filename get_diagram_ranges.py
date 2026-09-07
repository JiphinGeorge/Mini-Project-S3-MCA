import pymupdf

pdf_path = r"D:\Antigravity Projects\Mini Project S3 MCA\Inital Report\Mini_Project_Inital_report.pdf"
doc = pymupdf.open(pdf_path)

with open("diagram_ranges.txt", "w", encoding="utf-8") as f:
    for p_num in [25, 27, 29, 30, 32, 33, 35]:
        page = doc[p_num - 1]
        blocks = page.get_text("blocks")
        f.write(f"\n=== PAGE {p_num} ===\n")
        for b in blocks:
            t = b[4].strip().replace('\n', ' ')
            f.write(f"y=({b[1]:.1f} - {b[3]:.1f}), x=({b[0]:.1f} - {b[2]:.1f}): {t[:75]}\n")

print("Written diagram ranges.")
