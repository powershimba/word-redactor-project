import streamlit as st

from render import *
from redact import *
from highlight import *
from module import *

import tempfile
import os

st.title('Redact Words in PDF')
st.markdown('''
            :rainbow[Redact sensitive information from PDF documents.]\n
            Be aware that this tool is :blue-background[case sensitive].  
            :grey[i.e. 'CONSULTANT' is different from 'consultant']\n
            We don't save any files on the server.  
            We don't override the original file.
            ''')
st.divider()
col1, col2 = st.columns(2)

with col1:

    # Upload a PDF file
    uploaded_file = st.file_uploader("Upload a file", type=None)
    file_path_origin = None
    
    if uploaded_file:
        
        # Save the uploaded file to a temporary directory
        temp_dir = tempfile.mkdtemp()
        file_path_origin = os.path.join(temp_dir, "document.pdf")
        with open(file_path_origin, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Render the uploaded file
        st.write("#")  
        st.subheader("Original PDF")
        st.write("#")  
        st.write("")
        render_pdf(file_path_origin)        

with col2:

    # Get the words to redact
    with st.form(key='my_form'):
        redact_words = st.text_input(label='Enter the words to redact')
        submit_button = st.form_submit_button(label='Redact')
    st.text("Redact words: " + redact_words)

    if submit_button and file_path_origin:

        try:
            # replace words to random words
            changed_word = generate_word(redact_words)
            file_path_redacted = redact(file_path_origin, redact_words, changed_word)

            # Highlight the redacted word with black boxes
            file_path_highlighted = highlight_words(file_path_redacted, changed_word)

            # Download redacted pdf fileW
            st.subheader("Redacted PDF")

            with open(file_path_highlighted, "rb") as f:
                file_downloaded= f.read()

            st.download_button(
                label="Click here to download the redacted PDF", 
                data = file_downloaded,
                file_name="redacted.pdf",)

            render_pdf(file_path_highlighted)


        except Exception as e:
            st.error(f"An error occurred during redaction: {e}")
    
