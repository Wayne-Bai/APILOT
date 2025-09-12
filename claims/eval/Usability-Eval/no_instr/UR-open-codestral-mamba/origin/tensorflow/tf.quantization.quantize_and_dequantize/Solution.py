import tensorflow as tf

# Create a simple tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float32)

# Quantize the tensor to uint8
quantized_tensor = tf.quantization.fake_quant_with_min_max_args(tensor, 0.0, 1.0, num_bits=8)

# Dequantize the tensor back to float32
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, tensor)

print("Original Tensor:\n", tensor)
print("Quantized Tensor:\n", quantized_tensor)
print("Dequantized Tensor:\n", dequantized_tensor)
