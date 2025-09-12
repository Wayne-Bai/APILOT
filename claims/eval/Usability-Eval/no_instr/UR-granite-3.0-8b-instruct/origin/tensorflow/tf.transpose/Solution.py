import tensorflow as tf

# Assuming 'a' is a Tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor 'a'
transposed_a = tf.transpose(a)

print("Original Tensor 'a':\n", a)
print("Transposed Tensor 'a':\n", transposed_a)
