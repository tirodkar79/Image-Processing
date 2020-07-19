from cv2 import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blurred=cv2.GaussianBlur(gray,(5,5),0)

        edged=cv2.Canny(blurred,30,50)

        cv2.imshow('Videos', edged)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()