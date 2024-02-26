import cv2

def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pass


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow(frame )