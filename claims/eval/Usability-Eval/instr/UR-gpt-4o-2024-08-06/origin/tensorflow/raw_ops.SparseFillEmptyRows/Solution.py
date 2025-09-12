import tensorflow as tf

def fill_empty_rows(sparse_indices, sparse_values, dense_shape, default_value):
    # Create a SparseTensor from the input.
    sparse_tensor = tf.sparse.SparseTensor(indices=sparse_indices, 
                                           values=sparse_values, 
                                           dense_shape=dense_shape)

    # Convert the SparseTensor to a dense tensor, filling empty rows with the default value.
    dense_tensor = tf.sparse.to_dense(sparse_tensor, default_value=default_value)

    return dense_tensor

# Example usage:
# SparseTensor with indices representing two entries: (0, 0) and (2, 1).
sparse_indices = [[0, 0], [2, 1]]
sparse_values = [1, 5]
dense_shape = [4, 3]  # Example shape with potentially empty rows.
default_value = 0  # Value to fill in empty rows.

result = fill_empty_rows(sparse_indices, sparse_values, dense_shape, default_value)
print("Dense tensor with filled empty rows:")
print(result.numpy())
