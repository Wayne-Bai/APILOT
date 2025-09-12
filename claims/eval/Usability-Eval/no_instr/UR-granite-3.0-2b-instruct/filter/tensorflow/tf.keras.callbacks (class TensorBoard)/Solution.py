# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a simple model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Generate some dummy data
x_train = np.random.rand(60000, 784)
y_train = np.random.randint(0, 10, 60000)

# Train the model
model.fit(x_train, y_train, epochs=5)

# Enable visualizations for TensorBoard
tf.summary.create_file_writer('logs').set_as_default()

# Write summaries to TensorBoard
with tf.summary.create_file_writer('logs'):
    tf.summary.scalar('loss', model.loss, step=0)
    tf.summary.scalar('accuracy', model.metrics[0], step=0)
