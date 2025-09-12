import tensorflow as tf

# Example of creating a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])

# Convert the ragged tensor to a dense tensor
dense_tensor = ragged_tensor.to_tensor()

print("Ragged Tensor:")
print(ragged_tensor)
print("\nDense Tensor:")
print(dense_tensor)
