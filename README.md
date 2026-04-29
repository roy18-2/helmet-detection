# 🪖 Helmet Detection System using CNN

## 📌 Overview

Road safety is a major global concern, with many accidents leading to severe head injuries due to the non-use of helmets. Manual monitoring of helmet compliance is inefficient, especially in high-traffic areas.

This project presents an automated **Helmet Detection System** using a **Convolutional Neural Network (CNN)** to classify whether a person is wearing a helmet or not from images.

---

## 🎯 Problem Statement

To develop an automated system that detects helmet usage from images, reducing the need for manual monitoring and improving road safety enforcement.

---

## 💡 Proposed Solution

A deep learning-based image classification model is trained using a CNN architecture to distinguish between:

* ✅ Helmet
* ❌ No Helmet

The system processes input images, performs preprocessing, and predicts helmet compliance.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Frameworks/Libraries:** TensorFlow, OpenCV, NumPy, Matplotlib
* **Platform:** Jupyter Notebook / Local Machine

---

## 📂 Dataset

This project uses the Helmet Detection dataset available on Kaggle:

👉 https://www.kaggle.com/datasets/andrewmvd/helmet-detection

Download the dataset and organize it as follows:

```
data/
 ├── train/
 │   ├── helmet/
 │   └── no_helmet/
 │
 └── val/
     ├── helmet/
     └── no_helmet/
```

---

## 🧠 Model Architecture

The CNN model consists of:

* Convolutional layers for feature extraction
* MaxPooling layers for dimensionality reduction
* Fully connected (Dense) layers for classification
* Softmax activation for final prediction

---

## 📊 Results

The model is evaluated using:

* Accuracy
* Loss
* (Optional) Confusion Matrix

Sample outputs are available in the `/results` folder.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/your-username/helmet-detection.git
cd helmet-detection
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Download Dataset

Download from:
https://www.kaggle.com/datasets/andrewmvd/helmet-detection

Place it inside the `data/` directory as shown above.

---

### 4. Train the Model

```
python train.py
```

This will generate:

```
models/helmet_model.h5
```

---

### 5. Run Prediction

Place a test image in the root directory and run:

```
python predict.py
```

Output:

* `Helmet ✅`
* `No Helmet ❌`

---

## 📁 Project Structure

```
helmet-detection/
│
├── train.py
├── predict.py
├── requirements.txt
├── README.md
│
├── data/
├── models/
├── results/
```

---

## ⚠️ Notes

* Ensure dataset folder names match exactly (`helmet`, `no_helmet`)
* Input image size must be **224x224**
* If class labels are reversed, update prediction logic accordingly

---

## 🔮 Future Improvements

* Real-time helmet detection using video streams
* Integration with CCTV systems
* Object detection models (e.g., YOLO) for better accuracy
* Deployment as a web or mobile application

---

## 👤 Author

Developed as part of a mini project on CNN-based object detection.

---

## ⭐ Acknowledgements

* Kaggle dataset contributors
* TensorFlow and OpenCV communities

---
