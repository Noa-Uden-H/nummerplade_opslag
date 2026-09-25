import os
import pathlib
import cv2


def IP(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    cv2.imshow("greyscale", img_gray)

    thresh = cv2.threshold(img_gray, 1, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#    cv2.imshow("threshold", thresh)

    # cv2.findContours returnerer 2 elementer i nyere OpenCV-versioner
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Filtrér helt små støj-konturer fra
        if cv2.contourArea(contour) < 300:
            continue

        # 1. Tilnærm konturen til en geometrisk form
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # 2. Tjek om formen har 4 hjørner (rektangel / kvadrat)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)

            # Et rektangel har et forhold der afviger fra 1.0 (som er kvadrat)
            shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"

            thresh = thresh[y:y+h, x:x+w]
           

    cv2.imshow("Resultat", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return thresh


def EUC(image):
    INV_image = cv2.bitwise_not(image)
    contours, _ = cv2.findContours(INV_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    EUC_crop = None
    plate_without_EUC = None  # Billedet hvor EU-mærket er fjernet

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue

        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)

            if 0.15 <= ar <= 0.45 and x < image.shape[1] * 0.2:
                # 1. Selve EU-mærket
                EUC_crop = image[y:y+h, x:x+w]
                
                # 2. Nummerpladen hvor EU-mærket er skåret FRA
                # Vi starter ved (x + w), som er lige til højre for EU-mærket
                plate_without_EUC = image[:, x+w:]
                break

    if plate_without_EUC is not None:
        #cv2.imshow("EU Marke", EUC_crop)
        cv2.imshow("Nummerplade uden EU-marke", plate_without_EUC)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return plate_without_EUC
  
if __name__ == "__main__":
    # Sti og filnavn fra din anden kode (Projekt Nummerplade genkendelse)
    mydir = os.path.expanduser(
        "~\\OneDrive - TEC\\Informatik\\3.g\\Machine learning\\Projekt Nummerplade genkendelse\\Billeder_test"
    )
    # myfile = "IMG_7076.jpg"
    myfile = "Screenshot 2026-09-23 144340.png"

    path = pathlib.Path(mydir, myfile)
    image = cv2.imread(str(path))

    if image is None:
        print(f"Fejl: Kunne ikke finde eller åbne billedet på stien:\n{path}")
    else:
        image = cv2.resize(image, (1000, 600))
        plate = IP(image)
        EUC(plate)