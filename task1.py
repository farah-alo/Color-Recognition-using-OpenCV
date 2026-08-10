import cv2

# Read the image
img = cv2.imread("color_recognition/Task1/color.jpg")

# Check if the image was loaded
if img is None:
    print("Error: Could not read color.jpg")
    exit()

# Convert image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range for green color
lower_green = (35, 50, 50)
upper_green = (85, 255, 255)

# Create a mask for green color
mask = cv2.inRange(hsv, lower_green, upper_green)

# Display the original image and the detected green color
cv2.imshow("Original Image", img)
cv2.imshow("Green Color", mask)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()