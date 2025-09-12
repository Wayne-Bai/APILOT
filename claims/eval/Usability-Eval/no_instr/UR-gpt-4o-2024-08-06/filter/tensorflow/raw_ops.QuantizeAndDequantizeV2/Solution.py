import tensorflow as tf

# Define a tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0], dtype=tf.float32)

# Quantization parameters
min_value = tf.reduce_min(input_tensor)
max_value = tf.reduce_max(input_tensor)
num_bits = 8

# Scale and zero point for quantization
scale = (max_value - min_value) / (2**num_bits - 1)
zero_point = -min_value / scale

# Quantize the tensor
quantized_tensor = tf.round(input_tensor / scale + zero_point)
quantized_tensor = tf.clip_by_value(quantized_tensor, 0, 2**num_bits - 1)

# Dequantize the tensor
dequantized_tensor = (quantized_tensor - zero_point) * scale

# Print results
print("Original Tensor:", input_tensor.numpy())
print("Quantized Tensor:", quantized_tensor.numpy())
print("Dequantized Tensor:", dequantized_tensor.numpy())
