
import tensorflow as tf

# Define the input sparse tensor and its shape
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 1], [2, 2]], values=[1, 2, 3], dense_shape=(4, 4))

# Fill the empty rows with a default value of -1
filled_sparse_tensor = tf.raw_ops.SparseFillEmptyRows(sparse_indices=sparse_tensor.indices, sparse_values=sparse_tensor.values, dense_shape=(4, 4), default_value=-1)

# Print the filled tensor
print(filled_sparse_tensor)
