#Real-Time Barcode Detection with YOLOv10 and OpenCV
This project implements real-time barcode detection using a custom-trained YOLOv10 model and OpenCV for processing webcam frames.

##Overview
The project involves the following steps:
Dataset Preparation: A custom barcode dataset was sourced from RoboVision.
Model Training: The YOLOv10 model was trained on Google Colab using the custom dataset.
Model Deployment: The trained model weights were used in a Python script to detect barcodes in real-time from a webcam feed.

##Features
Real-Time Detection: Captures video frames from the webcam and processes them to detect barcodes.
Confidence Display: Displays the confidence score for detected barcodes.

##Setup
###Prerequisites
Python 3.x
OpenCV
Ultralytics YOLOv10
###Installation
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/barcode-detection-yolo.git
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Download the trained YOLOv10 model weights and place them in the weights directory.
Running the Barcode Detection
Run the barcode detection script:
bash
Copy code
python barcode_detection.py
The webcam feed will open, and detected barcodes along with their confidence scores will be displayed in real-time.
Training the YOLOv10 Model
The YOLOv10 model was trained on Google Colab using a custom dataset from RoboVision. Follow these steps to replicate the training:

Prepare Dataset: Upload the dataset to Google Colab.
Install Dependencies: Install the YOLOv10 model and other required libraries.
python
Copy code
!pip install git+https://github.com/THU-MIG/yolov10.git
!pip install roboflow supervision
Train Model: Use the training script provided in the repository to train the model on your dataset.
Export Weights: Save the trained model weights and download them for deployment.
Contributing
If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
