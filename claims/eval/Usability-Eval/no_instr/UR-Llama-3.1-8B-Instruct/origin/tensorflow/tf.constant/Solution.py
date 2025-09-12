# Import the tensorflow library
import tensorflow as tf

# Define a tensor-like object (numpy array in this case)
tensor_like_object = tf.constant([[1, 2, 3], [4, 5, 6]])

# Create a constant tensor from the tensor-like object
constant_tensor = tf.constant(tensor_like_object)

# Print the tensor-like object and the constant tensor
print("Tensor-like Object:")
print(tensor_like_object)

print("\nConstant Tensor:")
print(constant_tensor)

# Verify the constant tensor
print("\nIs the constant tensor constant?")
print(tf.is_matrix_vector_constant(constant_tensor))

# Also note that Tensorflow tensors are immutable, so they cannot be changed once they have been created.
# Changing a tensor-like object before it is converted to a constant tensor will change the constant tensor.
tensor_like_object[0, 0] = -5  # Change the tensor-like object
print("\nTensor-like Object after change:")
print(tensor_like_object)

print("\nConstant Tensor after change:")
print(constant_tensor)
