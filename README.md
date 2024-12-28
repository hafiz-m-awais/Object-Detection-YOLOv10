# Glass Liquid Level Detection with YOLO

## Overview
This project detects and classifies the liquid levels in glasses using object detection techniques with YOLOv10 or YOLOv11. It involves:
- Custom dataset creation of transparent glasses containing liquids of various levels (Empty, 25%, Half, 75%, Full).
- Training and evaluation of an object detection model to localize glasses and classify their liquid levels.
- Deployment of an inference GUI for real-time detection on live webcam feeds or recorded videos.

## Key Features
- **Custom Dataset**: Images collected with transparent glasses and varying liquid levels.
- **Object Detection**: YOLOv10/YOLOv11 models trained for glass detection and liquid level classification.
- **GUI Application**: Real-time inference on live webcams and recorded videos.

## Dataset Details
### Data Collection
1. **Glass Types**: Transparent glasses of different shapes and sizes.
2. **Liquids**: At least three types of liquids (e.g., water, juice, etc.).
3. **Image Variations**:
   - Number of glasses: 1 to 3 per image.
   - Liquid levels: Empty, 25%, Half, 75%, Full.
   - Captured from various distances and angles.

### Data Labeling
- Object Detection Labels: Bounding boxes for each glass with liquid level classification.
- Classes: 
  - `empty`
  - `25_percent`
  - `half`
  - `75_percent`
  - `full`

### Data Splits
- **Training Set**: 70%
- **Validation Set**: 20%
- **Test Set**: 10%


## File Descriptions
- **`glass_liquid_level_detect.ipynb`**: Colab notebook for training and evaluating the YOLOv10 model.
- **`inference_gui.py`**: Script for running the inference GUI on live webcam images or recorded videos.
- 
## Instructions to Run
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Glass-Liquid-Level-Detection.git
cd Glass-Liquid-Level-Detection
