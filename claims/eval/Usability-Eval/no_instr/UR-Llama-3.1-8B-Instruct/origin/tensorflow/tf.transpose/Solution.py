import tensorflow as tf

# Create a tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])

print("Original Tensor:")
print(a)

# Transpose the tensor
a_transposed = tf.transpose(a)

print("\nTransposed Tensor:")
print(a_transposed)
