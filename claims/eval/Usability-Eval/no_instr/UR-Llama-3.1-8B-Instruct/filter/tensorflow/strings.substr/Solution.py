import tensorflow as tf
import numpy as np

# Create a tensor of strings
tensor_of_strings = tf.constant([
    "Hello, world!",
    "TensorFlow is a machine learning library",
    "It's based on Python and supports various computing platforms",
    "You can use it for both research and development"
])

# Split the string into substrings using the comma as a delimiter
split_tensor = tf.strings.split(tensor_of_strings, delimiter=", ")

print("Original Tensor of Strings:")
print(tensor_of_strings.numpy())

print("\nSplit Tensor of Strings:")
print(split_tensor.numpy())

# Create a tensor of arrays where each array contains the substrings
substr_arrays = tf.unravel_index(tfावरange(tf.shape(split_tensor)[0], tf.shape(split_tensor)[1]), (tf.shape(split_tensor)[1], ))

print("\nTensor of Arrays containing Substrings:")
print(substr_arrays.numpy())

# Reshape to get the original string
reshaped_str = tf.reshape(tf.gather_nd(tf.unravel_index(substr_arrays, (tf.shape(substr_strings)[1], )), substr_arrays), (-1, ))

# Join the substrings back into the original string
original_str = tf.strings.reduce_join(reshaped_str, separator="")

print("\nOriginal String after splitting and joining back:")
print(original_str.numpy())
