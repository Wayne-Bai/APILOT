# Import necessary libraries
import tensorflow as tf

# Create a new TensorBoard callback
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='./logs')

# Create a sample model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with TensorBoard callback
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'],
              callbacks=[tensorboard_callback])

# Train the model with sample data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 784)
x_train = x_train / 255.0
model.fit(x_train, y_train, epochs=5)

# Visualize TensorBoard
# Open terminal, navigate to the logs directory and run the following command:
# tensorboard --logdir./logs
# Open a browser and navigate to http://localhost:6006 to see the visualizations.
