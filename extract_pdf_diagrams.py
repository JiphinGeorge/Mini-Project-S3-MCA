import pymupdf
import os

pdf_path = r"D:\Antigravity Projects\Mini Project S3 MCA\Inital Report\Mini_Project_Inital_report.pdf"
doc = pymupdf.open(pdf_path)

out_dir = r"D:\Antigravity Projects\Mini Project S3 MCA\extracted_diagrams"
os.makedirs(out_dir, exist_ok=True)

target_pages = [25, 27, 29, 30, 32, 33, 35] # 1-indexed

for p_num in target_pages:
    page = doc[p_num - 1]
    # Check embedded images
    image_list = page.get_images(full=True)
    print(f"Page {p_num}: {len(image_list)} embedded images")
    
    # Also render page at high DPI (300 DPI)
    zoom = 300 / 72 # 4.16x
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    page_img_path = os.path.join(out_dir, f"page_{p_num}.png")
    pix.save(page_img_path)
    print(f"  Rendered page {p_num} -> {page_img_path} ({pix.width}x{pix.height})")

    # If embedded images exist, extract them
    for img_idx, img_info in enumerate(image_list):
        xref = img_info[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        img_filename = f"diagram_page_{p_num}_img_{img_idx+1}.{image_ext}"
        img_filepath = os.path.join(out_dir, img_filename)
        with open(img_filepath, "wb") as f:
            f.write(image_bytes)
        print(f"  Extracted embedded image: {img_filepath} ({base_image['width']}x{base_image['height']})")
