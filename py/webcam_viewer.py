import cv2

print("WebCam Viewer v1.0")
print("Copyright (c) 2020 miniprime1")
print("[Press q to exit]")

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(113) < 0:
    # press q to exit
    ret, frame = capture.read()
    cv2.imshow("WebCam Viewer", frame)

capture.release()
cv2.destroyAllWindows()