import cv2

img1=cv2.imread("Butterfly.png")

resize=cv2.resize(img1,(80,100))
grey=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(img1,(5,5),0)
edge_detect=cv2.Canny(img1,100,200)

cv2.imshow("original image after resize",resize)
cv2.imshow("original image after grey",grey)
cv2.imshow("original image after blur",blur)
cv2.imshow("original image after edgedetct",edge_detect)
cv2.waitKey(0)
cv2.destroyAllWindows()