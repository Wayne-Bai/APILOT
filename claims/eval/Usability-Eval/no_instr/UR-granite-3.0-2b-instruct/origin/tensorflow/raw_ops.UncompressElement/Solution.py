import tensorflow as tf

def uncompress_dataset_element(compressed_data):
    """
    Uncompresses a compressed dataset element.

    Args:
    compressed_data (tf.Tensor): The compressed dataset element.

    Returns:
    tf.Tensor: The uncompressed dataset element.
    """
    # Check if the compressed data is a compression method supported by tf.raw_ops
    supported_compression_methods = ['LZ4', 'ZLIB', 'ZSTD', 'SNAPPY']
    if not any(method in compressed_data.dtype.as_basis_type().name for method in supported_compression_methods):
        raise ValueError("Unsupported compression method")

    # Use tf.raw_ops.Uncompress to uncompress the dataset element
    uncompressed_data = tf.raw_ops.Uncompress(compressed_data, num_shards=1, shard_index=0)

    return uncompressed_data
