import tempfile
import pdf_redactor
import re, os

from render import *

def redact(file_path, redacted_word, changed_word):

    # Set options of redactor method
    options = pdf_redactor.RedactorOptions()    
    options.input_stream = open(file_path, "rb")
    
    options.content_filters = [
        (
        re.compile(re.escape(redacted_word)),
        lambda m: changed_word,
        )
    ]

    # Save the redacted file to a temporary directory
    temp_dir = tempfile.mkdtemp()
    new_file_path = os.path.join(temp_dir, "redacted.pdf")

    with open(new_file_path, "wb") as output_file:
            options.output_stream = output_file
            pdf_redactor.redactor(options)

    return new_file_path