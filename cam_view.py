import cv2

vid = cv2.VideoCapture(1)

while (True):

    ret, frame = vid.read()

    cv2.imshow('TEST VID CAPT', frame)

    if cv2.waitKey(1) == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()