import tensorflow as tf

# Create a simple Tensor of strings
str_tensor = tf.constant(['Hello', 'World', 'How', 'are', 'you'])

# Extract a substring from each element of Tensor
# Let's take starting index as 1 and length of substring as 2
substr_tensor = tf.strings.substr(str_tensor, 1, 2)

# Print the resulting Tensor
print(substr_tensor.numpy())
