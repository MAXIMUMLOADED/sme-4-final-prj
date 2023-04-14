import cv2
import time
import uuid
from tkinter import Image
from PIL import Image
from pytesseract import pytesseract


def tesseract():
    camera=cv2.VideoCapture(0)
    text=""
    id=str(uuid.uuid1())
    fileName='sem_'+id+'.jpg'
    try:
        _,frame=camera.read()
        cv2.imshow('fileName',frame)
        # if cv2.waitKey(1)& 0xFF==ord('s'):
        #if cv2.waitKey():
        #time.sleep(2)
        cv2.imwrite(fileName,frame)
        fileName="AMPM.jpg"
        #text=pytesseract.image_to_string(fileName)
        #print(text)
    finally:    
        camera.release()
        cv2.destroyAllWindows()
        path_to_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        time.sleep(3)
        image_path="test1.jpg"
        pytesseract.tesseract_cmd=path_to_tesseract
        text=pytesseract.image_to_string(fileName)
        #text=pytesseract.image_to_string(Image.open(fileName))
        print(text)
        return text
print(tesseract())
    