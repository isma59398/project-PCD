import cv2
import numpy as np

img = cv2.imread("Isma2.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Isma Original", img)
cv2.imshow("Gmabar Isma Grayscale", gray)


cv2.waitKey(0)
cv2.destroyAllWindows()