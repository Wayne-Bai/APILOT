# Importing necessary modules from tensorflow
import tensorflow as tf
import numpy as np

# Creating a sample tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Converting tensor to strings using the tf.py_function method (lower-level API)
def convert_to_string(x):
    """
    Converts the given tensor entry to a string.
    
    Args:
    x: tensorflow tensor to be converted
    
    Returns:
    A string representation of the input tensor.
    """
    return tf.convert_to_tensor(str(x))

# Using tf.map_fn to apply the function to each entry in the tensor
# map_fn expects input and map_fn to return a list of tensors with shape [dim@1].
# We use a const scalar tensor as the output to map_fn function so that it can be properly executed by tensorflow
string_tensor = tf.map_fn(lambda x: convert_to_string(x), tensor, dtype=tf.string)

# Print the resulting string tensor
with tf.Session() as sess:
    result = sess.run(string_tensor)
    print(result)
