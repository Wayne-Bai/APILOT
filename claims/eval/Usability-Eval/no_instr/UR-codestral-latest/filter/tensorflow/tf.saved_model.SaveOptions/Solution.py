import tensorflow as tf
from tensorflow.keras import layers

# Define the model
model = tf.keras.Sequential()
model.add(layers.Dense(32, activation='relu', input_dim=100))
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Save the model
tf.keras.models.save_model(
    model,
    "my_model",
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)
