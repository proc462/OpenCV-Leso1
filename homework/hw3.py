import cv2 

img = cv2.imread('watermelon.png',0)

cv2.imshow("Monochrome Watermelon",img)

cv2.imwrite("MonochromeWatermelon.png",img)
#saves the image

cv2.waitKey(0)
cv2.destroyAllWindows()