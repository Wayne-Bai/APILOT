# Import required libraries
import tensorflow as tf

# Define a simple model
class SimpleModel(tf.Module):
    def __init__(self):
        self.variable_1 = tf.Variable(0.0)
        self.variable_2 = tf.Variable(0.0)

    def add_variables(self, delta):
        self.variable_1.assign_add(delta)
        self.variable_2.assign_add(delta)

# Create a checkpoint
class Checkpoint(tf.Module):
    def __init__(self, model):
        self.model = model

    def save(self, checkpoint_path):
        checkpoint = tf.train.Checkpoint(model=self.model)
        checkpoint.save(checkpoint_path)

    def restore(self, checkpoint_path):
        checkpoint = tf.train.Checkpoint(model=self.model)
        checkpoint.restore(checkpoint_path).assert_consumed()

# Create a model and checkpoint
model = SimpleModel()
checkpoint = Checkpoint(model)

# Save the checkpoint
checkpoint.save("./checkpoint")

# Modify the variables and save the checkpoint again
model.add_variables(5.0)
checkpoint.save("./checkpoint")

# Attempt to restore the model from the first checkpoint
print("Restore checkpoint")
checkpoint.restore("./checkpoint-1")

# Print the values of the variables after restoring the checkpoint
print("Values after restore:", model.variable_1.numpy(), model.variable_2.numpy())
