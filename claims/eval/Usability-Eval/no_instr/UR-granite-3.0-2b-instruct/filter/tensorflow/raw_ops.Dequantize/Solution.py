import tensorflow as tf

# Assuming 'input' is your tensor
input_tensor = tf.constant([1.0, 2.0, 3.0])

# Dequantize the tensor into a float tensor
dequantized_float_tensor = tf.raw_ops.Dequantize(input=input_tensor, output_type=tf.float32)

# Dequantize the tensor into a bfloat16 tensor
dequantized_bfloat16_tensor = tf.raw_ops.Dequantize(input=input_tensor, output_type=tf.bfloat16)
