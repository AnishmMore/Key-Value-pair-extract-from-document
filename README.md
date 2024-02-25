# Key-Value-pair-extract-from-document

Steps to run:
python app.py

For part1:

just run the ipynb file on jypter notebook or colab.


For part2:

run: python app.py



**Documentation: Data Extraction from PDFs and Scanned Images**

**Introduction:**
This document outlines the approach taken to extract data from PDFs and scanned images using Python. It covers the design choices made, challenges faced, and instructions on how to run the application.

**Approach:**
1. **Problem Understanding:** The first step was to understand the requirement thoroughly, which involved extracting structured data from unstructured sources like PDFs and scanned images.

2. **Research and Exploration:** Researched various Python libraries and tools suitable for OCR (Optical Character Recognition) and PDF processing. Explored libraries such as Pytesseract, pdf2image, and Camelot.

3. **Design Choices:**
    - Chose Pytesseract for OCR due to its simplicity and compatibility with various image formats.
    - Utilized pdf2image to convert PDFs to images, making them suitable for OCR.
    - Implemented regex patterns to extract key-value pairs and table data from OCR text.
    - Incorporated OpenCV for image preprocessing to enhance OCR accuracy.

4. **Challenges Faced:**
    - Accuracy: Achieving accurate OCR results, especially with scanned images containing noise or complex layouts, was challenging.
    - Table Extraction: Extracting structured data from tables embedded in PDFs or images required careful handling due to variations in formatting.
    - Performance: Processing large volumes of PDFs or images efficiently while maintaining accuracy posed a performance challenge.

5. **Additional Tools:**
    - Table Transformer: For extracting data from tables in PDFs, Table Transformer, or similar tools, can provide better accuracy and efficiency.
    - AWS Textract: For large-scale data extraction tasks, AWS Textract offers a more scalable and robust solution compared to local Python libraries.

**Instructions:**
1. **Setup Environment:**
    - Install Python (if not already installed).
    - Install required libraries: `pytesseract`, `PIL`, `pdf2image`, `opencv-python`, `pandas`.

2. **Run Application:**
    - Place the PDF files or scanned images in the specified directory.
    - Execute the provided Python script to extract data: `python app.py`.
    - The script will process the files, extract data, and save it to a CSV file named `extracted_data.csv`.

3. **Considerations:**
    - Utilize Specialized OCR Services: For tasks requiring better accuracy and scalability, consider leveraging specialized OCR services like AWS Textract. These services are designed to handle large-scale data extraction tasks more efficiently and accurately than local Python libraries.
    - Explore Additional Tools:
      Table Transformer: Consider using tools like Table Transformer, which offer advanced capabilities for extracting structured data from tables in PDFs. These tools can streamline the extraction process and handle complex table structures effectively.
      

**Conclusion:**
This documentation outlines a Python-based approach to extract data from PDFs and scanned images, highlighting design choices, challenges, and recommendations for improving accuracy and scalability. By following the provided instructions and considerations, users can efficiently extract structured data from unstructured sources for further analysis and processing.
