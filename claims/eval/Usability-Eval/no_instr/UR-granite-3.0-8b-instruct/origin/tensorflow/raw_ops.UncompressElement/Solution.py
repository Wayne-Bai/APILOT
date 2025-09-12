import tensorflow as tf

# Assuming 'compressed_data' is your compressed dataset element
# and 'original_data' is the original dataset element

# Uncompress the compressed dataset element
uncompressed_data = tf.raw_ops.Uncompress(compressed_data)

# Print the uncompressed data
print(uncompressed_data)
