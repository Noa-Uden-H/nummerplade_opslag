def IP(image):
    import cv2

    

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("greyscale", img_gray)

    thresh = cv2.threshold(img_gray, 1, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imshow("threshold", thresh)

    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    i=0
    for contour in contours:

        if i==0:
            i = 1
            continue


    cv2.waitKey(0) 
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import os
    import pathlib
    import cv2
    
    mydir = os.path.expanduser("~\\OneDrive - TEC\\Informatik\\3.g\\Machine learning\\Projekt Nummerplade genkendelse\\Billeder_test")
    
    myfile = "IMG_7076.jpg"
    path = pathlib.Path(mydir, myfile)
    image = cv2.imread(str(path))
    image = cv2.resize(image, (1000, 600))

    IP(image)

