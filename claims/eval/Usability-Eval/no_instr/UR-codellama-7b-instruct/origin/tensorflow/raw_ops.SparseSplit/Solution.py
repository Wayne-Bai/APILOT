
import tensorflow as tf

# Load a sparse tensor from a file
sparse_tensor = tf.io.SparseTensor(filename="path/to/sparse/tensor")

# Split the sparse tensor into num_split tensors along one dimension
num_splits = 2
split_tensors = tf.raw_ops.SplitV(indices=sparse_tensor.indices, values=sparse_tensor.values, dense_shape=sparse_tensor.dense_shape, num_split=num_splits, dim=1)

# Print the split tensors
print("Split tensors:", split_tensors)
