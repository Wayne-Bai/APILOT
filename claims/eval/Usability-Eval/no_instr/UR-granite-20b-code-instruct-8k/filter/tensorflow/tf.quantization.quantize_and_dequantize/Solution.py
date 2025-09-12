import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.float32)

# Define the scale and zero point for quantization
scale = tf.constant(0.01, dtype=tf.float32)
zero_point = tf.constant(10, dtype=tf.int32)

# Quantize the input tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(input_tensor, scale, zero_point, tf.quanteforge.LSTM)

# Dequantize the quantized tensor
dequantized_tensor = tf.quantization.quantize_and_dequantize(quantized_tensor, scale, zero_point, tf.quanteforge.LSTM, True)

# Print the original and dequantized tensors
print("Original Tensor:")
print(input_tensor)
print("Dequantized Tensor:")
print(dequantized_tensor)
