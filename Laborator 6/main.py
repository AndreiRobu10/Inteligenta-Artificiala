import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread(r"C:\Users\andre\Desktop\placuta.png")
#img = cv2.resize(img, (800, 600))
gray = cv2.cytColor(img, cv2.COLOR_BGRGRAY)
#Imagine Gri

for c in contur:
    peri = cv2.arcLenght(c, True)
    approx = cv2.approxPoly(c, 0.018 * pery = true)
