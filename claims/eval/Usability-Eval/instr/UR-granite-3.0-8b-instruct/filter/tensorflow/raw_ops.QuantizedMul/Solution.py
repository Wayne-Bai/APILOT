import tensorflow as tf

# Define the quantized buffers
x_quantized = tf.quantization.QuantizeV2(x, min_range, max_range, tf.int8, tf.float32)
y_quantized = tf.quantization.QuantizeV2(y, min_range, max_range, tf.int8, tf.float32)

# Perform element-wise multiplication
result = tf.raw_ops.QuantizedMul(x_quantized, y_quantized)
