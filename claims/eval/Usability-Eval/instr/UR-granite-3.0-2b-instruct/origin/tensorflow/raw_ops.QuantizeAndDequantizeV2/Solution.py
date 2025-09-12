import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)

# Quantize the tensor
quantized_tensor = tf.raw_ops.Quantize(input=tensor, num_bits=8, dtype=tf.qint8)

# Dequantize the tensor
dequantized_tensor = tf.raw_ops.Dequantize(input=quantized_tensor, num_bits=8, dtype=tf.float32)

# Print the original, quantized, and dequantized tensors
print("Original Tensor:")
print(tensor.numpy())
print("\nQuantized Tensor:")
print(quantized_tensor.numpy())
print("\nDequantized Tensor:")
print(dequantized_tensor.numpy())
