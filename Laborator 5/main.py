import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread(r"C:\Users\andre\Desktop\placuta.png")
#img = cv2.resize(img, (800, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Imagine Gri
#cv.imshow('GRAY SCALE IMAGE', gray)
gray = cv2.bilateralFilter(gray, 13, 15, 15)
#Imagine Filtrata
cv2.imshow('FILTERED IMAGE', gray)
edged = cv2.Canny(gray, 30, 200)
#cv2.imshow('CANNY EDGE IMAGE', edged)
contur = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contur = imutils.grab_contours(contur)
contur = sorted(contur, key=cv2.contourArea, reverse=True)[:18]
screenCnt = None
for c in contur:
    peri = cv2.arcLenght = (c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break
if screenCnt is None:
    detected = 0
    print("Nu a fost detectat niciun contor")
else:
    detected = 1

mask = np.zeros(gray.shape, np.unit8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1,)
new_image = cv2.bitwise_and(img, img, mask=mask)
(x, y) = np.where(mask==255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
CROP = gray[topx:bottomx+1, topy:bottomy+1]
text_numar = pytesseract.image_to_string(CROP, config='--psn 10')
img = cv2.resize(img, (500, 300))
CROP = cv2.resize(CROP, (400, 200))
cv2.imshow('DECUPAT', CROP)
cv2.waitkey()
cv2.destroyAllWindows()


