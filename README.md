
# 🪖 Helmet Detection System using CNN

## 📌 Overview

This project focuses on building an automated **Helmet Detection System** using **Convolutional Neural Networks (CNNs)**. The goal is to identify whether a person is wearing a helmet or not, which helps improve road safety enforcement through automation.

Manual monitoring of helmet compliance is inefficient in high-traffic areas. This system leverages deep learning to detect helmets in images and can be extended to real-time surveillance applications.

---

## 🚀 Features

* Detects helmets in images
* Classifies objects as:

  * With Helmet
  * Without Helmet
* Uses deep learning (CNN-based object detection)
* Provides performance evaluation metrics
* Scalable for real-time applications

---

## 📂 Dataset

The dataset used for this project is sourced from Kaggle:

🔗 https://www.kaggle.com/datasets/andrewmvd/helmet-detection

### Dataset Details:

* Contains annotated images of people with and without helmets
* Includes bounding box labels for object detection
* Suitable for training CNN-based detection models

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Libraries & Frameworks:**

  * TensorFlow / PyTorch
  * OpenCV
  * NumPy
  * Matplotlib
* **Platform:** Jupyter Notebook / Google Colab

---

## 🧠 Model Architecture

* Convolutional Neural Network (CNN)
* Layers include:

  * Convolutional Layers
  * Pooling Layers
  * Fully Connected Layers
* Can be extended to object detection models like:

  * SSD (Single Shot Detector)
  * YOLO (You Only Look Once)

---

## ⚙️ Workflow

1. Data Collection (Kaggle dataset)
2. Data Preprocessing

   * Image resizing
   * Annotation parsing
3. Model Training
4. Model Evaluation
5. Prediction & Output Visualization

---

## 📊 Performance Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Intersection over Union (IoU)

---

## 📸 Output

* Detects helmets in input images
* Draws bounding boxes around detected objects
* Labels objects as "Helmet" or "No Helmet"

---

## ▶️ How to Run

1. Clone the repository
2. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```
3. Download dataset from Kaggle and place it in the project folder
4. Run the Jupyter Notebook:

   ```bash
   jupyter notebook
   ```
5. Execute all cells

---

## 🔮 Future Improvements

* Real-time detection using CCTV/video streams
* Integration with traffic monitoring systems
* Improve accuracy using advanced models like YOLOv8
* Deploy as a web or mobile application

---

## 📄 Conclusion

This project demonstrates how deep learning can be applied to enhance road safety by automating helmet detection. It reduces manual effort and increases enforcement efficiency.

---

## 👤 Author

* Riya
* Tanishqa

---
