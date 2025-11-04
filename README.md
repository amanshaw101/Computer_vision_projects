# 🧠 Computer Vision Projects 

A collection of beginner to intermediate-level **Computer Vision** projects developed using **OpenCV**, **NumPy**, and **Matplotlib**.  
Each project demonstrates key concepts of image processing, object detection, and real-time computer vision applications.

---

## 📁 Project List

### 1️⃣ Basic Image Filtering and Edge Detection
**Tech Stack:** OpenCV, Matplotlib  
**Description:**  
Applies essential image processing techniques such as **grayscale conversion**, **Gaussian blurring**, and **Canny edge detection**.  
The results are visualized using Matplotlib in a 2x2 grid layout for easy comparison.

**Features:**
- Resize and preprocess input images  
- Apply Gaussian smoothing filter  
- Perform edge detection using the Canny algorithm  
- Display results in a comparative visualization  

📸 *Output Example:*  
> Original → Grayscale → Blurred → Edge Detected

---

### 2️⃣ Image Contrast and Brightness Enhancement
**Tech Stack:** OpenCV, NumPy, Matplotlib  
**Description:**  
Demonstrates how to enhance image visibility and quality using **contrast (α)** and **brightness (β)** adjustments through OpenCV’s `convertScaleAbs()` method.

**Features:**
- Dynamically control image contrast and brightness  
- Improve low-light or dull images  
- Save enhanced output automatically  

⚙️ *Formula:*  
`new_image = alpha * image + beta`

---

### 3️⃣ Traffic Sign Recognition
**Tech Stack:** Python, TensorFlow/Keras, OpenCV, Tkinter  
**Description:**  
A deep learning-based system for recognizing **traffic signs** from the **GTSRB dataset** (43 classes, 39K+ images).  
Deployed as a real-time **Tkinter GUI** application.

**Highlights:**
- CNN classifier achieving **98.3% accuracy**  
- Real-time prediction interface  
- Model trained on 43 traffic sign categories  

🏆 *Achievement:*  
> Accuracy: **98.3% (Test Set)**

---

### 4️⃣ Real-Time Face Detection using Haar Cascade Classifier
**Tech Stack:** OpenCV, Python  
**Description:**  
Detects human faces from live webcam feed using OpenCV’s **Haar Cascade Classifier**.  
Displays live FPS and bounding boxes around detected faces.

**Features:**
- Real-time face detection with bounding boxes  
- FPS (Frames Per Second) counter for performance tracking  
- Smooth video feed with OpenCV window handling  

🎥 *How it works:*  
- Captures video stream  
- Converts each frame to grayscale  
- Detects faces using `haarcascade_frontalface_default.xml`  
- Annotates live feed with rectangles and labels  

---

### 5️⃣ Real-Time Color Detection using HSV Trackbars
**Tech Stack:** OpenCV, NumPy  
**Description:**  
Interactive real-time color detection system that isolates colors based on **HSV range values** using adjustable trackbars.

**Features:**
- HSV color space conversion  
- Interactive color range tuning using sliders  
- Dynamic mask and result visualization  

🎨 *Use Case:*  
> Useful for detecting specific colors in objects, robotics, and industrial sorting applications.

---

