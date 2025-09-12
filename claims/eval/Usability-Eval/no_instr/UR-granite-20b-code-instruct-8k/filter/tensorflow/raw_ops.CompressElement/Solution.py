import tensorflow as tf

# Define your dataset element
dataset_element = ...

# Compress the dataset element
compressed_element = tf.raw_ops.compress(input=dataset_element, axis=-1, bits=8)

# Print the compressed element
print(compressed_element)
