
import tensorflow as tf

# Define inputs
x = tf.constant([1, 2, 3], dtype=tf.int8)
y = tf.constant([4, 5, 6], dtype=tf.int8)

# Perform element-wise multiplication on quantized buffers
result = tf.raw_ops.QuantizedMul(a=x, b=y)

print(result)
