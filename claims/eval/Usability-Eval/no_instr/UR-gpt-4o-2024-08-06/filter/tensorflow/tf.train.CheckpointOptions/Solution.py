import tensorflow as tf

# Define a simple model
class SimpleModel(tf.keras.Model):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.dense_layer = tf.keras.layers.Dense(1)

    def call(self, inputs):
        return self.dense_layer(inputs)

# Instantiate the model
model = SimpleModel()

# Define a checkpoint object to manage saving and restoring
checkpoint = tf.train.Checkpoint(model=model)

# Directory where the checkpoints will be saved
checkpoint_dir = './checkpoints'
checkpoint_prefix = f"{checkpoint_dir}/ckpt"

# Create a checkpoint manager
checkpoint_manager = tf.train.CheckpointManager(checkpoint, checkpoint_dir, max_to_keep=3)

# Example function to save checkpoints
def save_checkpoint():
    # Save the model weights to a checkpoint
    save_path = checkpoint_manager.save()
    print(f"Checkpoint saved at: {save_path}")

# Example function to restore checkpoints
def restore_checkpoint():
    # Restore the model weights from the latest checkpoint, if available
    if checkpoint_manager.latest_checkpoint:
        checkpoint.restore(checkpoint_manager.latest_checkpoint)
        print(f"Checkpoint restored from: {checkpoint_manager.latest_checkpoint}")
    else:
        print("No checkpoint found. Starting from scratch.")

# Example usage
# Assume we have some toy data
inputs = tf.constant([[1.0], [2.0], [3.0]])
outputs = model(inputs)

# Save a checkpoint
save_checkpoint()

# Restore from the latest checkpoint
restore_checkpoint()
