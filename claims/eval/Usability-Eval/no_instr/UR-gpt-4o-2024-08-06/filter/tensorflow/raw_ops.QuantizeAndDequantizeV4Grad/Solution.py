import tensorflow as tf

def quantize_and_dequantize_v4_grad(x, input_min, input_max, grad_y, num_bits=8, signed_input=True, range_given=True, narrow_range=False):
    """
    This function computes the gradient of the `QuantizeAndDequantizeV4` operation
    based on the input parameters.
    
    Args:
    - x: The input tensor.
    - input_min: Minimum range value.
    - input_max: Maximum range value.
    - grad_y: The gradient of the output with respect to some loss.
    - num_bits: Number of bits to use for quantization.
    - signed_input: Whether to use signed or unsigned quantization.
    - range_given: Whether the range is specified.
    - narrow_range: Whether to use the narrow quantization range.
    
    Returns:
    - Gradient of the quantized input tensor.
    """
    # Handling input range depending on whether range is given
    if range_given:
        min_val = tf.cast(input_min, x.dtype)
        max_val = tf.cast(input_max, x.dtype)
    else:
        min_val = tf.reduce_min(x)
        max_val = tf.reduce_max(x)

    # Calculate scale factor for quantization
    if narrow_range:
        quant_min = -(1 << (num_bits - 1)) + 1 if signed_input else 0
    else:
        quant_min = -(1 << (num_bits - 1)) if signed_input else 0
    
    quant_max = (1 << (num_bits - 1)) - 1
    
    scale = (max_val - min_val) / (quant_max - quant_min)
    scale = tf.maximum(scale, 1e-6)  # avoid division by zero

    # Dequantize the quantized input
    x_dequantized = x * scale + min_val

    # Compute the gradient of dequantized output w.r.t x
    grad_input = grad_y * scale
    
    return grad_input

# Example use
x = tf.constant([0.1, -0.2, 0.3], dtype=tf.float32)
input_min = -1.0
input_max = 1.0
grad_y = tf.constant([0.01, 0.02, 0.03], dtype=tf.float32)

grad_x = quantize_and_dequantize_v4_grad(x, input_min, input_max, grad_y)
print(grad_x.numpy())
