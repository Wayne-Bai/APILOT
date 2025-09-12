import tensorflow as tf

def quantize_and_dequantize_v4_gradient(input_tensor, scale, zero_point, quant_min, quant_max, axis):
    """
    Computes the gradient for QuantizeAndDequantizeV4 operation.

    Args:
    - input_tensor: The input tensor for which the gradient will be computed.
    - scale: The scale tensor for quantization.
    - zero_point: The zero point tensor for quantization.
    - quant_min: Minimum quantization value.
    - quant_max: Maximum quantization value.
    - axis: The dimension to reduce for per-axis quantization.

    Returns:
    - The gradient tensor of the input.
    """

    # Compute the quantized values
    quantized = tf.clip_by_value(tf.round(input_tensor / scale) + zero_point, quant_min, quant_max)

    # Compute the dequantized values
    dequantized = (quantized - zero_point) * scale

    # Gradient is the difference of output and input with respect to input_tensor
    gradient = tf.gradients(dequantized, [input_tensor])[0]
    
    return gradient

# Example usage
if __name__ == "__main__":
    input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
    scale = tf.constant(0.1, dtype=tf.float32)
    zero_point = tf.constant(0, dtype=tf.int32)
    quant_min = tf.constant(-128, dtype=tf.int32)
    quant_max = tf.constant(127, dtype=tf.int32)
    axis = None

    gradient_result = quantize_and_dequantize_v4_gradient(input_tensor, scale, zero_point, quant_min, quant_max, axis)

    print("Gradient of QuantizeAndDequantizeV4 operation:", gradient_result.numpy())
