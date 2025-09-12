import tensorflow as tf

# Define a function to dequantize a tensor
def dequantize_input(input_tensor, min_range, max_range, dtype=tf.float32):
    """
    Dequantize the input tensor to a float or bfloat16 tensor.
    
    Parameters:
    - input_tensor: The quantized tensor to dequantize.
    - min_range: The minimum scalar value possibly produced for the input.
    - max_range: The maximum scalar value possibly produced for the input.
    - dtype: The type to dequantize the input into, either tf.float32 or tf.bfloat16.
    
    Returns:
    A dequantized tensor of type `dtype`.
    """
    # Use tf.quantization.dequantize to dequantize the tensor
    dequantized_tensor = tf.quantization.dequantize(
        input_tensor,
        min_range=min_range,
        max_range=max_range,
        mode='SCALED',
        dtype=dtype
    )
    
    return dequantized_tensor

# Example usage
# Define a quantized input tensor (e.g., simulated with appropriate dtype and range)
quantized_input = tf.constant([0, 64, 127, 255], dtype=tf.qint8)
min_range = 0.0
max_range = 1.0

# Dequantize the input tensor
output_tensor = dequantize_input(quantized_input, min_range, max_range)

# Verify the result
print("Dequantized Tensor:")
print(output_tensor)
