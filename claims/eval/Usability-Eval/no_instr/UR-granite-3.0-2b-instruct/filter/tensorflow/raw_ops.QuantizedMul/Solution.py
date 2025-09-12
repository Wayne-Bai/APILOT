import tensorflow as tf

def elementwise_multiply(x, y):
    # Check if inputs are quantized buffers
    assert tf.is_quantized(x), "Input x is not a quantized buffer"
    assert tf.is_quantized(y), "Input y is not a quantized buffer"

    # Perform element-wise multiplication
    result = tf.raw_ops.ElementwiseMultiply(inputs=[x, y], output_types=tf.float16)

    return result
