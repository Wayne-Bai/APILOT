import tensorflow as tf

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Save the model to the SavedModel format
model.save('saved_model/my_model')

# To load the model later, you can use:
loaded_model = tf.keras.models.load_model('saved_model/my_model')

# Verify that the loaded model has the same architecture
loaded_model.summary()
