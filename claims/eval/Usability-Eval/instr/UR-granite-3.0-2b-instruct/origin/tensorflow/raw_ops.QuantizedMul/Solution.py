import tensorflow as tf

# Define the input tensors
x = tf.constant([1.0, 2.0, 3.0], dtype=tf.float16)
y = tf.constant([4.0, 5.0, 6.0], dtype=tf.float16)

# Create a quantized buffer for x
x_quantized = tf.raw_ops.QMul(x, x, dtype=tf.float16)

# Create a quantized buffer for y
y_quantized = tf.raw_ops.QMul(y, y, dtype=tf.float16)

# Perform element-wise multiplication of the quantized buffers
result = tf.raw_ops.QMul(x_quantized, y_quantized, dtype=tf.float16)

# Print the result
print(result.numpy())
