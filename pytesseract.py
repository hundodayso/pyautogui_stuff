from PIL import Image

import pytesseract

image = Image.open('screenshot0.png')
text = pytesseract.image_to_string(image)

