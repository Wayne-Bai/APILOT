import tensorflow as tf

# Create a RaggedTensor
data = [[1, 2], [3, 4, 5], [6, 7]]
ragged_tensor = tf.ragged.constant(data)

# Dense Tensor from a Ragged Tensor
dense_tensor = tf.RaggedTensorToTensor()(ragged_tensor)

print(ragged_tensor)
print(dense_tensor)
