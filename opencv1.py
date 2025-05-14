
import opencv as cv2
import numpy as np

# Create a blank image (500x500 pixels, 3 color channels)
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw a line
cv2.line(image, (50, 50), (450, 50), (0, 255, 0), 3)

# Draw a rectangle
cv2.rectangle(image, (100, 100), (400, 300), (255, 0, 0), 3)

# Draw a filled rectangle
cv2.rectangle(image, (120, 120), (380, 280), (0, 0, 255), -1)

# Draw a circle
cv2.circle(image, (250, 250), 50, (255, 255, 0), 3)

# Draw an ellipse
cv2.ellipse(image, (250, 400), (100, 50), 0, 0, 360, (0, 255, 255), 3)

# Draw a polygon (triangle)
pts = np.array([[200, 350], [300, 350], [250, 275]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], isClosed=True, color=(255, 0, 255), thickness=3)

# Add text annotation
cv2.putText(image, 'OpenCV Drawing', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the image
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
