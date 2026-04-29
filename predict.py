import tensorflow as tf
import cv2
import numpy as np
import os

MODEL_PATH = "models/helmet_model.h5"

# Create results folder if not exists

os.makedirs("results", exist_ok=True)

# Load model

model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(image_path, output_name):
# Read image
img = cv2.imread(image_path)
if img is None:
print(f"Error loading image: {image_path}")
return

```
img_resized = cv2.resize(img, (224, 224))

# Normalize
img_input = img_resized / 255.0
img_input = np.expand_dims(img_input, axis=0)

# Predict
prediction = model.predict(img_input)
class_index = np.argmax(prediction)
confidence = np.max(prediction)

label = "Helmet" if class_index == 0 else "No Helmet"

print(f"{image_path} → {label} ({confidence*100:.2f}%)")

# Draw label on original image
cv2.putText(img, f"{label} ({confidence*100:.1f}%)",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 0), 2)

# Save result image
output_path = os.path.join("results", output_name)
cv2.imwrite(output_path, img)

print(f"Saved: {output_path}")
```

# 🔹 Test images (change these)

predict_image("test1.jpg", "output1.jpg")
predict_image("test2.jpg", "output2.jpg")
