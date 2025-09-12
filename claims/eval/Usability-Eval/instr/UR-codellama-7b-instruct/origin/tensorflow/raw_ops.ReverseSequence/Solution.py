
import tensorflow as tf

# Define the input tensor and its shape
input_tensor = tf.constant([1, 2, 3, 4, 5, 6])
shape = [tf.shape(input_tensor)[0]]

# Reverse the slice
output_tensor = tf.reverse(input_tensor, shape)

print("Output tensor:", output_tensor)
