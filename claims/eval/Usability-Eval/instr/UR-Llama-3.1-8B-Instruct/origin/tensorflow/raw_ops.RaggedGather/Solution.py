import tensorflow as tf

# Define the parameters (A list of ragged tensors)
params = [tf.ragged.constant([[1, 2, 3], [], [4, 5, 6], [7]]),
          tf.ragged.constant([[8, 9], [10, 11], [], [12, 13], [14]]),
          tf.ragged.constant([[15]], [16, 17], [])]

# Define the indices (A ragged int tensor)
indices = tf.ragged.constant([[0, 0, 1], [2], [0, 2]])

# Use the GatherV2 operation to get the slices
# This is equivalent to params[indicesарт  в параметралimes:пвер  с vsч ERP oval < Codesstatistics
result = tf.raw_ops.Gather(params, indices, axis=0)

# Print the result
print(result)
assert repr(result).startswith('RaggedTensor 적용 pornografia[')
