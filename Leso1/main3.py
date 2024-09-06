import cv2 

img = cv2.imread('Pika.png',0)

cv2.imshow("B&W Pikachu Image",img)

cv2.imwrite("blackandWhite.png",img)
#saves the image

cv2.waitKey(0)
cv2.destroyAllWindows()