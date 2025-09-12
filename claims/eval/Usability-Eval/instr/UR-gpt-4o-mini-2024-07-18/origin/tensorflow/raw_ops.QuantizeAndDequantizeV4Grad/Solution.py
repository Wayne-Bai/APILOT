import tensorflow as tf

@tf.function
def quantize_and_dequantize_gradient(grad, inputs, min_range, max_range):
    # Scale and translate the inputs based on the given range
    scale = (max_range - min_range) / 255.0
    zero_point = min_range

    # Compute the quantized values
    quantized = tf.round((inputs - zero_point) / scale)

    # Clamp the quantized values to be within the range [0, 255]
    quantized = tf.clip_by_value(quantized, 0, 255)

    # Dequantize back to original range
    dequantized = quantized * scale + zero_point

    # Compute the gradient for quantization
    gradient = grad * tf.where(inputs > min_range, 1.0, 0.0)

    return gradient, dequantized
