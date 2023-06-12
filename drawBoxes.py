import cv2

# Load the image
image = cv2.imread('D:\EIT Studium\AI Projekt\Python\\test_3.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to the grayscale image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours and draw bounding boxes around the defects
count = 0
for contour in contours:
    # Get the bounding box coordinates
    x, y, w, h = cv2.boundingRect(contour)

    # Draw a red rectangle around the defect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)

    count += 1

# Display the original image with contours drawn
cv2.putText(image, "Defects Detected: " + str(count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
cv2.imshow('Defects Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()