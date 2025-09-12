
import tensorflow as tf

# Create a RaggedTensor from a list of lists
ragged_tensor = tf.RaggedTensor.from_row_lengths(
    values=[[1, 2, 3], [4, 5], [6, 7, 8, 9]],
    row_lengths=[3, 2, 4])

# Convert the RaggedTensor to a SparseTensor
sparse_tensor = tf.raw_ops.RaggedTensorToSparse(
    input=ragged_tensor,
    valid_row_mask=tf.reduce_any(ragged_tensor, axis=1))

# Print the sparse tensor
print(sparse_tensor)
