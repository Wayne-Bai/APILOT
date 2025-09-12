import tensorflow as tf

# Define your tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Quantize the tensor
quantized_tensor = tf.quantization.quantize_and_dequantize(input_tensor)

# Dequantize the tensor
dequantized_tensor = tf.quantization.quantize_and_dequantize(quantized_tensor, -1.0, 1.0, tf.quint8, True)

print("Quantized Tensor:\n", quantized_tensor.numpy())
print("Dequantized Tensor:\n", dequantized_tensor.numpy())
