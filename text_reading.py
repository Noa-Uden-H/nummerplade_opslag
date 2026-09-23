def ocr(img, imname) -> str:
    import cv2
    import pytesseract as tess

    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    cv2.imshow(imname,img)
    extracted_text = tess.image_to_string(img, config="--psm 6")

    cv2.waitKey(0) # Waits for any key
    cv2.destroyAllWindows()
    return extracted_text

def ocr_test(imgpath, imname) -> str:
    import cv2
    import pytesseract as tess

    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = cv2.imread(imgpath)
    #--Remove--
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (3,3), 1)
    #----------
    thresh = cv2.threshold(blur, 110,255, cv2.THRESH_BINARY)[1]
    cv2.imshow(imname,thresh)
    extracted_text = tess.image_to_string(thresh, config="--psm 6")

    cv2.waitKey(0) # Waits for any key
    cv2.destroyAllWindows()
    return extracted_text

if __name__ == "__main__":
    # import pathlib
    import os
    # import cv2

    imagesfolder = os.path.expanduser("~\\OneDrive - TEC\\Documents\\_hcoe\\3.m\\informatik_b\\5_machinelearning\\Projekt\\nrplates")
    
    for img in os.scandir(imagesfolder):
        if img.is_file():
            path = img.path
            text = ocr_test(path,str(img))
            print(text)
