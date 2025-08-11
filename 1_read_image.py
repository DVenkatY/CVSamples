import cv2

img1=cv2.imread("images/Butterfly.png")
cv2.imshow("The original image ",img1)
cv2.waitKey(0)

cv2.imwrite("images/saved_original_img.png",img1)