import tensorflow as tf

def dequantize_tensor(input_tensor, min_range, max_range, mode="MIN_COMBINED", dtype=tf.float32):
    """
    Dequantizes the 'input' tensor into a float or bfloat16 Tensor.

    Args:
        input_tensor: The input tensor to be dequantized.
        min_range: The minimum scalar value possibly produced for the input.
        max_range: The maximum scalar value possibly produced for the input.
        mode: String to determine the dequantization mode (default is "MIN_COMBINED").
        dtype: The dtype of the output tensor (default is tf.float32).

    Returns:
        A Tensor of type dtype.
    """
    # Ensure the input tensor is quantized
    input_tensor = tf.convert_to_tensor(input_tensor)
    
    # Calculate the scale and zero point
    if mode == "MIN_COMBINED":
        scale = (max_range - min_range) / (tf.reduce_max(input_tensor) - tf.reduce_min(input_tensor))
        zero_point = min_range - tf.reduce_min(input_tensor) * scale
    else:
        raise ValueError("Unsupported dequantization mode: {}".format(mode))
    
    # Dequantize the tensor
    dequantized_tensor = (input_tensor * scale) + zero_point
    
    # Cast to the desired dtype
    dequantized_tensor = tf.cast(dequantized_tensor, dtype)
    
    return dequantized_tensor

# Example usage:
# input_tensor = tf.constant([0, 127, 255], dtype=tf.uint8)
# min_range = 0.0
# max_range = 255.0
# dequantized_output = dequantize_tensor(input_tensor, min_range, max_range)
# print(dequantized_output)
