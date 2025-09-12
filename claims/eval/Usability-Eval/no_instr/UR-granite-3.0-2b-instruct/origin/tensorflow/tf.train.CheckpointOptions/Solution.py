import tensorflow as tf

# Define a model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Save the model
model.save('my_model.h5')

# Create a checkpoint
checkpoint = tf.keras.callbacks.ModelCheckpoint('my_model.h5', save_best_only=True)

# Train the model with the checkpoint
model.fit(x_train, y_train, epochs=10, callbacks=[checkpoint])
