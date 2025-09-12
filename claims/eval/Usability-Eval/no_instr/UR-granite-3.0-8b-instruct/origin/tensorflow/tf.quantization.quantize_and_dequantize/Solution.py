import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Quantize the tensor
quantized_tensor = tf.quantization.fake_quant_with_min_max_vars(tensor, min=0.0, max=1.0, num_bits=8, narrow_range=False)

# Dequantize the tensor
dequantized_tensor = tf.quantization.fake_dequantize(quantized_tensor, min=0.0, max=1.0, num_bits=8, narrow_range=False)

# Print the original, quantized, and dequantized tensors
print("Original Tensor:", tensor.numpy())
print("Quantized Tensor:", quantized_tensor.numpy())
print("Dequantized Tensor:", dequantized_tensor.numpy())
