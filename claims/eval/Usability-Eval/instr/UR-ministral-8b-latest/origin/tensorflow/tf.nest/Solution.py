import tensorflow as tf

# Example usage of tf._api.v2.nest namespace

# Define the input data
input_data = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)

# Define a sequence of layers
layers = [
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(1)
]

# Create a Model with the sequence of layers
model = tf.keras.Sequential(layers)

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Load the input data as batches
input_batches = tf.data.Dataset.from_tensor_slices(input_data).batch(1)

# Train the model
model.fit(input_batches, epochs=10)

# Make predictions
predictions = model(input_data)
print(predictions)
