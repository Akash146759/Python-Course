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
    elif filter_type == 'edge_canny':
        return cv2.Canny(frame, 100, 200)
    elif filter_type == 'edge_sobel':
        sobel_x = cv2.Sobel(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.CV_64F, 1, 0, ksize=5)
        sobel_y = cv2.Sobel(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.CV_64F, 0, 1, ksize=5)
        return cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    elif filter_type == 'edge_laplacian':
        return cv2.Laplacian(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.CV_64F)
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
    elif key == ord('c'):
        filter_type = 'edge_canny'
    elif key == ord('x'):
        filter_type = 'edge_sobel'
    elif key == ord('l'):
        filter_type = 'edge_laplacian'
    elif key == ord('n'):
        filter_type = 'normal'

cap.release()
cv2.destroyAllWindows()
