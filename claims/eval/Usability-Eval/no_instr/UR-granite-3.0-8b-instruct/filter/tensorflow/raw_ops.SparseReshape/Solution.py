import tensorflow as tf

# Assuming `sparse_tensor` is your input SparseTensor
# And `dense_shape` is a list or tuple representing the new dense shape

# Reshape the SparseTensor
reshaped_sparse_tensor = tf.raw_ops.SparseReshape(
    sparse_tensor,
    dense_shape,
    validate_indices=True
)

# Print the reshaped SparseTensor
print(reshaped_sparse_tensor)
