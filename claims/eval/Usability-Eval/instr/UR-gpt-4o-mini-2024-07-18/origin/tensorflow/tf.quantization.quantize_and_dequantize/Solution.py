import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)

# Quantize the tensor
quantized_tensor = tf.quantization.fake_quant_with_min_max_args(tensor, min=0.0, max=4.0)

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min=0.0, max=4.0)

# Print the results
print("Original Tensor:\n", tensor.numpy())
print("Quantized Tensor:\n", quantized_tensor.numpy())
print("Dequantized Tensor:\n", dequantized_tensor.numpy())
