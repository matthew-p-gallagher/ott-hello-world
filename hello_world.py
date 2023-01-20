import requests
import shutil

import cv2
import pytesseract

import os

def pull_image():

    url = "https://preview.redd.it/n93k6oc2wab71.png?width=3840&format=png&auto=webp&v=enabled&s=77f25c006eac0c8aed9f218f8b5f7c6793ec4e7b"
    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open('image.png', 'wb') as f:
            shutil.copyfileobj(res.raw, f)
    else:
        print("Error downloading image")
        exit(1)

def read_text_from_image():

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = cv2.imread('image.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)

    return text

def write_program_with_text(text):
    with open("final.py", "w") as f:
        f.write(text)

def run_program():
    os.system("python final.py")

def clean_up():
    os.remove("image.png")
    os.remove("final.py")

if __name__ == "__main__":
    pull_image()
    text = read_text_from_image()
    write_program_with_text(text)
    run_program()
    clean_up()





