import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe
img = cv2.imread('images/3.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
# Passing the image object to
# image_to_string() function
# This function will
File_object = open(r"informations.txt", "a")
# extract the text from the image
text = pytesseract.image_to_string(img)
File_object.write('\n')
File_object.write(text)
####### Detecting Words
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
for x, b in enumerate(boxes.splitlines()):
    if x == 0:
        continue
    b = b.split()
    print(b)
    if len(b) == 12:
        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
        cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 2)
        cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('Result', img)
File_object.close()
cv2.waitKey(0)
