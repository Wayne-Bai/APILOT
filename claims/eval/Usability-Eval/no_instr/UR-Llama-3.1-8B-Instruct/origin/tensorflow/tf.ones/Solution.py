# Import the tensorflow library
import tensorflow as tf

# Create a tensor with all elements set to one (1)
new_tensor = tf.ones([5, 5])

# Print the new tensor
print(new_tensor)

# Alternatively, you can create a tensor of arbitrary shape and size
tensor_shape = [10, 20]
tensor = tf.ones(tensor_shape)

# Print the shaped tensor
print(tensor)
