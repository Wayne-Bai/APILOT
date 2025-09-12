
import tensorflow as tf

# Specify the directory where the checkpoint files will be saved
checkpoint_dir = '/path/to/save/checkpoint_files'

# Create a Checkpoint object
checkpoint = tf.train.Checkpoint()

# Specify objects to be saved or restored in the checkpoint
# For example, if you have a model 'my_model' to be saved in the checkpoint:
# checkpoint.my_model = my_model

# Initialize a CheckpointManager to manage checkpoints
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint_manager = tf.train.CheckpointManager(checkpoint, checkpoint_prefix, max_to_keep=5)

# Save the checkpoint
checkpoint_manager.save()

# Restore the checkpoint
status = checkpoint.restore(checkpoint_manager.latest_checkpoint)
if status:
    status.assert_existing_objects_matched()

# Access restored objects from the checkpoint
# For example, if you want to access 'my_model' after restoration:
# restored_model = checkpoint.my_model
