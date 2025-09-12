import tensorflow as tf

def dequantize_tensor(input_tensor, min_range, max_range, mode='MIN_COMBINED', dtype=tf.float32):
    """
    Dequantize the 'input_tensor' into a float or bfloat16 Tensor.

    Parameters:
        input_tensor (tf.Tensor): A tensor of type quint8, qint8, quint16, qint16, quint32, qint32.
        min_range (float): The minimum scalar value possibly produced for the input.
        max_range (float): The maximum scalar value possibly produced for the input.
        mode (str): A string indicating the quantization mode. (Default 'MIN_COMBINED')
                   Supported modes: 'MIN_COMBINED', 'MIN_FIRST', 'SCALED'
        dtype (tf.DType): The type of the output (tf.float32 or tf.bfloat16). (Default tf.float32)

    Returns:
        tf.Tensor: A tensor of type float32 or bfloat16.
    """
    return tf.raw_ops.Dequantize(
        input=input_tensor, 
        min_range=min_range, 
        max_range=max_range, 
        mode=mode, 
        dtype=dtype
    )

# Example usage:
# Create a quantized tensor (simulating a quantized tensor input)
q_tensor = tf.constant([0, 128, 255], dtype=tf.uint8)
min_val, max_val = 0.0, 1.0

# Dequantize the tensor
dequantized_tensor = dequantize_tensor(q_tensor, min_val, max_val)

print(dequantized_tensor)
