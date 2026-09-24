import image_processing as imp
import text_reading as ocr
import search
import cv2
import os


imagesfolder = "C:\\temp_cars"
    
for img in os.scandir(imagesfolder):
    if img.is_file():
        path = img.path
        image = cv2.imread(path)
        plate = imp.IP(image)
        
        text = ocr.ocr(plate, str(img))
        print(text)
