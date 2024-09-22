import cv2 

img=cv2.imread('watermelon.png',0)

cv2.imshow("Monochrome watermelon",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
