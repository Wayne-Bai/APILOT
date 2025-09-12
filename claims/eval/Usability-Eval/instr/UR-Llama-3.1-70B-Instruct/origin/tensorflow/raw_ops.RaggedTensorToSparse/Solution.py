# Import the necessary libraries
import tensorflow as tf

# Create a RaggedTensor
values = tf.constant([1, 2, 3, 4, 5, 6])
row_splits = tf.constant([0, 3, 3, 6])
ragged_tensor = tf.RaggedTensor.from_row_splits(values, row_splits)

# Convert the RaggedTensor into a SparseTensor
sparse_tensor = tf.raw_ops.RaggedTensorToSparse(ragged_tensor.flat_values,
                                                ragged_tensor.row_splits,
                                                ragged_tensor.row_splits[1:],
                                                tf.constant(ragged_tensor.shape[0],
                                                            dtype=tf.int64),
                                                tf.constant(ragged_tensor.shape[1],
                                                            dtype=tf.int64))

# Print the SparseTensor
print(sparse_tensor)

# Also, there is `tf.sparse.from_dense()` however if we're specifically working with ragged tensors, I've included the method for direct ragged tensor conversion support. Example below:
# however if we want to verify result we can create a base sparse tensor from RaggedTensor and run the comparison 
# as part comparison support section

values = tf.constant([[1, 2, 3], [4, 5, 6]])
sparse_tensor_from_dense = tf.sparse.from_dense(values)
print(sparse_tensor_from_dense)

# or run the RaggedTensor.from_sparse('./path', [1,2,3]) for verification 
# prints comparison support section

values = tf.constant([1, 2, 3, 4, 5, 6])
row_lengths = tf.constant([1, 5])
values_verifying_variable = tf.RaggedTensor.from_sparse(tf.RaggedTensor.from_row_splits(values, 
                                                                                       row_lengths))
# use point Rvalues('./path', [1,2,3]) for verification 
print(values_verifying_variable)
