import tensorflow as tf
from tensorflow import checkpoints

# Define the model
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

# Create a model
model = create_model()

# Define the optimizer and loss function
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
loss = tf.keras.losses.SparseCategoricalCrossentropy()

# Checkpoints
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)

# Train the model normally
# If you define a modelize this training process.

# Define a checkpoint directory path
checkpoint_dir = './training_checkpoints'

# Define the checkpoint prefix
checkpoint_prefix = os.path.join(checkpoint_dir, 'ckpt')

# Create a checkpoint instance
checkpoint = tf.train.Checkpoint(optimizer=optimizer, global_step=tf.Variable(0, name="step", trainable=False, dtype=tf.int64))

# Save the checkpoint at certain intervals
checkpoint.save(checkpoint_save_filename)

# Later, you can load the checkpoint and continue the training process
checkpoint.restore('path_toknow whereitsave check')
