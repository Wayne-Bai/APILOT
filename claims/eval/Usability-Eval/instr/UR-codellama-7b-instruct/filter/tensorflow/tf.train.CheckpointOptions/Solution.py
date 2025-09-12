
import tensorflow as tf

# Create a variable
v = tf.Variable(10)

# Initialize the checkpoint
ckpt = tf.train.Checkpoint()

# Add the variable to the checkpoint
ckpt.variable_manager().register_variable("my_variable", v)

# Save the checkpoint
ckpt.save("my_checkpoint")
