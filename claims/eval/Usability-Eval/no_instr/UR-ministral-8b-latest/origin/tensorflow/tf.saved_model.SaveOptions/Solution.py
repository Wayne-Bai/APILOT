import tensorflow as tf
from tensorflow.keras import layers

# Define a simple model
model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Save the model to a SavedModel format
model.save('my_model')

print("Model saved to 'my_model' directory.")
