import tensorflow as tf

# Example of creating a dense tensor from a ragged tensor

# Create a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6, 7, 8, 9]])

# Convert the ragged tensor to a dense tensor with a specified shape
# For example, let's pad the tensor to be 3x4 (if the original is not at least this size).
dense_tensor = ragged_tensor.to_tensor(default_value=0, shape=[3, 4])

print("Ragged Tensor:")
print(ragged_tensor)

print("\nDense Tensor:")
print(dense_tensor)
