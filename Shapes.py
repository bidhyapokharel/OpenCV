import cv2

img = cv2.imread('lena.jpg', 1)
img = cv2.line(img, (0,0), (5,5) ,(0,255,0), 5)
resized_image = cv2.resize(img, (1000, 500)) 

cv2.imshow('image',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 

