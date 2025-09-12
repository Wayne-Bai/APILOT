import tensorflow as tf

def quantize_and_dequantize(input_tensor):
    """
    This function takes a tensor as input, quantizes it and then dequantizes it.

    Args:
        input_tensor (tf.Tensor): The input tensor to be processed.

    Returns:
        tf.Tensor: The dequantized tensor.
    """

    # Define the min and max values for quantization
    min_range = tf.reduce_min(input_tensor)
    max_range = tf.reduce_max(input_tensor)

    # Quantize the tensor
    quantized_tensor = tf.cast(tf.round((input_tensor - min_range) / (max_range - min_range) * 255), tf.uint8)

    # Dequantize the tensor
    dequantized_tensor = (tf.cast(quantized_tensor, tf.float32) / 255) * (max_range - min_range) + min_range

    return dequantized_tensor

# Create a sample tensor
tensor = tf.random.uniform(shape=(3, 3), minval=0, maxval=100, dtype=tf.float32)

# Call the function
result = quantize_and_dequantize(tensor)

# Print the result
print(result)
