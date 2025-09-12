import tensorflow as tf

def compute_gradient(quantize_and_dequantize_op):
    return tf.raw_ops.Gradient(
        var_handle1=quantize_and_dequantize_op,
    )

# Example usage:
quantize_and_dequantize_op = tf.raw_ops.QuantizeAndDequantizeV4(...)
gradient = compute_gradient(quantize_and_dequantize_op)
