import tensorflow as tf

# Define a tensor
tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Quantize the tensor
quantized_tensor = tf.raw_ops.Quantize(input=tensor, num_bits=8)

# Dequantize the tensor
dequantized_tensor = tf.raw_ops.Dequantize(input=quantized_tensor, num_bits=8)

# Print the original, quantized, and dequantized tensors
print("Original Tensor: ", tensor.numpy())
print("Quantized Tensor: ", quantized_tensor.numpy())
print("Dequantized Tensor: ", dequantized_tensor.numpy())
