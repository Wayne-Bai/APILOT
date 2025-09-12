import tensorflow as tf

input_tensor = tf.raw_ops.Dequantize('input')
output_tensor = tf.raw_ops.Remapping(input_tensor, dtype=tf.float32)
