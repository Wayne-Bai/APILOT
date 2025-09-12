import tensorflow as tf

def decompress_element(compressed_element):
    # Uncompress a compressed dataset element using the `UncompressElement` raw operation from TensorFlow
    uncompressed_element = tf.raw_ops.UncompressElement(bytes=compressed_element)
    return uncompressed_element
