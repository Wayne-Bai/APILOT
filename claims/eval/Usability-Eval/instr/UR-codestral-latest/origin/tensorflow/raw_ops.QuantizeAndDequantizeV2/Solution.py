import tensorflow as tf

# Let's create a random tensor for this example
input_tensor = tf.random.normal([10, 10])

# Quantize the tensor
quantized_tensor = tf.quantization.quantize(
    input_tensor, min_range=-1.0, max_range=1.0, T=tf.int16, mode='SCALED'
)

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min_range=-1.0, max_range=1.0, mode='SCALED')

# Print the original and dequantized tensors
print("Original tensor:\n", input_tensor)
print("Dequantized tensor:\n", dequantized_tensor)
