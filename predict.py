import tensorflow as tf
import cv2
import numpy as np

MODEL_PATH = "models/helmet_model.h5"

# Load trained model

model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(image_path):
# Read image
img = cv2.imread(image_path)
img = cv2.resize(img, (224, 224))

```
# Normalize
img = img / 255.0

# Expand dimensions
img = np.expand_dims(img, axis=0)

# Predict
prediction = model.predict(img)
class_index = np.argmax(prediction)

if class_index == 0:
    print("Helmet ✅")
else:
    print("No Helmet ❌")
```

# Change this path to your test image

predict_image("test.jpg")
