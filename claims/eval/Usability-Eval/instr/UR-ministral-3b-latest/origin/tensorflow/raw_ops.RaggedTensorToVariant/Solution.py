import tensorflow as tf

# Assuming you have a RaggedTensor `ragged_tensor`
ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

# Convert the RaggedTensor into a Tensor
variant_tensor = tf.ragged.vector_softmax(ragged_tensor)
print(variant_tensor)
