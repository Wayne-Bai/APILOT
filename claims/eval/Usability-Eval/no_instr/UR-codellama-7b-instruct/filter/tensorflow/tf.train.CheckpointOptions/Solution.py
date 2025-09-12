import tensorflow as tf

# Load the checkpoint
ckpt = tf.train.Checkpoint(model=your_model)
ckpt_manager = tf.train.CheckpointManager(ckpt, directory='/path/to/checkpoints', max_to_keep=5)
