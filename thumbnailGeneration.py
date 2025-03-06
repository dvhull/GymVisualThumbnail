import cv2
import numpy as np
import os

# Define the lower and upper bounds of the green color range
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# Input folder containing video files. 
input_folder = '/Users/davidhull/Documents/PythonStuff/input_folder'

# Output folder for saving images
output_folder = '/Users/davidhull/Documents/PythonStuff/output_2'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through video files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):
        video_path = os.path.join(input_folder, filename)

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Check if the video opened successfully
        if not cap.isOpened():
            print(f"Error: Could not open video {filename}")
            continue

        # Create an output image filename based on the video filename. 
        output_filename = os.path.splitext(filename)[0] + '_thumbnail.png'
        output_path = os.path.join(output_folder, output_filename)

        while True:
            # Capture a frame from the video
            ret, frame = cap.read()

            # Check if the frame was read successfully
            if not ret:
                break

            # Create a mask that selects the green color
            mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower_green, upper_green)

            # Invert the mask (to select the non-green areas)
            mask_inv = cv2.bitwise_not(mask)

            # Create an image with a transparent background
            result = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            result[:, :, 3] = mask_inv

             # Get the dimensions of the image
            h, w = result.shape[:2]

            # Find the bounding box of the non-transparent pixels
            coords = cv2.findNonZero(result[:, :, 3])
            if coords is not None:
                x, y, w_box, h_box = cv2.boundingRect(coords)

                # Calculate the size of the square
                max_size = max(w_box, h_box)

                # Calculate the padding needed
                pad_x = (max_size - w_box) // 2
                pad_y = (max_size - h_box) // 2

                # Create a new square image with transparent background
                square_image = np.zeros((max_size, max_size, 4), dtype=np.uint8)

                # Place the original content in the center of the square image
                square_image[pad_y:pad_y+h_box, pad_x:pad_x+w_box] = result[y:y+h_box, x:x+w_box]

                # Replace the result with the square image
                result = square_image

            # Save the result as an image with transparency
            cv2.imwrite(output_path, result)

            # Exit the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture object
        cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
