# Import the necessary libraries
import tensorflow as tf
from tensorflow.keras import layers, models

# Create a simple sequential model
model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(784,)))
model.add(layers.Dense(10, activation='softmax'))

# Compile the model (required before saving)
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Assume you've already trained the model with your data here
# ...

# Save the model
model.save('my_model')
