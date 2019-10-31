#encoding:utf-8
import pytesseract
from PIL import Image

image=Image.open(r'E:\pic.png')
vcode=pytesseract.image_to_string(image)
Image._show(image)
print(vcode)