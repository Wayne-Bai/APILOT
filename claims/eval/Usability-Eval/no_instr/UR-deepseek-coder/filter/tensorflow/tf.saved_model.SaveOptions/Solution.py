import tensorflow as tf

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save the model to SavedModel format
model.save('path_to_saved_model')

# Load the model from SavedModel format
loaded_model = tf.keras.models.load_model('path_to_saved_model')

# Verify the loaded model
print(loaded_model.summary())
