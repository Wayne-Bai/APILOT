import tensorflow as tf

def compress_dataset_element(element, compression_rate=0.5):
    # Define a random value for compression.
    compressed_element = tf.random.normal(shape=tf.shape(element), mean=0, stddev=compression_rate * tf.reduce_max(tf.abs(element)))

    return compressed_element

# Example usage:
element = tf.constant([1.0, 2.0, 3.0, 4.0])
compressed_element = compress_dataset_element(element, compression_rate=0.2)
print("Original element:", element.numpy())
print("Compressed element:", compressed_element.numpy())
