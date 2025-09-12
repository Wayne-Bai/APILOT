import tensorflow as tf

# Assuming you have a compressed dataset element
compressed_element = tf.constant([254, 255, 60, 75], dtype=tf.int8)  # Compressed byte sequence

# Reshape the compressed element to a 1D tensor
compressed_element = tf.reshape(compressed_element, shape=[-1])

# Define a function to uncompress a single byte element
def _uncompress_byte(compressed_byte):
    # If the byte is 0xFF, it represents an uncompressed byte
    if compressed_byte == 255:
        return compressed_byte
    # If the byte is less than 0xFF, it represents a byte that has been delta-encoded
    else:
        return compressed_byte - 1

# Apply the _uncompress_byte function to each byte in the compressed element
uncompressed_elements = tf.map_fn(lambda x: _uncompress_byte(x), compressed_element, dtype=tf.int8)

# Convert the uncompressed elements back to a TensorFlow compatible data type
uncompressed_elements = tf.cast(uncompressed_elements, dtype=tf.uint8)

# Predict and return the uncompressed element
uncompressed_element = tf.reduce_min(uncompressed_elements)

# Print the uncompressed element
print(uncompressed_element)

# Reshape and print the original 2D Output from uncompressed elements
compressed_element = tf.reshape(uncompressed_elements, shape=[4])
print(compressed_element)
