import tensorflow as tf
from tensorflow.keras import layers

# Define the model architecture
model = tf.keras.Sequential([
    # Input layer
    layers.Dense(64, activation='relu', input_shape=(784,)),
    # Hidden layer
    layers.Dense(64, activation='relu'),
    # Output layer
    layers.Dense(10)
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
