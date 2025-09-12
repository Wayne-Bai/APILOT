import tensorflow as tf

def dequantize_tensor(input_tensor, mode='TFLite', dtype=tf.float32, scale=1.0, zero_point=0):
    """
    Dequantize a tensor from its quantized form.

    Args:
        input_tensor: The quantized input tensor.
        mode: The mode of dequantization, default is 'TFLite'.
        dtype: The target data type, default is tf.float32.
        scale: The scale used for dequantization.
        zero_point: The zero point for dequantization.

    Returns:
        A dequantized tensor.
    """
    if mode == 'TFLite':
        # TFLite dequantization method
        dequantized_tensor = tf.cast(input_tensor, dtype) * scale - zero_point
    else:
        raise ValueError("Unsupported dequantization mode")

    return dequantized_tensor

# Example usage:
# Assuming input_tensor is a quantized tensor
# input_tensor should be a tf.Tensor
input_tensor = tf.constant([128, 130, 132], dtype=tf.uint8)

# Defining scale and zero_point
scale = 0.1
zero_point = 128

# Dequantizing the tensor into float32
dequantized_tensor = dequantize_tensor(input_tensor, dtype=tf.float32, scale=scale, zero_point=zero_point)

print(dequantized_tensor)
