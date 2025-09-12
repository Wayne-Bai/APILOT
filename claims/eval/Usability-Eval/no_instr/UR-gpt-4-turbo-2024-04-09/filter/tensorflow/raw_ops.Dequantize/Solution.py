import tensorflow as tf

def dequantize_tensor(input_tensor, min_range, max_range, mode='MIN_COMBINED', dtype=tf.float32):
    """
    Dequantize the 'input' tensor of type quint8, quint16, qint8, qint16, or qint32 into a float32 or bfloat16 Tensor.

    Parameters:
        input_tensor (tf.Tensor): Tensor to dequantize.
        min_range (float): The minimum scalar value possibly produced for the input.
        max_range (float): The maximum scalar value possibly produced for the input.
        mode (str): Dequantize mode ('MIN_COMBINED', 'MIN_FIRST', or 'SCALED').
        dtype (tf.DType): Output tensor data type (tf.float32 or tf.bfloat16).

    Returns:
        Tensor: Dequantized tensor.
    """
    return tf.quantization.dequantize(input_tensor, min_range, max_range, mode=mode, dtype=dtype)

# Example usage:
# Define a quantized tensor (for example purposes, normally this would be the output from another operation)
quant_tensor = tf.constant([0, 128, 255], dtype=tf.quint8)
min_val, max_val = 0.0, 1.0  # Corresponding to the scale of quantization

# Dequantized output
dequantized_tensor = dequantize_tensor(quant_tensor, min_val, max_val)
print(dequantized_tensor)
