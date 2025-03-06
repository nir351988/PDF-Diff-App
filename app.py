from flask import Flask, request, redirect, url_for, flash
import difflib
from PyPDF2 import PdfReader
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages

def extract_text_from_pdf_file(file_stream):
    """
    Extracts text from a PDF provided as a file-like stream.
    :param file_stream: A file-like object containing the PDF.
    :return: Extracted text as a single string.
    """
    text = []
    try:
        # Initialize PdfReader with the file stream.
        reader = PdfReader(file_stream)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
            else:
                text.append("[No extractable text]")
    except Exception as e:
        raise Exception(f"Error reading PDF: {e}")
    return "\n".join(text)

@app.route('/')
def index():
    """
    Renders the homepage with a form for PDF uploads.
    """
    return '''
    <!doctype html>
    <html>
      <head>
        <title>PDF Diff Web App</title>
      </head>
      <body>
        <h1>Upload Two PDF Files to Compare</h1>
        <form method="post" action="/diff" enctype="multipart/form-data">
          <label>PDF 1:</label>
          <input type="file" name="pdf1" accept="application/pdf"><br><br>
          <label>PDF 2:</label>
          <input type="file" name="pdf2" accept="application/pdf"><br><br>
          <input type="submit" value="Compare PDFs">
        </form>
      </body>
    </html>
    '''

@app.route('/diff', methods=['POST'])
def diff():
    """
    Processes the uploaded PDFs, extracts text, creates an HTML diff, and returns it.
    """
    # Validate that both files were uploaded.
    if 'pdf1' not in request.files or 'pdf2' not in request.files:
        flash("Both PDF files must be uploaded")
        return redirect(url_for('index'))
    
    file1 = request.files['pdf1']
    file2 = request.files['pdf2']

    if file1.filename == "" or file2.filename == "":
        flash("Missing file selection")
        return redirect(url_for('index'))

    try:
        # Extract text from the two PDF streams.
        text1 = extract_text_from_pdf_file(file1.stream)
        text2 = extract_text_from_pdf_file(file2.stream)
    except Exception as e:
        return f"Error processing PDFs: {e}"

    # Generate a side-by-side HTML diff.
    diff_generator = difflib.HtmlDiff()
    diff_html = diff_generator.make_file(text1.splitlines(), text2.splitlines(), fromdesc='PDF 1', todesc='PDF 2')
    
    return diff_html

if __name__ == '__main__':
    # Run the app on all available IPs at port 5000.
    app.run(host='0.0.0.0', port=5000, debug=True)