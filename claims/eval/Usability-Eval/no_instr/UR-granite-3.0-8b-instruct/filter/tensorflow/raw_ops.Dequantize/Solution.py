import tensorflow as tf

# Assuming 'input' is a quantized tensor
input_tensor = tf.raw_ops.Dequantize(input, min_range, max_range, out_type=tf.float32)
