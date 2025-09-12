import tensorflow as tf

# Assume quantization 8 bits only
quantized_tensor = tf.quantize([1.0, 2.0, 3.0, 4.0])
print("Quantized Tensor: ", quantized_tensor)

# Dequantize the tensor
dequantized_tensor = tf.dequantize(quantized_tensor)
print("Dequantized Tensor: ", dequantized_tensor)
