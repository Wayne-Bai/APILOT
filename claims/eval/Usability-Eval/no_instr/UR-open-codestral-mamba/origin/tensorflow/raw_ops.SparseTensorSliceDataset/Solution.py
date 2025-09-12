import tensorflow as tf

# Create a SparseTensor
indices = tf.constant([[0, 0], [1, 1], [2, 2]])
values = tf.constant([1, 2, 3])
shape = tf.constant([3, 3])
sparse_tensor = tf.sparse.SparseTensor(indices, values, shape)

# Split the SparseTensor row-wise
row_splits = tf.constant([0, 1, 2, 3])
dataset = tf.data.Dataset.from_tensor_slices(tf.sparse.split(sparse_tensor, row_splits, tf.halt_if_error))

# Iterate over the dataset
for element in dataset:
    print(element)
