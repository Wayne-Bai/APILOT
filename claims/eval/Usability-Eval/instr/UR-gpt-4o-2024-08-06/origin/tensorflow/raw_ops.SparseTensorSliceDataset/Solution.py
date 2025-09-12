import tensorflow as tf

# Create a sample SparseTensor
sparse_indices = [[0, 0], [1, 2], [2, 3], [3, 0], [3, 1]]
sparse_values = [1, 2, 3, 4, 5]
sparse_dense_shape = [4, 4]

sparse_tensor = tf.sparse.SparseTensor(
    indices=sparse_indices,
    values=sparse_values,
    dense_shape=sparse_dense_shape
)

# Convert SparseTensor to a dataset of row-wise elements
dataset = tf.data.Dataset.from_tensor_slices(tf.sparse.to_dense(sparse_tensor))

# Iterator to inspect each element of the dataset
for element in dataset:
    print(element.numpy())
