import tensorflow as tf

def generate_sparse_cross(sparse_indices, sparse_values, sparse_shapes, dense_inputs):
    """
    Generates sparse cross from a list of sparse and dense tensors.

    Args:
        sparse_indices (list): A list of 2D tensors representing the indices of the sparse tensors.
        sparse_values (list): A list of 1D tensors representing the values of the sparse tensors.
        sparse_shapes (list): A list of 1D tensors representing the shapes of the sparse tensors.
        dense_inputs (list): A list of 2D tensors representing the dense inputs.

    Returns:
        A SparseTensor resulting from the cross operation.
    """
    # Create sparse tensors from the input values
    sparse_tensors = []
    for indices, values, shape in zip(sparse_indices, sparse_values, sparse_shapes):
        sparse_tensors.append(tf.SparseTensor(indices, values, shape))

    # Create the dense tensors
    dense_tensors = [tf.convert_to_tensor(dense_input) for dense_input in dense_inputs]

    # Calculate the sparse cross
    sparse_cross = tf.raw_ops.SparseCross(
        sparse_indices=sparse_indices,
        num_sparse=1,
        sparse_values=sparse_values,
        dense_inputs=dense_tensors,
        hash_ids=[0],
        num_buckets=1000,
        out_type=tf.dtypes.int64
    )

    return sparse_cross

# Example usage
sparse_indices = [[0, 0], [1, 2]]
sparse_values = [1.0, 2.0]
sparse_shapes = [3, 4]
dense_inputs = [[1.0, 2.0], [3.0, 4.0]]

sparse_cross = generate_sparse_cross([sparse_indices], [sparse_values], [sparse_shapes], [dense_inputs])
print(sparse_cross)
