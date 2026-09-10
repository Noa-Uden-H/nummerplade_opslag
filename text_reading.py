def ocr(imgpath,imname):
    import cv2
    import pytesseract as tess
    from matplotlib import pyplot as plt

    img = cv2.imread(imgpath)
    cv2.imshow(imname,img)

    cv2.waitKey(0) # Waits for any key
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    # import pathlib
    import os
    # import cv2

    imagesfolder = os.path.expanduser("~\\OneDrive - TEC\\Documents\\hcoe\\2.m\\informatik_b\\5_machinelearning\\Projekt\\nrplates")
    
    for img in os.scandir(imagesfolder):
        if img.is_file():
            path = img.path
            ocr(path,str(img))
