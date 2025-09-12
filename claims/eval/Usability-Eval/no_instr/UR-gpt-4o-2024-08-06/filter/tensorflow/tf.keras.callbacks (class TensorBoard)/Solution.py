import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import datetime

# Define a simple model
def create_model():
    model = keras.Sequential([
        layers.Dense(units=128, activation='relu', input_shape=(784,)),
        layers.Dense(units=64, activation='relu'),
        layers.Dense(units=10, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Load a dataset (e.g., MNIST)
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the input data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Flatten the images
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# Create a TensorBoard callback
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Create and train the model
model = create_model()
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), callbacks=[tensorboard_callback])

# To visualize the training in TensorBoard:
# Open a terminal and run the following command:
# tensorboard --logdir=logs/fit
