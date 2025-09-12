
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.uint8)

# Dequantize the input tensor to a float or bfloat16 Tensor
dequantized_tensor = tf.raw_ops.Dequantize(input_tensor, 0, 1, dtype=tf.float16)

print(dequantized_tensor)
