import cv2

img = cv2.imread('lena.jpg', 1)
img = cv2.line(img, (0,0), (100,100) ,(0,255,255), 5)
resized_image = cv2.resize(img, (500, 500)) 

font = cv2.FONT_HERSHEY_COMPLEX
resized_image = cv2.putText(img, 'OpenCV', (10,500), font,4, (255,255,255), 10, cv2.LINE_AA)
cv2.imshow('image',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 

