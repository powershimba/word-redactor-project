
<!-- PROJECT LOGO -->
<br />
<div align="center"
  <a href="https://github.com/powershimba/jigo_project_redact_words_from_pdf">
    <img src="/img/jigoai_logo.png" alt="Logo" height="80">
  </a>

<!-- PROJECT TITLE-->
<h3 align="center">Redact Words from PDF</h3>
    <a href="https://github.com/github_username/repo_name">View Demo</a>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- DEMO VIDEO -->
Web App to redact sensitive information in PDF.

Simply upload document, 
Select words to redact, 
Download redacted version.

Built by python and streamlit

![Demo Screenshot](/img/demo1.png)
![Demo Screenshot](/img/demo2.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Discription

#### User uses in 3 steps
1. Upload PDF document 
2. Enter the words to redact
3. Review and Download redacted PDF

#### Web app operates in 3 steps
##### 1. Rendering
* It renders uploaded PDF iterating each page
* Flie: `render.py`
* Library: `pypdfium2`
    https://pypdfium2.readthedocs.io/en/stable/
##### 2. Redacting
* Change `redacted_word` into `changed_word`
    * `redacted_word` : 
        It can be customized not only string but also patterns using regex
    * `changed_word`: 
        It is created based on the number of upper and lower characters of `redacted_word` to customize the length of the word
* File: `redact.py`
* library: `pdf_redactor`
    https://github.com/vitalbeats/pdf-redactor
##### 3. Highlighting
* Highlight the redacted words with black box.
    * It parses text in PDF and compare each text with `changed_word`
    * Designates the position(`rect`) of `changed_word` and fill the box in black color.
* File: `highlight.py`
* Library: 
    - `pdfminer`
        https://github.com/euske/pdfminer
    - `PyPDF2`
        https://pypdf.readthedocs.io/en/latest/index.html

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to Run Locally

1. Clone the repo
```
    git clone https://github.com/powershimba/jigo_project_redact_words_from_pdf
```

2. Install dependencies
```
    pip install -r requirements.txt
```

3. Run streamlit
```
    streamlit run ./src/app.py
```


<!-- LICENSE -->
## License

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jigoai Labs - https://jigo.ai/labs

Project Link: [https://github.com/powershimba/repo_namejigo_project_redact_words_from_pdf](https://github.com/powershimba/jigo_project_redact_words_from_pdf)

<p align="right">(<a href="#readme-top">back to top</a>)</p>