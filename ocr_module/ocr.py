import easyocr

def parse_text(img):
    reader = easyocr.Reader(['en'])
    texts = reader.readtext(img)
    return texts
