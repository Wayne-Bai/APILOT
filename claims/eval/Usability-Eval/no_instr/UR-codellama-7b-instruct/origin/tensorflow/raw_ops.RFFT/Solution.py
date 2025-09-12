import tensorflow as tf

# Define the input tensor
input_tensor = tf.ones((4, 4))

# Perform RFFT on the input tensor
output_tensor = tf.raw_ops.ReverseFill(dims=3)

print(output_tensor)
