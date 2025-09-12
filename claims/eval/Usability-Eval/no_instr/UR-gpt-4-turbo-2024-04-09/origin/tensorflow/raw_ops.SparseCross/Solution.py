import tensorflow as tf

def generate_sparse_cross(sparse_tensors, dense_tensors, hashed_output=True, num_buckets=0, hash_key=None):
    """Generate a sparse cross of the given sparse and dense tensors.

    Args:
    sparse_tensors (list of tf.SparseTensor): List of SparseTensor inputs.
    dense_tensors (list of tf.Tensor): List of DenseTensor inputs.
    hashed_output (bool): If True, output is hashed to num_buckets. If False, strings are output
    num_buckets (int): It is used if hashed_output is True. It defines the number of buckets.
    hash_key (int): Specify the hash_key to use. Defaults to None.

    Returns:
    tf.SparseTensor: The resulted SparseTensor of the cross operation.
    """
    return tf.raw_ops.SparseCross(
        indices=[sp.indices for sp in sparse_tensors],
        values=[sp.values for sp in sparse_tensors],
        shapes=[sp.dense_shape for sp in sparse_tensors],
        dense_inputs=dense_tensors,
        hashed_output=hashed_output,
        num_buckets=num_buckets,
        hash_key=hash_key
    )

# Example usage:
# Sparse tensor examples (assuming they are already created)
sparse_tensor1 = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=['a', 'b'], dense_shape=[2, 3])
sparse_tensor2 = tf.SparseTensor(indices=[[0, 1], [1, 1]], values=['x', 'y'], dense_shape=[2, 2])

# Dense tensor example
dense_tensor = tf.constant(['one', 'two', 'three'])

# Call the function
result_sparse_tensor = generate_sparse_cross([sparse_tensor1, sparse_tensor2], [dense_tensor])

# To evaluate the SparseTensor you may need to use a session or convert it to a dense format if it's necessary 
# for further processing, for instance, tf.sparse.to_dense(result_sparse_tensor) in a eager execution environment.
