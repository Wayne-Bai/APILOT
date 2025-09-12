import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]], dtype=tf.float32)

# Quantize the tensor
quantized_tensor = tf.quantization.quantize(tensor, 
                                              min_range=0.0, 
                                              max_range=1.0, 
                                              T=tf.qint8, 
                                              mode='SCALED')

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor[0], 
                                                 min_range=0.0, 
                                                 max_range=1.0)

print("Original Tensor:\n", tensor)
print("Quantized Tensor:\n", quantized_tensor)
print("Dequantized Tensor:\n", dequantized_tensor)
