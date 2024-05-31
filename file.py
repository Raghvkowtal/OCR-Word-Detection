import os
from typing import List
import easyocr

reader = easyocr.Reader(['en'], gpu=True)

def ocr_scan(image_path: str) -> str:
    result = reader.readtext(str(image_path))
    recognized_text = " ".join(elem[1] for elem in result)

    return recognized_text

# def search_images():
#     pass

image_path = "./er.PNG"
ocr_scan(image_path)

def search_images(directory: str, keyword: str) -> List[str]:
    matching_images = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".gif", ".pdf", ".jpeg")):
                image_path = os.path.join(root, file)
                detected_text = ocr_scan(image_path)
                if keyword.lower() in detected_text.lower():
                    matching_images.append(image_path)
    return matching_images


results = search_images(".", keyword="Dharwar")
print(results)
