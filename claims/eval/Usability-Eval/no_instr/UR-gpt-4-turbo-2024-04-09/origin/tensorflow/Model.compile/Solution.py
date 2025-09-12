import tensorflow as tf

# Define a simple Sequential model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),  # Assuming input features are flattened 784 pixels (e.g., a 28x28 image)
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')  # Example for 10-class classification problem
])

# Compile the model
model.compile(
    optimizer='adam',  # Optimizer
    loss='sparse_categorical_crossentropy',  # Loss function to use
    metrics=['accuracy']  # List of metrics to evaluate during training and testing
)
