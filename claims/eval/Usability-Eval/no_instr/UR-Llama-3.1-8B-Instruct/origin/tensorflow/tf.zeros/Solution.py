# Import the tensorflow library
import tensorflow as tf

# Create a tensor with all elements set to zero
zero_tensor = tf.zeros((3, 4))

# Print the tensor
print(zero_tensor)

# Create a tensor with a specified value
value = 5
tensor = tf.ones((2, 2)) * value

# Print the tensor
print(tensor)
