import cv2

# Load the image
image = cv2.imread('D:\EIT Studium\AI Projekt\Python\\kugel_test_edit.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to the grayscale image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 0, 255), 1)

# Display the original image with contours drawn
cv2.imshow('Defects Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()