import tensorflow as tf

# Create a simple model for demonstration
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(None, 1)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Save the model to SavedModel format
model.save('path_to_saved_model', save_format='tf')

# To load the model back
loaded_model = tf.keras.models.load_model('path_to_saved_model')

# Use the loaded model for predictions
# Example input
import numpy as np
example_input = np.array([[1], [2], [3]])
predictions = loaded_model.predict(example_input)

print(predictions)
