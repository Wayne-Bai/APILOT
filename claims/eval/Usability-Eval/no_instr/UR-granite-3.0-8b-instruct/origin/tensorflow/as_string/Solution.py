import tensorflow as tf

# Assuming 'input_tensor' is your input tensor
input_tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings
output_tensor = tf.strings.as_string(input_tensor)

# Print the output tensor
print(output_tensor)
