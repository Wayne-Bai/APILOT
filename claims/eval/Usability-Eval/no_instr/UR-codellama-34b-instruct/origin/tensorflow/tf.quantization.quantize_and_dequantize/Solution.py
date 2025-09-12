import tensorflow as tf

# Define a tensor to be quantized and dequantized
tensor = tf.constant([[1, 2], [3, 4]])

# Quantize the tensor
quantized_tensor = tf.quantization.fake_quant_with_min_max_args(
    tensor, min=0.0, max=6.0)

# Dequantize the quantized tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor)

print("Original tensor:", tensor.numpy())
print("Quantized tensor:", quantized_tensor.numpy())
print("Dequantized tensor:", dequantized_tensor.numpy())
