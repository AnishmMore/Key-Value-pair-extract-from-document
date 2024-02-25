import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import cv2
import pandas as pd
import numpy as np
import re

def process_pdf_and_extract_data(pdf_path):
    # Function to convert a PDF to images
    def pdf_to_images(pdf_path):
        return convert_from_path(pdf_path)

    # Function to preprocess an image for OCR
    def preprocess_image_for_ocr(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        return thresh

    # Function to extract key-value pairs, table data, phone numbers, and full names from text
    def extract_data_from_text(text):
        key_value_pattern = r"([A-Za-z ]+):\s*([A-Za-z0-9./ ]+)"
        table_pattern = r'(\b[A-Z0-9\.]+\b)\s+([A-Z ]+)\s+(\d+)\s+(\d+\.?\d*)\s+(-?\d+\.?\d*)\s+(\d+)'
        phone_number_pattern = r"\b\d{3}[ -]?\d{4}\b"
        name_pattern = r"(Mr|Ms|Mrs)\.\s+[A-Z][a-z]+ [A-Z][a-z]+"

        key_value_matches = re.findall(key_value_pattern, text)
        table_matches = re.findall(table_pattern, text)
        phone_matches = re.findall(phone_number_pattern, text)
        name_matches = re.findall(name_pattern, text)

        key_value_dict = {key.strip(): value.strip() for key, value in key_value_matches}
        table_dict = {match[0]: match[1:] for match in table_matches}
        phone_list = list(set(phone_matches))  # Remove duplicates
        name_list = list(set(name_matches))  # Remove duplicates

        return {**key_value_dict, 'Table Data': table_dict, 'Phone Numbers': phone_list, 'Full Names': name_list}

    # Function to extract highlighted values from the original image
    def extract_highlighted_values(img):
        lower_highlight = np.array([0, 200, 200])
        upper_highlight = np.array([10, 255, 255])
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_highlight, upper_highlight)
        highlighted_text = pytesseract.image_to_string(cv2.bitwise_and(img, img, mask=mask))

        key_value_pairs = {}
        for line in highlighted_text.splitlines():
            if "Discount" in line:
                key_value_pairs["Discount"] = line.split()[-1]
            elif "Total CHF" in line:
                key_value_pairs["Total CHF"] = line.split()[-1]

        return key_value_pairs

    images = pdf_to_images(pdf_path)
    combined_data = {}

    for img in images:
        original_img = np.array(img)
        preprocessed_img = preprocess_image_for_ocr(original_img)
        phone_img = preprocess_image_for_ocr(original_img)
        text = pytesseract.image_to_string(preprocessed_img, config='--oem 3 --psm 6 ')
        phone_text = pytesseract.image_to_string(phone_img, config='--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789+()- ')
        data_from_text = extract_data_from_text(text)
        highlighted_values = extract_highlighted_values(original_img)

        combined_data.update(data_from_text)
        combined_data.update(highlighted_values)

    return combined_data
