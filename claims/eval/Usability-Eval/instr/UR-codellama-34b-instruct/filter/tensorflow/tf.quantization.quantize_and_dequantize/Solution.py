
import tensorflow as tf

# Define a tensor to be quantized
x = tf.constant([1, 2, 3, 4], dtype=tf.float32)

# Quantize the tensor using a 8-bit signed integer format
quantized_x = tf.quantize(x, tf.Qint8)

# Dequantize the quantized tensor to get the original values back
dequantized_x = tf.dequantize(quantized_x, x.dtype)

print(dequantized_x)  # [1., 2., 3., 4.]
