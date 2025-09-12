import tensorflow as tf

# Create a sample SparseTensor
raw_sparse_tensor = tf.SparseTensor(
    indices=[[0, 0], [1, 1], [2, 2]],
    values=[1.0, 2.0, 3.0],
    dense_shape=[3, 3]
)

# Define the number of splits
num_split = 2

# Split the SparseTensor
split_sparse_tensors = tf.raw_ops.SparseTensorToAttentionSnapshot(
    sparse_values=raw_sparse_tensor,
    sparse_indices=raw_sparse_tensor.indices,
    num_splits=num_split,
    global_batch_size=1,
    split_vectors=tf.convert_to_tensor(2, dtype=tf.int32)
)
