import tensorflow as tf

# Define the SparseTensor to be sliced
sparse_tensor = tf.sparse.from_dense([[1, 0, 0], [0, 2, 0], [0, 0, 3]])

# Define the row_split tensor
row_split = tf.constant([0, 1, 2, 3], dtype=tf.int64)

# Create the dataset using the SparseTensorSliceDataset method
dataset = tf.raw_ops.SparseTensorSliceDataset(sparse_tensor=sparse_tensor, row_split=row_split)

# Iterate over the elements of the dataset
for element in dataset:
    print(element)
