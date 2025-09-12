import tensorflow as tf

# Activating raw ops
tf.raw_ops = tf.raw_ops.RawOps({'op_type_names': tf.raw_ops.OpTypeNames})

# Assuming you have a sparse tensor
sparse_input = tf.SparseTensor(
    indices=[[0, 1, 2], [2, 2, 2]], # Row, Col, Row, Col, ..., Row, Col
    values=[10, 20, 30],             # Value at (0, 1), (2, 2), (2, 3)
    dense_shape=[3, 3]               # Dense shape [rows, cols]
)

# Reshaping the sparse tensor
# Explanation of the operation:
# - dense_shape: The new dense shape of the output tensor
# - After reshaping: [
#   (0, 0), (0, 1), (0, 2),
#   (1, 0), (1, 1), (1, 2),
#   (2, 0), (2, 1), (2, 2)
# ] as the new indices, with no change in values

new_dense_shape = [6, 3]  # New dense shape
reshaped_sparse_tensor = tf.raw_ops.SparseReshape(
    input=tf.convert_to_tensor(sparse_input),
    dense_shape=new_dense_shape,
    validate_shape=True
)

# Printing out the reshaped sparse tensor
print(reshaped_sparse_tensor)
