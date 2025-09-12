import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2], [3], [], [4, 5, 6]])

# Convert the RaggedTensor to a dense tensor
dense_tensor = tf.RaggedTensor.to_tensor(ragged_tensor)

print("Ragged Tensor:")
print(ragged_tensor)
print("\nDense Tensor:")
print(dense_tensor)
