import tensorflow as tf

def compress_dataset_element(dataset_element):
    """Compresses a dataset element using tf.raw_ops.EncodeProto."""
    serialized_tensor = tf.raw_ops.EncodeProto(sizes=[1], values=[dataset_element])
    return serialized_tensor

# Example usage:
element = tf.constant([1, 2, 3])
compressed_element = compress_dataset_element(element)
print(compressed_element)
