# Import the necessary tensorflow modules
import tensorflow as tf

# Define the input tensor
tensor = tf.random.normal([3, 4, 5])

# Print the original tensor
print("Original Tensor:")
print(tensor)

# Define the min and max values for quantization
min_val = tf.reduce_min(tensor)
max_val = tf.reduce_max(tensor)

# Calculate the number of bits for quantization
num_bits = 8  # Set the number of bits to 8 for example

# Calculate the step for quantization
step = (max_val - min_val) / (2 ** num_bits - 1)

# Quantize the tensor
quantized_tensor = tf.round((tensor - min_val) / step)

# Print the quantized tensor
print("\nQuantized Tensor:")
print(quantized_tensor)

# Dequantize the tensor
dequantized_tensor = tensor.assign(tf.round(quantized_tensor * step) + min_val)

# Print the dequantized tensor
print("\nDequantized Tensor:")
print(dequantized_tensor)
