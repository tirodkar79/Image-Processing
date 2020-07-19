import numpy as np
from cv2 import cv2

def click_events(event, x, y, flag, param):
    global img
    global points
    if event == cv2.EVENT_LBUTTONDOWN:

        img = cv2.circle(img, (x,y), 5, (255,255,0), -1)
        points.append((x,y))

        if len(points) >= 2:
            img = cv2.line(img, points[-1], points[-2], (255,0,0), 3)

        cv2.imshow("image", img)

img = np.zeros((512,512,3), np.uint8)
points = []
cv2.imshow("image", img)

cv2.setMouseCallback("image", click_events)

cv2.waitKey(0)
cv2.destroyAllWindows()