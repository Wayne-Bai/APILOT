import tensorflow as tf

# Define our model
class MyModel(tf.keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.dense_layer = tf.keras.layers.Dense(10, activation='relu')

    def call(self, inputs):
        return self.dense_layer(inputs)

# Instantiate the model
model = MyModel()

# Define the checkpoint for the model
checkpoint_path = "model_{epoch:04d}.ckpt".format(
    epoch=0
)  # Model will be saved after every 100 training steps

manager = tf.train.Checkpoint(
    model=model,
    optimizer=None  # Optimizer will be defined separately
)

# Create a checkpoint saver
ckpt_saver = tf.train.CheckpointManager(
    manager, directory='model_checkpoints', max_to_keep=3
)
