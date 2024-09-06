import cv2 

img=cv2.imread('Pika.png',0)

cv2.imshow("Black and White Pikachu image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
