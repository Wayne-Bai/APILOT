import tensorflow as tf

def dataset_from_sparse_tensor(sparse_tensor):
    """
    Creates a dataset that splits a `SparseTensor` into elements row-wise.
    
    Args:
    sparse_tensor: A SparseTensor.

    Returns:
    A `tf.data.Dataset` where each element is a row slice of the original SparseTensor.
    """
    indices = sparse_tensor.indices
    values = sparse_tensor.values
    dense_shape = sparse_tensor.dense_shape

    # Determine maximum number of rows based on the indices of the SparseTensor
    num_rows = dense_shape[0]

    # Create a dataset of row indices
    row_dataset = tf.data.Dataset.range(num_rows)

    # Filter the amenities for each row in the SparseTensor
    def fetch_row_amenities(row):
        # Find matching indices for the current row
        row_mask = tf.math.equal(indices[:, 0], row)
        # Fetch the values at these indices
        row_values = tf.boolean_mask(values, row_mask)
        # Return the sparse tensor for the current row
        return tf.sparse.reorder(tf.SparseTensor(indices=tf.boolean_mask(indices, row_mask)[:, 1:],
                                                values=row_values,
                                                dense_shape=dense_shape[1:]))

    # Map each element in row_dataset (row numbers) to its corresponding amenities
    final_dataset = row_dataset.map(fetch_row_amenities)

    return final_dataset

# Example usage:
# Create a SparseTensor
example_indices = tf.constant([[0, 0], [1, 2], [2, 3]])
example_values = tf.constant([1, 2, 3])
example_dense_shape = tf.constant([3, 4])
example_sparse_tensor = tf.SparseTensor(indices=example_indices, 
                                        values=example_values, 
                                        dense_shape=example_dense_shape)

# Create a dataset from the SparseTensor
resulting_dataset = dataset_from_sparse_tensor(example_sparse_tensor)

# Print each element in the resulting dataset
for item in resulting_dataset:
    print(tf.sparse.to_dense(item))
