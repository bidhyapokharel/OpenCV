import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY)

kernal = np.ones((3,3), np.uint8)
dilation = cv.dilate(mask, kernal, iterations=2)
erosion = cv.erode(mask, kernal, iterations=2)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)

titles = ['Image', 'mask', 'dilation', 'Erosion', 'Opening', 'Closing', 'TopHat']
images = [img, mask, dilation, erosion, opening ,closing, th]
 
for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()