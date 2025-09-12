import tensorflow as tf

# Define your model
class MyModel(tf.keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.dense1 = tf.keras.layers.Dense(10, activation='relu')
        self.dense2 = tf.keras.layers.Dense(1)

    def call(self, x):
        x = self.dense1(x)
        return self.dense2(x)

# Create an instance of the model
model = MyModel()

# Define the optimizer and loss
optimizer = tf.keras.optimizers.Adam()
loss_fn = tf.keras.losses.MeanSquaredError()

# Define the checkpoint directory
checkpoint_dir = './checkpoints'

# Create a checkpoint manager
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)

# Create the checkpoint manager
checkpoint_manager = tf.train.CheckpointManager(checkpoint, checkpoint_dir, max_to_keep=3)

# Train the model and save checkpoints
for epoch in range(10):
    for x, y in dataset:
        with tf.GradientTape() as tape:
            predictions = model(x)
            loss = loss_fn(y, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

        # Save the checkpoint
        checkpoint.save(file_prefix=checkpoint_prefix)

        if checkpoint_manager.should_stop():
            break
