import tensorflow as tf

def dequantize_tensor(input_tensor, min_range, max_range, dtype=tf.float32):
    """
    Dequantize the 'input' tensor into a float or bfloat16 Tensor.
    
    Args:
        input_tensor (tf.Tensor): Input tensor to be dequantized.
        min_range (float): Minimum value of the range.
        max_range (float): Maximum value of the range.
        dtype (tf.dtypes.DType, optional): Output data type. Defaults to tf.float32.

    Returns:
        tf.Tensor: Dequantized tensor.
    """
    # Calculate the scale and offset for dequantization
    scale = (max_range - min_range) / (tf.reduce_max(input_tensor) - tf.reduce_min(input_tensor))
    offset = tf.cast(min_range, dtype) - tf.cast(tf.reduce_min(input_tensor), dtype) * scale
    
    # Apply the scale and offset to the input tensor
    dequantized_tensor = tf.cast(input_tensor, dtype) * scale + offset
    
    return dequantized_tensor

# Example usage:
input_tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.uint8)
min_range = 0.0
max_range = 1.0

dequantized_tensor = dequantize_tensor(input_tensor, min_range, max_range)
print(dequantized_tensor)
