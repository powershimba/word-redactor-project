<!-- PROJECT TITLE-->
<h3 align="center">Redact Words from PDF</h3>
</div>

<!-- ABOUT THE PROJECT -->
### User uses in 3 steps
1. Upload PDF document 
2. Enter the words to redact
3. Review and Download redacted PDF

### Web app operates in 3 steps
#### 1. Rendering
* It renders uploaded PDF iterating each page
* Flie: `render.py`
* Library: `pypdfium2`
    https://pypdfium2.readthedocs.io/en/stable/
#### 2. Redacting
* Change `redacted_word` into `changed_word`. Redacted word can be specific words or phrase, and pattern(regex). Changed word is created using the function in `options.content_filters`
* File: `redact.py`
* library: `pdf_redactor`
    https://github.com/vitalbeats/pdf-redactor
#### 3. Highlighting
* Highlight the `changed_word` with black box.
* File: `highlight.py`
* Library: 
    - `pdfminer`
        https://github.com/euske/pdfminer
    - `PyPDF2`
        https://pypdf.readthedocs.io/en/latest/index.html

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### How to Run Locally

1. Clone the repo
```
    git clone https://github.com/powershimba/jigo_project_redact_words_from_pdf
```

2. Install dependencies
```
    pip3 install -r requirements.txt
```

3. Run streamlit
```
    streamlit run ./src/app.py
```