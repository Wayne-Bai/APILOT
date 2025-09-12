import tensorflow as tf

# Create a constant tensor
# We can use tf.constant() to create a Tensor from a tensor-like object.
# For example, we can create a tensor from a list, a numpy array, or a scalar.

# Create a tensor from a list
list_constant = tf.constant([[1, 2, 3], [4, 5, 6]])
print("Tensor created from list:")
print(list_constant)

# Create a tensor from a scalar
scalar_constant = tf.constant(1.234)
print("\nTensor created from scalar:")
print(scalar_constant)
