import tensorflow as tf

# Create a sample tensor 'a'
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# Transpose the tensor 'a'
transposed_a = tf.transpose(a)

# Print the original and transposed tensors
print("Original tensor:")
print(a)
print("\nTransposed tensor:")
print(transposed_a)
