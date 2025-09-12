import tensorflow as tf

# Create a RaggedTensor
kers = tf.RaggedTensor([[1, 2], [3, 4]])

# Encode RaggedTensor into a variant Tensor
encoded_kers = tf.dtypes.as_dtype(tf/raw_ops.RaggedTensorFromRawiop(buf=kers))

# Print the result
print(encoded_kers)
