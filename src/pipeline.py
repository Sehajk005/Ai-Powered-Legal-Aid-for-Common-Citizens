import tempfile
import os
from src.ocr_processing.pdf_processor import convert_pdf_to_images
from src.ocr_processing.image_to_text import extract_text_from_image

def process_pdf_for_text(file_path):
    with tempfile.TemporaryDirectory() as tmp_dir: # create a temporary directory
        images = convert_pdf_to_images(file_path, tmp_dir)
        full_text = ""
        for filename in os.listdir(tmp_dir):
            full_path = os.path.join(tmp_dir, filename)
            full_text += extract_text_from_image(full_path)
        return full_text