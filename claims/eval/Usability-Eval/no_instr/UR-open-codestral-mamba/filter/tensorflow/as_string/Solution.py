import tensorflow as tf

# Assume the input tensor
input_tensor = tf.constant([10, 20, 30, 40, 50])

# Convert the input tensor to string
output_tensor = tf.as_string(input_tensor)

# Print the output tensor
print(output_tensor.numpy())
