import tensorflow as tf

# Assuming 'params' is a RaggedTensor and 'indices' is a tensor containing indices to gather
params = tf.ragged.constant([[1, 2, 3], [4], [5, 6]])
indices = tf.constant([2, 0])

# Use tf.gather to gather slices from a RaggedTensor along axis 0 according to 'indices'
result = tf.gather(params, indices)

print(result)
