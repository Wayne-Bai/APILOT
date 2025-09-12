
import tensorflow as tf

def compress_dataset_element(dataset_element, compression_type):
    compressed_element = tf.raw_ops.Method(input=dataset_element, method="Compress", compression_type=compression_type)
    return compressed_element

# Example usage
dataset_element = tf.constant("This is a sample dataset element.")
compressed_element = compress_dataset_element(dataset_element, "gzip")
print(compressed_element)
