import tensorflow as tf

# Assume we have a sparse tensor
indices = tf.constant([[0, 0], [1, 2]])
values = tf.constant([1, 2])
shape = tf.constant([2, 3])
sparse_tensor = tf.SparseTensor(indices, values, shape)

# We can convert to dense tensor first
sparse_tensor_to_dense = tf.sparse.to_dense(sparse_tensor)

# Now, we create a dataset from the dense tensor
dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor_to_dense)
