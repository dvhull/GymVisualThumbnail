# 📌 GymVisual Thumbnail Generator  

## 🔹 Overview  
This Python script processes **MP4 video files**, extracts a frame, removes the **green screen background**, and resizes the image into a **square format** while maintaining transparency.  

## 🚀 Features  
- ✅ Automatically extracts a frame from each **MP4 video** in the input folder.  
- ✅ Removes **green screen backgrounds** and replaces them with **transparency**.  
- ✅ Crops the **non-transparent area** and **resizes it into a square**.  
- ✅ Saves the processed image as a **PNG file with transparency**.  

## 🔹 Requirements  

### 📦 Dependencies  
Before running the script, install the required Python libraries:  

```bash
pip install opencv-python numpy
```

## 🖥️ System Requirements
- Python 3.x
- OpenCV (cv2) for image processing
- NumPy (numpy) for numerical operations
- Works on Windows, macOS, and Linux

## 🔹 Installation & Setup

1️⃣ Clone the Repository (or Save the Script)

```bash
git clone https://github.com/dvhull/GymVisualThumbnail.git
cd GymVisualThumbnail
```

2️⃣ Set Up Input & Output Folders
Place all MP4 videos in the input_folder.
The script will save thumbnails in the output_folder.
Modify the paths in the script to match there locations:

```bash
input_folder = '/Users/davidhull/Documents/PythonStuff/input_folder'
output_folder = '/Users/davidhull/Documents/PythonStuff/output_2'
```

3️⃣ Run the Script
```bash
python3 thumbnail_generator.py
```

## 🔹 How It Works

1️⃣ Reads All MP4 Files
The script scans the input_folder for .mp4 video files and processes them one by one.

2️⃣ Extracts a Frame from Each Video
It captures a frame from the video and converts it to HSV format to detect the green screen color range.

3️⃣ Removes Green Background & Crops the Image
It creates a mask to remove the green areas.
Converts the frame to BGRA (with transparency).
Crops the bounding box of non-transparent pixels.

4️⃣ Resizes the Image to a Square
Finds the largest dimension (width or height).
Adds padding to ensure a perfect square.

5️⃣ Saves the Final Image
Saves the processed PNG file with transparency in the output_folder.

## 🔹 Example Output

🎥 Input:
📁 input_folder/video1.mp4

🖼️ Output:
📁 output_2/video1_thumbnail.png (cropped, transparent, and square)





