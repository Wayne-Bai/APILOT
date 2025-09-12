
import tensorflow as tf

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model (dummy data used for illustration purposes)
dummy_x = tf.random.normal(shape=(100, 784))
dummy_y = tf.random.uniform(shape=(100,), maxval=10, dtype=tf.int32)
model.fit(dummy_x, dummy_y, epochs=5)

# Save the model to SavedModel format
model.save("saved_model_path")

print("Model saved to SavedModel format.")
