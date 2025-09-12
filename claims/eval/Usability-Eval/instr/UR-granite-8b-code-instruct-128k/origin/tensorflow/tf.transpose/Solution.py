import tensorflow as tf

# Define the input tensor a
a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Use the tf.transpose() function to transpose a
transposed_a = tf.transpose(a)

# Print the transposed tensor
print(transposed_a)
