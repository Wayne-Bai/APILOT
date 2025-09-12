import tensorflow as tf

# Define a simple model
class SimpleModel(tf.Module):
    def __init__(self):
        # Initialize some variables
        self.w = tf.Variable(tf.random.normal([3, 2]), name='weight')
        self.b = tf.Variable(tf.zeros([2]), name='bias')

    def __call__(self, x):
        return tf.matmul(x, self.w) + self.b

# Create an instance of the model
model = SimpleModel()

# Define a checkpoint that includes the model
checkpoint = tf.train.Checkpoint(model=model)

# Define a checkpoint manager, which will manage saving the model
checkpoint_manager = tf.train.CheckpointManager(checkpoint, directory='./checkpoints', max_to_keep=3)

# Later you can use checkpoint.restore() to restore the model's state
# For example, to restore the latest checkpoint do:
# checkpoint.restore(checkpoint_manager.latest_checkpoint)
