import cv2
import numpy as np

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

#Gaussian for Apple
apple_copy = apple.copy()
qp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    qp_apple.append(apple_copy)

#Gaussian for Orange
orange_copy = orange.copy()
qp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    qp_orange.append(orange_copy)

# Laplasian for Apple
apple_copy = qp_apple[5]
lp_apple = [apple_copy]
for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(qp_apple[i])
    lap_lassian = cv2.subtract(qp_apple[i-1], gaussian_extended)
    cv2.imshow(str(i), lap_lassian)

# Laplasian for Orange
orange_copy = qp_apple[5]
lp_orange = [apple_copy]
for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(qp_orange[i])
    lap_lassian = cv2.subtract(qp_orange[i-1], gaussian_extended)
    cv2.imshow(str(i), lap_lassian)

# Add the left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack(apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):])
    apple_orange_pyramid.append(laplacian)

# Now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)



cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)
cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct )


cv2.waitKey(0)
cv2.destroyAllWindows()