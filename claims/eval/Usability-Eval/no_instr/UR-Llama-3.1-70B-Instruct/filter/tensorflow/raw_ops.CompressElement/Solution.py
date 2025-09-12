import tensorflow as tf

def compress_tensor(input_tensor):
    """
    This function compresses a given tensor.

    Args:
        input_tensor (Tensor): The input tensor to be compressed.

    Returns:
        bytes: The compressed tensor as a bytes object.
    """
    # Convert the input tensor to bytes
    tensor_bytes = tf.io.serialize_tensor(input_tensor)
    
    # Compress the bytes using the zlib library
    compressed_bytes = tf.io.compress(tensor_bytes, compression_type="ZLIB")

    return compressed_bytes

# Example usage
if __name__ == "__main__":
    # Create a sample tensor
    sample_tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.int32)

    # Compress the tensor
    compressed_tensor = compress_tensor(sample_tensor)

    # Print the compressed tensor
    print(compressed_tensor)
