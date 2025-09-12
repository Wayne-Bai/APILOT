import tensorflow as tf

# A tensor of integers
int_tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.int32)

# Convert the tensor to strings
str_tensor = tf.as_string(int_tensor)

# Print the tensor of strings
print(str_tensor)
