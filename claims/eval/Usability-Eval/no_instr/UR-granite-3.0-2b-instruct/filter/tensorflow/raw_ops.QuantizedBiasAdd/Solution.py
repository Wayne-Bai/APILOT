import tensorflow as tf

# Define the input and bias tensors
input_tensor = tf.constant([1.0, 2.0, 3.0])
bias_tensor = tf.constant([4.0, 5.0, 6.0])

# Create a Quantized type tensor
quantized_input_tensor = tf.quantization.quantize_and_dequantize(input_tensor)

# Add the bias tensor to the quantized input tensor
result_tensor = tf.add(quantized_input_tensor, bias_tensor)

# Print the result tensor
print(result_tensor)
