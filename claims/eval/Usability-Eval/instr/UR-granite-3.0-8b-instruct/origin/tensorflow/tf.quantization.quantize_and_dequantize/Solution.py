import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.2, 2.3, 3.4, 4.5, 5.6])

# Quantize the tensor
quantized_tensor = tf.quantization.fake_quant_with_min_max_vars(tensor, min=0.0, max=1.0, num_bits=8, narrow_range=True)

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min=0.0, max=1.0, num_bits=8, narrow_range=True)

print("Original Tensor:", tensor.numpy())
print("Quantized Tensor:", quantized_tensor.numpy())
print("Dequantized Tensor:", dequantized_tensor.numpy())
