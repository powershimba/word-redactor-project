import streamlit as st
import module

# Layout
st.title('Redact words from PDF docs')
col1, col2 = st.columns(2)

# Get the path of the uploaded file
with col1:
    uploaded_file = st.file_uploader("Upload a file", type=None)
    if uploaded_file:
        file_path = module.get_path(uploaded_file)
        st.caption("File Path: " + file_path)

# Display the original PDF
        st.subheader("Original PDF")
        module.render_pdf(file_path)        

# Insert the words to redact
with col2:
    with st.form(key='my_form'):
        text_input = st.text_input(label='Enter the words to redact')
        submit_button = st.form_submit_button(label='Redact')
    # st.caption("- Redacted words will be replaced with 'REDACTED'")
    # st.caption("- It's case-sensitive")
    st.text("Redact words: " + text_input)

# Display the redacted PDF
    if submit_button:
        new_file_path = module.redact(file_path, text_input)
        st.caption("File path: " + new_file_path)
        st.subheader("Redacted PDF")
        module.render_pdf(new_file_path)