import os
from typing import List
import easyocr

"""
README:
easyocr 1.7.0 still using deprecated ANTIALIAS attribute in PIL.image module.
Force Pillow back to 9.5.0
pip install --force-reinstall -v "Pillow==9.5.0"
"""

reader = easyocr.Reader(['en'], gpu=True)
def ocr_scan(image_path: str) -> str:
    """Running OCR over the image"""
    result = reader.readtext(image_path)
    return " ".join(elem[1] for elem in result)

def search_images():
    """"Iterate over images in a folder, running OCR on each"""

    pass

image_path = "./place-name-sign.jpg"
print(ocr_scan(image_path))