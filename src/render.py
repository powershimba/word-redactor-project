import streamlit as st
import pypdfium2 as pdfium

def render_pdf(file_path):
    pdf = pdfium.PdfDocument(file_path)
     
    # Get the number of pages in the document
    n_pages = len(pdf)

    # Rendering each page
    for i in range(n_pages):
        page = pdf[i] # load a page
        bitmap = page.render(
            scale = 1,    # 72dpi resolution
            rotation = 0, # no additional rotation
        )
        pil_image = bitmap.to_pil()
        st.write(pil_image)
 