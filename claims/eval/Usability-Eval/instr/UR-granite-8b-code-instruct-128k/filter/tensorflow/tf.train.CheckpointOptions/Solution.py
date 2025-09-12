import tensorflow as tf

# Create a checkpoint
checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)

# Save the checkpoint
checkpoint.save(checkpoint_path)

# Restore the checkpoint
checkpoint.restore(checkpoint_path).assert_consumed()
