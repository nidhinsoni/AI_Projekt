import numpy as np
import cv2
import pandas as pd
import openpyxl
import tkinter as tk
import time

# Create the Tkinter window
window = tk.Tk()
window.title("Information")
window.geometry("1280x720")  # Width x Height
window.configure(bg="black")

# Create the "Number of Defects Detected" label
defects_label = tk.Label(window, text="Number of Defects Detected =", fg="white", bg="black", font=("Arial", 16))
comment_label = tk.Label(window, text="Comment/Result =", fg="white", bg="black", font=("Arial", 16))
defects_label.grid(row=0, column=0, padx=10, pady=10)
comment_label.grid(row=1, column=0, padx=10, pady=10)


cap = cv2.VideoCapture(0) # Open the camera

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    #CANNY EDGE DETECTION METHOD
    # Apply Gaussian blur to the frame
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    # Find edges in the grayscale frame
    edges = cv2.Canny(gray, 100, 200)

    # Apply morphological operations (dilation and erosion) to remove noise
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Create a circular mask
    mask = np.zeros_like(edges)
    center_x = frame.shape[1] // 2
    center_y = frame.shape[0] // 2
    circle_radius_inner = 100
    circle_radius_outer = 270
    cv2.circle(mask, (center_x, center_y), circle_radius_outer, (255, 255, 255), -1)
    cv2.circle(mask, (center_x, center_y), circle_radius_inner, (0, 0, 0), -1)

    # Apply the circular mask to the edges
    masked_edges = cv2.bitwise_and(edges, mask)

    # Convert the masked edge image to a color image
    masked_edges_color = cv2.cvtColor(masked_edges, cv2.COLOR_GRAY2BGR)

    # Find contours in the masked edge image
    contours, _ = cv2.findContours(masked_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    count=0

    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)

        # Set a threshold for the defect size
        if area > 10:  # Adjust the threshold as needed
            # Get the bounding rectangle for the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Draw a red rectangle over the defect on the color edge image
            cv2.rectangle(masked_edges_color, (x, y), (x + w, y + h), (0, 0, 255), 2)
        count += 1

    #BLACK PIXEL DETECTION METHOD

    kernel2 = np.ones((5, 5), np.uint8)
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred2 = cv2.GaussianBlur(gray2, (5, 5), 0)
    (T, thresh) = cv2.threshold(blurred2, 50, 255, cv2.THRESH_BINARY)

    # Apply circular mask to the thresholded image
    masked_thresh = cv2.bitwise_and(thresh, mask)

    opening2 = cv2.morphologyEx(masked_thresh, cv2.MORPH_OPEN, kernel)

    # Find contours in the resulting image
    contours, _ = cv2.findContours(opening2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the contours and draw rectangles over defects
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)

        # Set a threshold for the defect size
        if area > 1:  # Adjust the threshold as needed
            # Get the bounding rectangle for the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Draw a red rectangle over the defect on the color edge image
            cv2.rectangle(opening2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # *******************************************

    # Draw a small cross at the center of the frames
    frame_with_cross = frame.copy()
    edges_color_with_cross = masked_edges_color.copy()
    opening2_with_cross = cv2.cvtColor(opening2, cv2.COLOR_GRAY2BGR)

    # Get the center coordinates of the frames
    center_x = frame.shape[1] // 2
    center_y = frame.shape[0] // 2

    # Set the length of the cross lines (adjust as desired)
    line_length = 20

    # Draw the horizontal line of the cross
    cv2.line(frame_with_cross, (center_x - line_length, center_y), (center_x + line_length, center_y), (0, 0, 255), 2)
    cv2.line(edges_color_with_cross, (center_x - line_length, center_y), (center_x + line_length, center_y),
             (0, 0, 255), 2)
    cv2.line(opening2_with_cross, (center_x - line_length, center_y), (center_x + line_length, center_y), (0, 0, 255),
             2)

    # Draw the vertical line of the cross
    cv2.line(frame_with_cross, (center_x, center_y - line_length), (center_x, center_y + line_length), (0, 0, 255), 2)
    cv2.line(edges_color_with_cross, (center_x, center_y - line_length), (center_x, center_y + line_length),
             (0, 0, 255), 2)
    cv2.line(opening2_with_cross, (center_x, center_y - line_length), (center_x, center_y + line_length), (0, 0, 255),
             2)

    # Draw a inner circle around the cross
    cv2.circle(frame_with_cross, (center_x, center_y), circle_radius_inner, (255, 0, 0), 2)
    cv2.circle(edges_color_with_cross, (center_x, center_y), circle_radius_inner, (255, 0, 0), 2)
    cv2.circle(opening2_with_cross, (center_x, center_y), circle_radius_inner, (255, 0, 0), 2)

    # Draw a outer circle around the cross
    cv2.circle(frame_with_cross, (center_x, center_y), circle_radius_outer, (255, 0, 0), 2)
    cv2.circle(edges_color_with_cross, (center_x, center_y), circle_radius_outer, (255, 0, 0), 2)
    cv2.circle(opening2_with_cross, (center_x, center_y), circle_radius_outer, (255, 0, 0), 2)

    # Display the frames with the cross
    cv2.imshow('Original Image with Cross', opening2)
    #cv2.imshow('Canny Edge Detection with Cross', edges_color_with_cross)
    #cv2.imshow('MorphologyEx Detection with Cross', opening2_with_cross)

#EXCEL IMPORT/EXPORT
    # Resize frames to have the same dimensions for display
    frame_with_cross = cv2.resize(frame_with_cross, (720, 405))
    edges_color_with_cross = cv2.resize(edges_color_with_cross, (720, 405))
    opening2_with_cross = cv2.resize(opening2_with_cross, (720, 405))
    information_window = np.zeros((405, 720, 3), np.uint8)

    # Draw text on the information window
    cv2.putText(information_window, "Number of Defects Detected: " + str(count),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Arrange the frames in a 2x2 grid
    top_row = np.hstack((frame_with_cross, edges_color_with_cross))
    bottom_row = np.hstack((opening2_with_cross, information_window))
    grid = np.vstack((top_row, bottom_row))

    # Display the grid of frames
    cv2.imshow('Frames', grid)


    #INFORMATION WINDOW
    #window.update()


    if cv2.waitKey(1) == ord('q'):
        break
    #time.sleep(0.5)

cap.release()  # Release the camera
cv2.destroyAllWindows()

# Close the information window
window.destroy()


