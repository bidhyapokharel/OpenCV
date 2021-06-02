import numpy as np
import cv2

img = np.zeros([512,512,3], np.uint8)

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_black.jpg',img)
    cv2.destroyAllWindows()
else:
   cv2.destroyAllWindows() 