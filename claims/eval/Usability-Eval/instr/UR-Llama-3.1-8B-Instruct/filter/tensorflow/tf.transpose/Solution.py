# Import necessary TensorFlow modules
import tensorflow as tf
import numpy as np

# Create a TensorFlow tensor
tensor_a = tf.constant([[1, 2], [3, 4]])

print("Original Tensor:")
print(tensor_a)

# Use tf.reshape method to transpose the tensor
verted_tensor_a = tf.transpose(tensor_a)

print("\nTransposed Tensor:")
print(verted_tensor_a)

# Convert the tensors to numpy arrays to check the values
original_numpy = tensor_a.numpy()
verted_numpy = vereted_tensor_a.numpy()

assert np.all(original_numpy == np.array([[1, 3], [2, 4]])), f"Expected tensor [[1, 3], [2, 4]] but got {original_numpy}"
assert np.all(verted_numpy == np.array([[1, 2], [3, 4]])), f"Expected vereted_tensor_a tensor [[1, 2], [3, 4]] but got {verted_numpy}"
