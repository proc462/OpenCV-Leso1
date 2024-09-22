import cv2

img = cv2.imread('watermelon.png')
B,G,R = cv2.split(img)
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()