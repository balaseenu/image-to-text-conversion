#python image to text converion

from PIL import Image
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print('bala')
#Define path to images folder
path_to_images = r'C:/Users/admin/Downloads/WSR/'
print('image')
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
print('came')
#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file name in the folder
    print(file_names)
    for file_name in file_names:
        print(file_name)
        #Open image with PIL
        img = Image.open(path_to_images + file_name)

        #Extract text from image
        text = pytesseract.image_to_string(img)

        print(text)