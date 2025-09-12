# Import the necessary modules
import tensorflow as tf
import numpy as np

# Create a random input tensor
# We assume 'input' is a uint8 tensor for demonstration purposes
input_tensor = tf.random.uniform(shape=(5,5), minval=0, maxval=256, dtype=tf.uint8)

# Dequantize the tensor
dequantized_tensor = tf.raw_ops.Dequantize(input=input_tensor, axis=-1, min=0, max=255)

# You can also use the tf.cast method as an alternative to dequantize
# dequantized_tensor = tf.cast(input_tensor, dtype=tf.float32)

# Print the shape and data type of dequantized tensor
print("Shape of dequantized tensor:", dequantized_tensor.shape)
print("Data type of dequantized tensor:", dequantized_tensor.dtype)

# Test it with an example (for 'input' tensor)
input_tensor_eg = tf.constant([[[101, 102, 103], [104, 105, 106], [107, 108, 109]],
                               [[110, 111, 112], [113, 114, 115], [116, 117, 118]],
                               [[119, 120, 121], [122, 123, 124], [125, 126, 127]]])

dequantized_tensor_eg = tf.raw_ops.Dequantize(input=input_tensor_eg, axis=-1, min=0, max=255)

print("Example Dequantized tensor:")
print(dequantized_tensor_eg)
