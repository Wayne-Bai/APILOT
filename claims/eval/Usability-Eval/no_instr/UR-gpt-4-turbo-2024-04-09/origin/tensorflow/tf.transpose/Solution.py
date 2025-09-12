import tensorflow as tf

# Create a Tensor 'a'
a = tf.constant([[1, 2], [3, 4]])

# Transpose the Tensor 'a'
transposed_a = tf.transpose(a)

print("Original Tensor:")
print(a)

print("Transposed Tensor:")
print(transposed_a)
