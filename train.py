import tensorflow as tf
import os

# Paths

TRAIN_DIR = "data/train"
VAL_DIR = "data/val"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "helmet_model.h5")

# Create model directory if not exists

os.makedirs(MODEL_DIR, exist_ok=True)

# Load dataset

train_data = tf.keras.preprocessing.image_dataset_from_directory(
TRAIN_DIR,
image_size=(224, 224),
batch_size=32
)

val_data = tf.keras.preprocessing.image_dataset_from_directory(
VAL_DIR,
image_size=(224, 224),
batch_size=32
)

# Normalize data

normalization_layer = tf.keras.layers.Rescaling(1./255)
train_data = train_data.map(lambda x, y: (normalization_layer(x), y))
val_data = val_data.map(lambda x, y: (normalization_layer(x), y))

# Build CNN model

model = tf.keras.Sequential([
tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
tf.keras.layers.MaxPooling2D(),

```
tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
tf.keras.layers.MaxPooling2D(),

tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
tf.keras.layers.MaxPooling2D(),

tf.keras.layers.Flatten(),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dense(2, activation='softmax')
```

])

# Compile model

model.compile(
optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy']
)

# Train model

history = model.fit(
train_data,
validation_data=val_data,
epochs=10
)

# Save model

model.save(MODEL_PATH)

print(f"Model saved at {MODEL_PATH}")
