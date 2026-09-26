import image_processing as imp
import text_reading as ocr
import search
import cv2
import os


imagesfolder = r"C:\temp_cars2"
    
for img in os.scandir(imagesfolder):
    if img.is_file():
        print("---------")
        
        path = img.path
        image = cv2.imread(path)
        
        plate = imp.IP(image)
        if plate is None:
            print("Couldn't find a plate")
            continue

        plate_wo_eu = imp.EUC(plate)
        # cv2.imshow("plate",plate)
        # cv2.imshow("woeu",plate_wo_eu)
            
        text = ocr.ocr(plate_wo_eu, str(img))
        print(text)
        if text is None:
            print("Couldn't read plate")
            continue

        text_parsed = search.check_plate(text)
        print(text_parsed)
        if text_parsed is None:
            print("Incorrect plate read")
            continue

        car_info = search.search_plate(text_parsed)
        cv2.imshow(car_info, image)

        cv2.waitKey(0) # Waits for any key
        cv2.destroyAllWindows()
