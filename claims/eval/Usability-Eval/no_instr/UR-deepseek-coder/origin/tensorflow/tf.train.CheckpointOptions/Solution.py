import tensorflow as tf

# Define a model or optimizer for which you want to create a checkpoint
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model (optional, but recommended)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Create a Checkpoint object
checkpoint = tf.train.Checkpoint(model=model)

# Save the checkpoint to a file
checkpoint.save('/path/to/checkpoint/directory/checkpoint')

# To restore the model from a checkpoint
# checkpoint.restore('/path/to/checkpoint/directory/checkpoint-1')
