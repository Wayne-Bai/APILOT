import tensorflow as tf

# Configure the model for training
model = tf.keras.models.Sequential([
    # Input layer
    tf.keras.layers.Dense(units=64, activation='relu', input_shape=(784,)),
    # Hidden layer 1
    tf.keras.layers.Dense(units=32, activation='relu'),
    # Hidden layer 2
    tf.keras.layers.Dense(units=16, activation='relu'),
    # Output layer
    tf.keras.layers.Dense(units=10)
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
