# import os
# from typing import List
# import easyocr
# import  argparse
# reader = easyocr.Reader(['en'], gpu=True)


# def ocr_scan(image_path: str) -> str:
#     result = reader.readtext(str(image_path))
#     recognized_text = " ".join(elem[1] for elem in result)

#     return recognized_text


# def search_images(directory: str, keyword: str) -> List[str]:
#     matching_images = []
#     for root, _, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith((".png", ".jpg", ".gif", ".pdf", ".jpeg")):
#                 image_path = os.path.join(root, file)
#                 detected_text = ocr_scan(image_path)
#                 if keyword.lower() in detected_text.lower():
#                     matching_images.append(image_path)
#     return matching_images

#  #def main():
# parser = argparse.ArgumentParser(description="ocr search nod pa idd")
# parser.add_argument('-d', "--directory", type=str, help="the directory containing the images")
# parser.add_argument('-i','--image', type=str, help="the single imageto scan")
# parser.add_argument('-kw', "--keyword", type=str, help="the keyword to search for in image")     
# args = parser.parse_args()

# if args.directory:
#     matching_images = search_images(args.directory, args.keyword)
#     print("images that contain keyword")
#     for image_path in matching_images:
#         print(image_path)
# else:
#     detected_text = ocr_scan(args.image)
#     if args.keyword.lower() in detected_text.lower():
#          print(f"keyword found in image!")
#          print(f"found text: {detected_text}")
#     else:
#         print(f"keyword not found in image")

# if __name__ == "main":
#     main()
import os
from typing import List
import easyocr
import argparse

# Initialize the OCR reader
reader = easyocr.Reader(['en'], gpu=True)

# OCR function
def ocr_scan(image_path: str) -> str:
    result = reader.readtext(image_path)
    recognized_text = " ".join(elem[1] for elem in result)
    return recognized_text

# Search function
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

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Search for a keyword in images")
    parser.add_argument('-d', "--directory", type=str, help="The directory containing the images")
    parser.add_argument('-i', '--image', type=str, help="The single image to scan")
    parser.add_argument('-kw', "--keyword", type=str, help="The keyword to search for in the image")
    args = parser.parse_args()

    # Check if directory argument is provided
    if args.directory:
        # Check if the provided directory exists
        if not os.path.isdir(args.directory):
            print("Error: Directory does not exist.")
            return

        matching_images = search_images(args.directory, args.keyword)
        if matching_images:
            print("Images that contain the keyword:")
            for image_path in matching_images:
                print(image_path)
        else:
            print("No images found containing the keyword.")
    # Check if image argument is provided
    elif args.image:
        # Check if the provided image file exists
        if not os.path.isfile(args.image):
            print("Error: Image file does not exist.")
            return

        detected_text = ocr_scan(args.image)
        if args.keyword.lower() in detected_text.lower():
            print("Keyword found in the image!")
            print(f"Found text: {detected_text}")
        else:
            print("Keyword not found in the image.")
    else:
        print("Error: Please provide either a directory or an image file.")

if __name__ == "__main__":
    main()
