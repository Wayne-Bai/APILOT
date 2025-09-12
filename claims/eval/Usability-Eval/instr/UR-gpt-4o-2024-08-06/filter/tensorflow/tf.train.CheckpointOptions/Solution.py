import tensorflow as tf

# Define a simple sequential model for demonstration
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(32,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(10)
])

# Let's build the model by calling it with a sample input
model(tf.random.normal([1, 32]))

# Create a checkpoint directory
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = f'{checkpoint_dir}/ckpt'

# Create a checkpoint instance
checkpoint = tf.train.Checkpoint(optimizer=tf.keras.optimizers.Adam(), model=model)

# Function to save checkpoint
def save_checkpoint():
    checkpoint.save(file_prefix=checkpoint_prefix)

# Function to restore checkpoint
def restore_checkpoint():
    latest_checkpoint = tf.train.latest_checkpoint(checkpoint_dir)
    if latest_checkpoint:
        checkpoint.restore(latest_checkpoint)
        print("Checkpoint restored from", latest_checkpoint)
    else:
        print("No checkpoint found. Starting from scratch.")

# Example usage
save_checkpoint()  # Save a checkpoint
restore_checkpoint()  # Restore from the last checkpoint
