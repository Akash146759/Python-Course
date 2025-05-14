import cv2
import numpy as np

def apply_filter(frame, filter_type):
    if filter_type == 'gray':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'sepia':
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        return cv2.transform(frame, kernel)
    elif filter_type == 'inverted':
        return cv2.bitwise_not(frame)
    elif filter_type == 'blur':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    elif filter_type == 'edge':
        return cv2.Canny(frame, 100, 200)
    return frame

cap = cv2.VideoCapture(0)
filter_type = 'normal'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    filtered_frame = apply_filter(frame, filter_type)
    cv2.imshow('Filtered Video', filtered_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        filter_type = 'gray'
    elif key == ord('s'):
        filter_type = 'sepia'
    elif key == ord('i'):
        filter_type = 'inverted'
    elif key == ord('b'):
        filter_type = 'blur'
    elif key == ord('e'):
        filter_type = 'edge'
    elif key == ord('n'):
        filter_type = 'normal'

cap.release()
cv2.destroyAllWindows()
