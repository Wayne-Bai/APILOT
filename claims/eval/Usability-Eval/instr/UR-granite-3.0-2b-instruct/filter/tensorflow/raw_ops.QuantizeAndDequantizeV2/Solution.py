import tensorflow as tf

# Create a tensor
tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0], dtype=tf.float32)

# Quantize the tensor
quantized_tensor = tf.raw_ops.Quantize(input=tensor, quant_type=tf.quint8, num_bits=8)

# Dequantize the tensor
dequantized_tensor = tf.raw_ops.Dequantize(input=quantized_tensor, dequant_type=tf.float32)

# Print the original, quantized, and dequantized tensors
print("Original tensor:")
print(tensor.numpy())
print("\nQuantized tensor:")
print(quantized_tensor.numpy())
print("\nDequantized tensor:")
print(dequantized_tensor.numpy())
