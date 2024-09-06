import cv2

img=cv2.imread("Pika.png",1)

cv2.imshow("Pikachu Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
