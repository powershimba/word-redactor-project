import streamlit as st
import pypdfium2 as pdfium
import tempfile
import os
import re
import pdf_redactor

def get_path(uploaded_file): 
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, "uploaded.pdf")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    return file_path

# Use pdfium to render the PDF
def render_pdf(file_path):
    pdf = pdfium.PdfDocument(file_path)
    n_pages = len(pdf) # get the number of pages in the document
    
    for i in range(n_pages):
        page = pdf[i] # load a page
        bitmap = page.render(
            scale = 1,    # 72dpi resolution
            rotation = 0, # no additional rotation
        )
        pil_image = bitmap.to_pil()
        st.write(pil_image)
    return

# Use pdf-redactor to redact the words
def redact(file_path, redacted_word):
    options = pdf_redactor.RedactorOptions()    
    options.input_stream = open(file_path, "rb")

    options.content_filters = [
        # compiled regular expression
        (
        re.compile(re.escape(redacted_word)),
        # function to generate replacement text
        lambda m: "REDACTED",
        )
    ]

    temp_dir = tempfile.mkdtemp()
    new_file_path = os.path.join(temp_dir, "redacted.pdf")

    with open(new_file_path, "wb") as output_file:
        options.output_stream = output_file
        pdf_redactor.redactor(options)

    return new_file_path