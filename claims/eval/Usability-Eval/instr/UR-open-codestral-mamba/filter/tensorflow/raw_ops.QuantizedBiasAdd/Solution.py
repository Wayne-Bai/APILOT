import tensorflow as tf

# Assuming input and bias are tensors of the correct shape
@tf.register_op("AddBiasQuantized", Tinputs=[tf.qint8, tf.int32], Toutput=tf.qint8)
def _add_bias_quantized(input, bias):
    """Custom op to add bias to quantized input tensor."""
    return tf.raw_ops.AddBiasQuantized(input=input, bias=bias)

# Usage example:
input_data = tf.constant([1, 2, 3, 4, 5], dtype=tf.qint8)  # Quantized input
bias_data = tf.constant([2, 4, 6, 8, 10], dtype=tf.int32)  # Int32 bias

result = _add_bias_quantized(input_data, bias_data)
print(result)
