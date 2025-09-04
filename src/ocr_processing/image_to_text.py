import os
import pytesseract
from PIL import Image
from .image_preprocessor import preprocess_image

# Extract text from clean image
def extract_text_from_image(image_path):
    clean_img = preprocess_image(image_path)
    text = pytesseract.image_to_string(clean_img).lower()
    return text
