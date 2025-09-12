import tensorflow as tf

# Create a random tensor
x = tf.random.uniform(shape=[1, 2, 3, 4], minval=0, maxval=10)

# Quantize the tensor to 8 bits
x_quantized = tf.quantize_per_tensor(x, axis=None)

# Dequantize the tensor
x_dequantized = tf.dequantize(x_quantized)

print("Original tensor:")
print(x)
print("\nQuantized tensor:")
print(x_quantized)
print("\nDequantized tensor:")
print(x_dequantized)
