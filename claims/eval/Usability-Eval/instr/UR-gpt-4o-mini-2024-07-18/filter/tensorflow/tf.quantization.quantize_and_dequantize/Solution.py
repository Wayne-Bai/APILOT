import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([[0.1, 0.5, 0.9], [1.5, 1.0, 0.0]], dtype=tf.float32)

# Quantize the tensor
quantized_tensor = tf.quantization.quantize(tensor, 
                                              min_level=0, 
                                              max_level=255, 
                                              T=tf.uint8)

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor[0], 
                                                  min_level=0.0, 
                                                  max_level=1.0)

print("Original Tensor:")
print(tensor)

print("Quantized Tensor:")
print(quantized_tensor[0])

print("Dequantized Tensor:")
print(dequantized_tensor)
