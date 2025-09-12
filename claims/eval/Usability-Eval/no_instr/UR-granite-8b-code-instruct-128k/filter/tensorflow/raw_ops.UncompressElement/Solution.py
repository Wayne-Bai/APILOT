import tensorflow as tf

# Import the necessary module
from tensorflow.python.ops import gen_dataset_ops

# Define the input tensor
input = tf.constant([1, 2, 3, 4, 5])

# Define the compression type
compression_type = tf.constant("GZIP")

# Use the tf.raw_ops.Uncompress method to uncompress the input tensor
output = gen_dataset_ops.uncompress(input, compression_type)

# Print the output tensor
print(output)
