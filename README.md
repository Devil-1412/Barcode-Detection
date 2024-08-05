# Real-Time Barcode Detection with YOLOv10 and OpenCV

This project implements real-time barcode detection using a custom-trained YOLOv10 model and OpenCV for processing webcam frames.

## Overview

The project involves the following steps:
1. **Dataset Preparation**: A custom barcode dataset was sourced from RoboVision.
2. **Model Training**: The YOLOv10 model was trained on Google Colab using the custom dataset.
3. **Model Deployment**: The trained model weights were used in a Python script to detect barcodes in real-time from a webcam feed.

## Features

- **Real-Time Detection**: Captures video frames from the webcam and processes them to detect barcodes.
- **Confidence Display**: Displays the confidence score for detected barcodes.

## Setup

### Prerequisites

- Python 3.x
- OpenCV
- Ultralytics YOLOv10

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/barcode-detection-yolo.git
