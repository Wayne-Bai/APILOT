import tensorflow as tf

def uncompress_element(compressed_element, compression_type):
    """
    Uncompresses a compressed dataset element.

    Args:
    - compressed_element: A scalar string tensor containing the compressed element.
    - compression_type: A scalar string tensor specifying the compression algorithm.

    Returns:
    - Uncompressed element.
    """

    # Check if compression type is valid
    valid_compression_types = ['NONE', 'GZIP', 'ZLIB', 'SNAPPY']
    if compression_type not in valid_compression_types:
        raise ValueError(f"Invalid compression type. Supported types are: {valid_compression_types}")

    # Use tf.io.decode_compressed to uncompress the element
    # Then return the uncompressed element
    uncompressed_element = tf.io.decode_compressed(compressed_element, compression_type=compression_type)

    return uncompressed_element

# Test the function
compressed_element = tf.io.encode_gzip(tf.constant("Hello World!"))
compression_type = 'GZIP'
uncompressed = uncompress_element(compressed_element, compression_type)

print(uncompressed)
