import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena.jpg")
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)

cv2.imshow("Original image", img)
cv2.imshow("pyrDown 1 image", lr1)
cv2.imshow("pyrDown 2 image", lr2)
cv2.imshow("pyrUp 2 image", hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()