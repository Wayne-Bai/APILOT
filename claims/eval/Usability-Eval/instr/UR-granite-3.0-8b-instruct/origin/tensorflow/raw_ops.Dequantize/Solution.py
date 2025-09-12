import tensorflow as tf

# Assuming 'input' is your quantized tensor
input_tensor = tf.raw_ops.Dequantize(input, min_range, max_range, output_type)
