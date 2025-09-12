import tensorflow as tf

# Assuming 'a' is a tensor
a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Transpose tensor 'a'
transpose_a = tf.transpose(a)

print("Original tensor:")
print(a.numpy())
print("\nTranspose of the tensor:")
print(transpose_a.numpy())
