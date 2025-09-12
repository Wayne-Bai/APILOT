import tensorflow as tf

# Define a function to uncompress a compressed dataset element
def uncompress_element(compressed_element):
    # Use tf.raw_ops.DecodeBase64 to decode the compressed element
    decoded_element = tf.raw_ops.DecodeBase64(input=compressed_element)

    # Use tf.io.decode_zlib to uncompress the decoded element
    uncompressed_element = tf.io.decode_zlib(decoded_element)

    return uncompressed_element
