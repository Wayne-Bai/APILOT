
import tensorflow as tf

# Create two quantized tensors
tensor_a = tf.constant([1, 2, 3], dtype=tf.quint8)
tensor_b = tf.constant([4, 5, 6], dtype=tf.quint8)

# Perform element-wise multiplication
result = tf.quantization.multiply(tensor_a, tensor_b)

print(result)
