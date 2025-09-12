import tensorflow as tf

# Define a float tensor
float_tensor = tf.constant([0.1, 0.2, 0.3, 0.4], dtype=tf.float32)

# Define the quantization parameters
min_val = tf.reduce_min(float_tensor)
max_val = tf.reduce_max(float_tensor)

# Quantize the tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(float_tensor, min_val, max_val, num_bits=8, narrow_range=True)

# Dequantize the tensor
dequantized_tensor = tf.quantization.quantize_and_dequantize(quantized_tensor, min_val, max_val, num_bits=8, narrow_range=True, signed=False)
