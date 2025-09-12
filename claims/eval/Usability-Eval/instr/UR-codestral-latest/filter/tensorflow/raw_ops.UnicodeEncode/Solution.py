import tensorflow as tf

# Define a tensor of integers
int_tensor = tf.constant([1, 2, 3, 4, 5])

# Encode the tensor of integers into unicode strings
str_tensor = tf.strings.as_string(int_tensor)

# Print the result
print(str_tensor)
