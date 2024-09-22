import cv2

img=cv2.imread("watermelon.png",1)

cv2.imshow("watermelon",img)

cv2.waitKey(0)
cv2.destroyAllWindows()