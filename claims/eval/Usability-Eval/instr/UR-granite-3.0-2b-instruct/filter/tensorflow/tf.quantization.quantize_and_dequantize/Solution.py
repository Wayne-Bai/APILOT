import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Quantize the tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(tensor)

# Print the original and quantized tensors
print("Original Tensor:")
print(tensor)
print("\nQuantized Tensor:")
print(quantized_tensor)
