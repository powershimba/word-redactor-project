# Extract Text Coordinates using pdfminer.six

# 1. 대소문자 rR 바뀐거 모두 체크 (lower로 바꾼다음에 비교..!) 
# 2. 특수기호 붙은거 

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextLine, LTChar
from PyPDF2.generic import DictionaryObject, NameObject, ArrayObject, FloatObject, TextStringObject
import tempfile
import os
from module import *

def text_coordinates(pdf_path, changed_word):
    text_coords = []
    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    if isinstance(text_line, LTTextLine):
                        for character in text_line:
                            if isinstance(character, LTChar):
                                text_coords.append({
                                    'text': character.get_text(),
                                    'x0': character.bbox[0],
                                    'y0': character.bbox[1],
                                    'x1': character.bbox[2],
                                    'y1': character.bbox[3],
                                    'page': page_layout.pageid - 1 # 0-based index
                                })

    word_coords = []
    current_word = ''
    current_coords = []

    for char_info in text_coords:
        if char_info['text'].isspace():
            if current_word == changed_word:
                word_coords.append(current_coords)
            current_word = ''
            current_coords = []
        else:
            current_word += char_info['text']
            current_coords.append(char_info)

    # Check the last word
    if current_word == changed_word:
        word_coords.append(current_coords)

    return word_coords

# Specify Rectangles in PyPDF2
from PyPDF2 import PdfReader, PdfWriter

def highlight_words(file_path, changed_word):
    word_coordinates = text_coordinates(file_path, changed_word)
    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]

        for word_coords in word_coordinates:
            if len(word_coords) > 0:
                # Assuming all characters of the word are on the same page
                if word_coords[0]['page'] == page_num:
                    x0 = min(char['x0'] for char in word_coords)
                    y0 = min(char['y0'] for char in word_coords)
                    x1 = max(char['x1'] for char in word_coords)
                    y1 = max(char['y1'] for char in word_coords)

                    # Create a rectangle annotation
                    highlight = DictionaryObject()
                    highlight.update({
                        NameObject("/Type"): NameObject("/Annot"),
                        NameObject("/Subtype"): NameObject("/Highlight"),
                        NameObject("/Rect"): ArrayObject([FloatObject(x0), FloatObject(y0), FloatObject(x1), FloatObject(y1)]),
                        NameObject("/QuadPoints"): ArrayObject([FloatObject(x0), FloatObject(y1), FloatObject(x1), FloatObject(y1), FloatObject(x0), FloatObject(y0), FloatObject(x1), FloatObject(y0)]),
                        NameObject("/C"): ArrayObject([FloatObject(0), FloatObject(0), FloatObject(0)]),  # Black color
                        NameObject("/T"): TextStringObject("Highlight")
                    })

                    if "/Annots" in page:
                        page["/Annots"].append(highlight)
                    else:
                        page[NameObject("/Annots")] = ArrayObject([highlight])

        writer.add_page(page)

    # Save the highlighted file to a temporary directory
    temp_dir = tempfile.mkdtemp()
    new_file_path = os.path.join(temp_dir, "highlighted.pdf")
    with open(new_file_path, "wb") as f:
        writer.write(f)
    return new_file_path