
import tensorflow as tf

# Define input tensor
input_tensor = tf.constant([-0.5, 0.5], dtype=tf.bfloat16)

# Dequantize the input tensor into a float or bfloat16 Tensor
output_tensor = tf.raw_ops.Dequantize(input=input_tensor, out_type='float')
