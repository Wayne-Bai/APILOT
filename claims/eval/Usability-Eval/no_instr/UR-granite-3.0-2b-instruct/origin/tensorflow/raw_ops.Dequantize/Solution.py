import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Dequantize the input tensor into a float tensor
dequantized_float_tensor = tf.raw_ops.Dequantize(input_tensor, tf.float32)

# Dequantize the input tensor into a bfloat16 tensor
dequantized_bfloat16_tensor = tf.raw_ops.Dequantize(input_tensor, tf.bfloat16)
