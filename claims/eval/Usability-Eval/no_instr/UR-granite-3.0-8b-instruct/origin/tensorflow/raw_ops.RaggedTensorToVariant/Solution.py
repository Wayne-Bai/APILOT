import tensorflow as tf

# Assuming 'rt' is your RaggedTensor
rt = tf.RaggedTensor.from_row_lengths([1, 2, 3], [[0], [1, 2], [3]])

# Encode the RaggedTensor into a variant Tensor
encoded_rt = tf.raw_ops.EncodeRaggedTensor(rt)

print(encoded_rt)
