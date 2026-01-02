# 🚀 AutoPoint-3D-Scanner

**AutoPoint-3D-Scanner** is an innovative open-source project designed to solve a common problem in 3D Laser Scanning: the "Black Mask" or "Operator Shadow" (Nadir mask) in LGS/E57 files. 

When viewing a setup point in tools like TruView, the area behind the camera is often hidden by a black mask. This software aims to automatically fill those gaps and generate **Virtual Setup Points** for a clear, 360-degree view, making it easier to design accurate floor plans.

---

## 🌟 Key Features
- **Auto Mask Removal:** Automatically removes the black operator shadow behind the camera.
- **Virtual Setup Point Generation:** Creates new camera viewpoints in areas where data is missing.
- **AI-Powered Inpainting:** Uses Generative AI to predict and fill hidden walls or doors.
- **Floor Plan Optimization:** Specifically designed to help surveyors and architects see through blind spots.
- **Multi-Format Support:** Focused on `.E57`, `.LAS`, and processing `.LGS` data.

---

## 🛠️ How It Works (The Logic)
1. **Data Parsing:** Reads 3D Point Cloud data from exported scan files.
2. **Void Detection:** Identifies the "Blind Spots" (black masks) where the scanner was blocked.
3. **Point Projection:** Takes image data from nearby setup points to fill the current view's black area.
4. **Virtual Camera:** Generates a new panoramic view by stitching data from multiple angles.

---

## 💻 Tech Stack
- **Language:** Python
- **3D Libraries:** [Open3D](http://www.open3d.org/), NumPy
- **Image Processing:** OpenCV, Pillow
- **AI Integration:** PyTorch (for AI Inpainting)
- **GUI:** (Planned) PyQt or Streamlit

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed. Then install the required libraries:
```bash
pip install open3d numpy opencv-python
