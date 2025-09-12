# Import required modules from tensorflow
import tensorflow as tf

# Create a custom model
class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
        self.layers = [
            tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(10)
        ]

    def call(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

# Create an instance of the custom model
model = Model()

# Create a checkpoint handler
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, 'ckpt')

# Create a checkpoint object
checkpoint = tf.train.Checkpoint(step=tf.Variable(1), model=model)

# Create a manager for restoring and saving checkpoints
manager = tf.train.CheckpointManager(checkpoint, directory=checkpoint_dir, max_to_keep=3)

# Save the model without intermediate checkpoints
def save_ckpt():
    manager.save()
    print(f"Saved checkpoint: {checkpoint_prefix}")

# Restore the model to a previous checkpoint
def restore_ckpt():
    try:
        manager.restore_or_initialize()
    except:
        print("No checkpoint to restore.")

# Save a checkpoint with intermediate checkpoints
class Checkpointer(tf.keras.callbacks.Callback):
    def __init__(self, checkpoint_dir):
        self.checkpoint_dir = checkpoint_dir

    def on_epoch_end(self, epoch, logs=None):
        step = self.model.step.assign(epoch + 1)
        manager.save(checkpoint_number=step)

    def on_train_end(self, logs=None):
        manager.save()

# Usage
save_ckpt()  # Saves the model without intermediate checkpoints
restore_ckpt()  # Restores the model to a previous checkpoint

# To save a checkpoint with intermediate checkpoints, use a Checkpointer
checkpoint_dir = './training_checkpoints'
checkpointer = Checkpointer(checkpoint_dir)
model.fit(X_train, y_train, epochs=10, callbacks=[checkpointer])
