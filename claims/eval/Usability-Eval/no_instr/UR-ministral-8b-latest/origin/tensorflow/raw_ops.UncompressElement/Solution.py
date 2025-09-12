import tensorflow as tf

# Define a function to uncompress tensor
def uncompress_dataset(element):
    # Assuming element is a list [compressed_data, uncompressed_shape]
    compressed_data = element[0]
    uncompressed_shape = element[1]

    # Use tf.raw_ops.RaWUncompress to uncompress the data
    uncompressed_data = tf.raw_ops.RaWUncompress(compressed_data, uncompressed_shape)
    return uncompressed_data

# Example usage
compressed_data = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int32)
uncompressed_shape = tf.constant([2, 3], dtype=tf.int32)

element = [compressed_data, uncompressed_shape]
uncompressed_data = uncompress_dataset(element)

print(uncompressed_data)
