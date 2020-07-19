import numpy as np
from cv2 import cv2

def click_event(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        color_selected = np.zeros((512,512,3), np.uint8)

        color_selected[:] = [blue, green, red]
        title = "Color Selected: " + str(blue) + ", " + str(green) + ", " + str(red)
        cv2.imshow(title, color_selected) 

img = cv2.imread("F:/PRATHAM/PYTHON/cv projects/new project/lena.jpg")
cv2.imshow("image", img)

cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
