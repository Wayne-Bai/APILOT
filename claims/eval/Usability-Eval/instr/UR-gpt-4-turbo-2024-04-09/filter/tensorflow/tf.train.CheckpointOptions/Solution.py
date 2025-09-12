import tensorflow as tf

# Instantiate a simple model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(32,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Define the optimizer, loss function, and metrics
optimizer = tf.keras.optimizers.Adam()
model.compile(optimizer=optimizer, loss='mse', metrics=['accuracy'])

# Prepare to save weights using a Checkpoint
checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)

# Set the checkpoint file path
checkpoint_directory = "/path/to/save/"
checkpoint_prefix = checkpoint_directory + "ckpt"

# Save the checkpoint
checkpoint.save(file_prefix=checkpoint_prefix)
