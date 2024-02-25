from io import BytesIO
import pandas as pd
import base64
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from main import process_pdf_and_extract_data
import os
import subprocess
# Your PDF processing functions
# Include pdf_to_images, preprocess_image_for_ocr, extract_data_from_text, extract_highlighted_values, and process_pdf_and_extract_data here

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return "No file uploaded"
    
    file = request.files['file']
    
    # Check if the file is a PDF
    if file.filename.endswith('.pdf'):
        # Save the PDF file to a temporary location
        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(pdf_path)
        
        # Process the PDF file and extract data
        extracted_data = process_pdf_and_extract_data(pdf_path)
        
        # Convert to DataFrame and save to CSV
        df = pd.DataFrame(list(extracted_data.items()), columns=['Key', 'Value'])
        df.to_csv('extracted_data.csv', index=False)
        
        return redirect(url_for('success', data=df.to_html()))
    
    else:
        return "Unsupported file format"

@app.route('/success')
def success():
    # Retrieve the DataFrame from the query parameters
    data_html = request.args.get('data')
    
    # Render the template with the DataFrame
    return render_template('success.html', data_html=data_html)

if __name__ == '__main__':
    app.run(debug=True)
