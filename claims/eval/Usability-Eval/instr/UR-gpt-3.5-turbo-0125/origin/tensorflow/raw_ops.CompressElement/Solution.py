
import tensorflow as tf

def compress_dataset_element(dataset_element, compression_type):
    compressed_element = tf.raw_ops.EncodeProto(serialized=dataset_element, compression_type=compression_type)
    return compressed_element

# Example usage
dataset_element = tf.io.serialize_tensor(tf.constant([1, 2, 3]))
compression_type = "ZLIB"
compressed_element = compress_dataset_element(dataset_element, compression_type)
print(compressed_element)
