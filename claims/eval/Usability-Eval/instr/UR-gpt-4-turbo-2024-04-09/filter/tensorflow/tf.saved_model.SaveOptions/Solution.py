import tensorflow as tf

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model on dummy data
import numpy as np
x_train = np.random.random((100, 10))
y_train = np.random.random((100, 1))
model.fit(x_train, y_train, epochs=5)

# Save the entire model as a SavedModel
model.save('saved_model/my_model')
