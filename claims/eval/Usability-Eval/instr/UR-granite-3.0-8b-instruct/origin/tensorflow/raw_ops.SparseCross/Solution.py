import tensorflow as tf

# Assuming you have a list of sparse and dense tensors
sparse_tensors = [tf.SparseTensor(indices, values, dense_shape)]
dense_tensors = [tf.constant(values)]

# Convert the list of sparse and dense tensors to a single sparse tensor
sparse_cross = tf.raw_ops.SparseCross(sparse_tensors, dense_tensors)

# Print the sparse tensor
print(sparse_cross)
