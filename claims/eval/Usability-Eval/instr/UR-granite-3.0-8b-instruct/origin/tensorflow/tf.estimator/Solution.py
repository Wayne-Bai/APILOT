import tensorflow as tf

# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Assume that you have a dataset loaded into `train_images` and `train_labels`
# model.fit(train_images, train_labels, epochs=5)

# Evaluate the model
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# Make predictions
# predictions = model.predict(test_images)

# Export the model
# model.save('my_model.h5')
