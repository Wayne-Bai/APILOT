import tensorflow as tf

# Assuming 'compressed_data' is your compressed dataset element
# Replace 'compressed_data' with your actual compressed data
compressed_data = ...

# Uncompress the dataset element
uncompressed_data = tf.raw_ops.Decompress(compressed_data, tf.string)

# Print the uncompressed data
print(uncompressed_data)
