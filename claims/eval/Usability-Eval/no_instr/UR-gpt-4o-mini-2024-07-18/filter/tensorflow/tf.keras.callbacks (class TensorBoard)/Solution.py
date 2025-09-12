import tensorflow as tf
from tensorflow import keras
import datetime

# Create a callback for TensorBoard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Example model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Training the model and enabling TensorBoard
# Replace `x_train`, `y_train`, `epochs` with your training data and desired epochs
model.fit(x_train, y_train, epochs=epochs, callbacks=[tensorboard_callback])
