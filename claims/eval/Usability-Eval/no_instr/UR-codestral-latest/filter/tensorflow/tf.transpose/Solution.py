import tensorflow as tf

# Assuming a is the Tensor that you want to transpose
a = tf.constant([[1, 2], [3, 4]])

# Transpose a Tensor
transposed_a = tf.transpose(a)

# Print the original and transposed Tensors
print("Original Tensor:")
print(a)
print("Transposed Tensor:")
print(transposed_a)
