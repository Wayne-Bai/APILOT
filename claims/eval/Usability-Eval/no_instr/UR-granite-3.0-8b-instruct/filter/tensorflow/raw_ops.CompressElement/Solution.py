import tensorflow as tf

# Assume 'input_tensor' is your dataset element
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Use tf.raw_ops.QuantizeV2 to compress the dataset element
quantized_tensor = tf.raw_ops.QuantizeV2(
    input_tensor,
    tf.raw_ops.QuantizationFeatures.ZERO_POINT,
    tf.raw_ops.QuantizationFeatures.SCALE,
    tf.raw_ops.QuantizationFeatures.MIN,
    tf.raw_ops.QuantizationFeatures.MAX
)

# Print the quantized tensor
print(quantized_tensor)
