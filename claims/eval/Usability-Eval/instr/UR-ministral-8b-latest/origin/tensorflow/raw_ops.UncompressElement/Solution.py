import tensorflow as tf

def uncompress(data, shape):
    """
    Uncompresses a compressed dataset element using the tf.raw_ops API.

    Args:
    - data (tf.Tensor): The compressed dataset element.
    - shape (tuple): The shape of the uncompressed tensor.

    Returns:
    - tf.Tensor: The uncompressed tensor.
    """
    uncompressed = tf.raw_ops.UnpackUncompressed(data, shape=shape)
    return uncompressed

# Example usage:
compressed_data = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
uncompressed_data = uncompress(compressed_data, shape=(2, 2))

print(uncompressed_data)
