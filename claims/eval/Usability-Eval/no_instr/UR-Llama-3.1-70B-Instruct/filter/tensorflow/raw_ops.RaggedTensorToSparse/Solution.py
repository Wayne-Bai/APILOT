# Import necessary modules
import tensorflow as tf

# Function to convert RaggedTensor to SparseTensor
def ragged_to_sparse(ragged_tensor):
    # Get the values, row_splits, and row_lengths from the RaggedTensor
    values = ragged_tensor.values
    row_splits = ragged_tensor.row_splits
    row_lengths = ragged_tensor.row_lengths

    # Calculate the dense shape of the RaggedTensor
    dense_shape = [row_splits.shape[0] - 1, row_lengths.max()]

    # Create a SparseTensor with the same values
    sparse_tensor = tf.sparse.SparseTensor(
        indices=tf.where(tf.sequence_mask(row_lengths, maxlen=row_lengths.max())), 
        values=values,
        dense_shape=dense_shape
    )

    return sparse_tensor

# Example usage:
# Create a RaggedTensor
ragged_tensor = tf.RaggedTensor.from_row_splits(
    values=[1, 2, 3, 4, 5, 6],
    row_splits=[0, 4, 4, 6, 6, 6]
)

# Convert RaggedTensor to SparseTensor
sparse_tensor = ragged_to_sparse(ragged_tensor)

# Print the result
print(sparse_tensor.indices)
print(sparse_tensor.values)
print(sparse_tensor.dense_shape)
