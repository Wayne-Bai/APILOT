import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1.8, 2.1, 3.0], [4.2, 5.9, 6.3]], dtype=tf.float32)

# Define the quantization settings
min_val = tf.reduce_min(tensor)
max_val = tf.reduce_max(tensor)

# Quantize the tensor
quantized_tensor = tf.quantization.fake_quant_with_min_max_args(tensor, min_val, max_val)
print("Quantized Tensor: ", quantized_tensor)

# Dequantize the tensor
dequantized_tensor = quantized_tensor * (max_val - min_val) / 255.0 + min_val
print("Dequantized Tensor: ", dequantized_tensor)
