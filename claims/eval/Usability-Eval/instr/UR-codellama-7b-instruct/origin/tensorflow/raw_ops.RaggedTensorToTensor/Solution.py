import tensorflow as tf

# Creating a ragged tensor
ragged_tensor = tf.RaggedTensor.from_row_lengths(values=[1, 2, 3, 4], row_lengths=[2, 1, 3])

# Using `tf.raw_ops.DenseToSparse` to convert the ragged tensor into a dense tensor with the same shape
dense_tensor = tf.raw_ops.DenseToSparse(input=ragged_tensor)
