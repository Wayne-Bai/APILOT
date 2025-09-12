# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import os

# Create a simple model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(784,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Create some dummy data to demonstrate model saving
x_train = np.random.rand(100, 784)
y_train = np.random.randint(10, size=100)

# Train the model for one epoch to demonstrate saving
model.fit(x_train, y_train, epochs=1)

# Options for saving to SavedModel
# Save the entire model to SavedModel format
model.save('saved_model', save_format='tf')

# Load the entire model from SavedModel
loaded_model = keras.models.load_model('saved_model')

# Evaluate loaded model
loaded_model.evaluate(x_train, y_train)

# Remove saved model directory
import shutil
shutil.rmtree('saved_model')

# Save only the model's weights
model.save_weights('model_weights')

# Load model's weights
model.load_weights('model_weights')

# Remove saved weights file
os.remove('model_weights')

# Save model to HDF5 format
model.save('model_h5.h5')

# Load model from HDF5 format
loaded_model = keras.models.load_model('model_h5.h5')

# Remove saved model file
os.remove('model_h5.h5')
