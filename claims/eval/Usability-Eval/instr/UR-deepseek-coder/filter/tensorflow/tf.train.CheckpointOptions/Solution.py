import tensorflow as tf

# Define a model or optimizer
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1)
])

# Define a Checkpoint
checkpoint = tf.train.Checkpoint(model=model)

# Save the checkpoint
checkpoint.save('/path/to/save/checkpoint')

# Restore the checkpoint
checkpoint.restore('/path/to/save/checkpoint')
