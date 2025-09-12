import tensorflow as tf

# Create a sample tensor "a"
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor "a"
a_transposed = tf.transpose(a)

# To verify the result, you can print the transposed tensor
print(a_transposed)
