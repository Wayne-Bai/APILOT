import tensorflow as tf

# Set up a SparseTensor for demonstration
indices = tf.constant([[0, 0], [1, 2], [2, 3], [3, 4]], dtype=tf.int64)
values = tf.constant([1, 2, 3, 4], dtype=tf.int32)
dense_shape = tf.constant([4, 5], dtype=tf.int64)

sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Split the SparseTensor elements row-wise into a dataset
dataset = tf.data.Dataset.from_tensor_slices(
    (tf.sparse.to_dense(sparse_tensor))
)

# Function to demonstrate the dataset output
for element in dataset:
    tf.print("Row:", element)

# Iterate over the dataset to see the individual rows
for row_tensor in dataset.batch(1):
    sparse_row = tf.sparse.from_dense(row_tensor)
    tf.print("Sparse Row Indices:", sparse_row.indices, "Values:", sparse_row.values, "Dense Shape:", sparse_row.dense_shape)
