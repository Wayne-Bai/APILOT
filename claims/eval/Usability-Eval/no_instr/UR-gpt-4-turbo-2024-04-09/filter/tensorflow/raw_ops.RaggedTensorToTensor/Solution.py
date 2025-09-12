import tensorflow as tf

# Create a RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4], [], [5, 6]])

# Convert the RaggedTensor to a dense tensor
dense_tensor = ragged_tensor.to_tensor()

print("Dense Tensor:")
print(dense_tensor)
