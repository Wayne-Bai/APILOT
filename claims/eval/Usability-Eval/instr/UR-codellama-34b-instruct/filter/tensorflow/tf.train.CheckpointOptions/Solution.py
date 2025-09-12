
import tensorflow as tf

# Create a model to save
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model on some data
model.fit(x_train, y_train, epochs=10)

# Create a checkpoint manager to save the model
checkpoint = tf.train.Checkpoint(model=model)

# Save the checkpoint
checkpoint.save('/path/to/model.h5')
