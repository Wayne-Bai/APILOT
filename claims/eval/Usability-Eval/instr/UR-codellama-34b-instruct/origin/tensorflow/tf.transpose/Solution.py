import tensorflow as tf

# Generate a random tensor for testing
a = tf.random.normal((3, 4))

# Transpose the tensor using the transpose() function from TensorFlow
transposed_a = tf.transpose(a)

print("Original tensor:")
print(a)
print("\nTransposed tensor:")
print(transposed_a)
