# 🛡️ AI Deepfake Detection System

A Computer Vision and Deep Learning based system for detecting manipulated facial images and identifying potential deepfakes using a custom-trained ResNet18 model.

---

## 🚀 Features

* Deepfake Image Detection
* Face Detection and Face Extraction
* Confidence Score Generation
* Custom ResNet18 Model
* FastAPI Backend
* React Frontend
* Real vs Deepfake Classification

---

## 🧠 Project Overview

This project analyzes uploaded facial images and predicts whether the image is:

* REAL
* DEEPFAKE

The system automatically:

1. Uploads the image
2. Detects faces
3. Extracts facial regions
4. Runs deep learning inference
5. Generates prediction with confidence score

---

## 🛠️ Tech Stack

### Programming & AI

* Python
* PyTorch
* NumPy
* OpenCV

### Frontend

* HTML
* CSS
* React

### Backend

* FastAPI

---

## 📂 Project Structure

```text
backend/
frontend/
model/
best_model.pth
train_resnet.py
test_model.py
evaluate_model.py
```

---

## 📊 Model Performance

Current Evaluation Results:

* Real Image Accuracy: 66%
* Deepfake Image Accuracy: 82%
* Overall Accuracy: 74%

---

## 🔬 Deep Learning Pipeline

Image Upload
↓
Face Detection
↓
Face Cropping
↓
Image Preprocessing
↓
ResNet18 Classification
↓
Prediction & Confidence Score

---

## 🎯 Future Improvements

* Video Deepfake Detection
* AI Generated Image Detection
* Larger Training Dataset
* Model Optimization
* Cloud Deployment

---

## 👨‍💻 Author

**Jeewan Sagar Singh**

Computer Vision | AIML Enthausist | Python Developer
