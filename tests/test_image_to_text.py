from src.ocr_processing.image_to_text import extract_text_from_image
import pytest
from pathlib import Path


def test_extract_text_from_image():
    # This builds a path to the image from the test file location
    current_dir = Path(__file__).parent # get the current directory
    project_root = current_dir.parent # get the parent directory
    image_path = project_root / "documents" / "samples" / "image3.jpg"
    text = extract_text_from_image(image_path)
    assert "good lighting" in text
    