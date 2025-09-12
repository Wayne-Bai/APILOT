
import tensorflow as tf

# Define the dataset element
dataset_element = tf.constant([5, 6, 7, 8])

# Define the compression options
compression_type = "GZIP"

# Define the compression options as a string
compression_options = f'{{"compression_type":"{compression_type}"}}'

# Compress the dataset element
compressed_dataset_element = tf.raw_ops.DatasetCompress(input_dataset_element=dataset_element, compression_type=compression_type, compression_options=compression_options)

print(compressed_dataset_element)
