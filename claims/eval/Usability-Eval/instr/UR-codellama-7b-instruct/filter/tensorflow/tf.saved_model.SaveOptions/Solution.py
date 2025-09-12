import tensorflow as tf
from tensorflow import keras

# Define model architecture
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    keras.layers.Dense(10, activation='softmax')
])

# Compile the model with a loss function and an optimizer
model.compile(loss='categorical_crossentropy', optimizer=keras.optimizers.Adam(lr=0.001), metrics=['accuracy'])

# Load the saved weights into the model
model.load_weights('./weights.h5')

# Save the model and its configuration to a SavedModel directory
tf.keras.experimental.export_saved_model(
    model,
    './saved_model',
    as_text=False,
    include_optimizer=True
)
