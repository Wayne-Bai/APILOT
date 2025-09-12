import tensorflow as tf

# Define a tensor
input_tensor = tf.constant([1.5, 2.6, 3.7], dtype=tf.float32)

# Quantize the tensor with 8 bits
quantized_tensor = tf.quantization.quantize(input_tensor, tf.float32_ref.min, tf.float32_ref.max, tf.uint8.min, tf.uint8.max)

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, tf.float32_ref.min, tf.float32_ref.max, tf.uint8.min, tf.uint8.max)

# Print the results
print("Original Tensor: ", input_tensor.numpy())
print("Quantized Tensor: ", quantized_tensor.numpy())
print("Dequantized Tensor: ", dequantized_tensor.numpy())
