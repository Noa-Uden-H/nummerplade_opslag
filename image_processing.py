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


if __name__ == "__main__":
    # Sti og filnavn fra din anden kode (Projekt Nummerplade genkendelse)
    mydir = os.path.expanduser(
        "~\\OneDrive - TEC\\Informatik\\3.g\\Machine learning\\Projekt Nummerplade genkendelse\\Billeder_test"
    )
    myfile = "IMG_7076.jpg"

    path = pathlib.Path(mydir, myfile)
    image = cv2.imread(str(path))

    if image is None:
        print(f"Fejl: Kunne ikke finde eller åbne billedet på stien:\n{path}")
    else:
        image = cv2.resize(image, (1000, 600))
        IP(image)