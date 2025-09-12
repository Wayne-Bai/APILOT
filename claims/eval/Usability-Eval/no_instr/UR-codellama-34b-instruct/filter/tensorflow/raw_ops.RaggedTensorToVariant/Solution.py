import tensorflow as tf

# Create a RaggedTensor with some data
rt = tf.ragged.constant([[1, 2, 3], [4, 5, 6]])

# Encode the RaggedTensor into a variant tensor
vt = tf.ragged.encode_ragged_tensor(rt)

print(vt)
