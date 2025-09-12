
import tensorflow as tf

# Define input and bias tensors
input = tf.constant([[1, 2], [3, 4]], dtype=tf.quint8)
bias = tf.constant([1, 2], dtype=tf.quint8)

# Add bias to input using TensorFlow's add function
result = tf.add(input, bias)

print(result.numpy())
