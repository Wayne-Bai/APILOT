import tensorflow as tf

# Define the input sparse tensor components
indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
values = tf.constant([1, 2, 3], dtype=tf.int32)
dense_shape = tf.constant([3, 4], dtype=tf.int64)

# Create the input sparse tensor
sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Define the necessary parameters for bin counting
weights = tf.constant([1.0, 1.0, 1.0], dtype=tf.float32)  # Optional: weights for values
min_val = 0
max_val = 3
nbins = 4

# Perform restricted bin counting
sparse_count = tf.raw_ops.Bincount(
    arr=values,
    size=nbins,
    weights=weights,
    binary_output=False  # Change to True if binary count is desired
)

# Create a sparse tensor for the resulting count
sparse_count_tensor = tf.SparseTensor(
    indices=tf.where(sparse_count > 0), 
    values=tf.gather_nd(sparse_count, tf.where(sparse_count > 0)),
    dense_shape=[nbins]
)

# Evaluate and print the sparse bins
print("Indices of sparse count: ", sparse_count_tensor.indices.numpy())
print("Values of sparse count: ", sparse_count_tensor.values.numpy())
