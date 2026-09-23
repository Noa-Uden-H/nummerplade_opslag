def IP(image):
    import cv2

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("greyscale", img_gray)


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

    IP(image)

