
import tensorflow as tf

# Define dataset element
dataset_element = tf.constant([1, 2, 3, 4, 5])

# Compress the dataset element
compressed_element = tf.raw_ops.Method(element=dataset_element)

# Print the compressed element
print(compressed_element)
