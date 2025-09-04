import fitz
import os

def convert_pdf_to_images(file_path, output_folder):
    doc = fitz.open(file_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix =  page.get_pixmap() # convert page to image
        pix.save(f"{output_folder}/page-{page_num}.jpg") # saves the image in the output folderand .jpg