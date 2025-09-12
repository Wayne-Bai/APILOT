import tensorflow as tf

# Example inputs: params is the source, indices specifies which slices to gather.
params = tf.ragged.constant([[1, 2, 3], [4], [5, 6]])
indices = tf.constant([2, 0])

# Using tf.gather with a RaggedTensor
result = tf.gather(params, indices)

print("Gathered ragged slices:", result)
