import tensorflow as tf

# Generate a tensor with random values
x = tf.constant([[1.2, 2.3, 3.4], [4.5, 5.6, 6.7]], dtype=tf.float32)

# Quantize the tensor
q_x = tf.quantize_and_dequantize(x, 0.0, 10.0)

print("Original tensor:", x)
print("Quantized and Dequantized tensor:", q_x)
