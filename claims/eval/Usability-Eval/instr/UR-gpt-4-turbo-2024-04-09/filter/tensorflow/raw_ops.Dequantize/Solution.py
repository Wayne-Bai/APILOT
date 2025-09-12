import tensorflow as tf

def dequantize_tensor(input_tensor, min_range, max_range, mode='MIN_COMBINED', dtype=tf.float32):
    """
    Replace the deprecated tf.raw_ops.Dequantize operation with the modern equivalent
    using `tf.quantization.dequantize`.

    Args:
    input_tensor: A quantized TensorFlow Tensor to be dequantized.
    min_range: The minimum scalar value possibly produced for the input tensor.
    max_range: The maximum scalar value possibly produced for the input tensor.
    mode: A string specifying the quantization mode, default is 'MIN_COMBINED'.
    dtype: The type of the output tensor, tf.float32 by default.

    Returns:
    A tensor of type `dtype` which has been dequantized.
    """
    return tf.quantization.dequantize(input_tensor, min_range, max_range, mode=mode, dtype=dtype)

# Example usage:
# Create a fake quantized tensor
quantized_tensor = tf.constant([0, 128, 255], dtype=tf.uint8)
min_val, max_val = 0.0, 1.0  # Example range values for quantization

# Dequantize the tensor
dequantized_tensor = dequantize_tensor(quantized_tensor, min_val, max_val)
print(dequantized_tensor)
