import tensorflow as tf

def generate_sparse_cross(sparse_tensors, dense_tensors):
    """Generates sparse cross from a list of sparse and dense tensors.

    Args:
      sparse_tensors: A list of SparseTensor objects.
      dense_tensors: A list of dense tensors.

    Returns:
      A SparseTensor representing the cross of the input tensors.
    """
    # Ensure sparse_tensors is a list of SparseTensor
    if not all(isinstance(t, tf.Tensor) and t.dtype == tf.int64 for t in sparse_tensors):
        raise ValueError("All sparse_tensors must be SparseTensor objects.")
    
    # Ensure dense_tensors is a list of dense tensors
    if not all(isinstance(t, tf.Tensor) for t in dense_tensors):
        raise ValueError("All dense_tensors must be Tensor objects.")

    # Create the sparse cross using scatter_nd
    sparse_cross_result = tf.raw_ops.SparseCross(
        sparse_tensors=sparse_tensors,
        dense_tensors=dense_tensors
    )

    return sparse_cross_result

# Example usage:
# sparse_tensors = [tf.SparseTensor(...) , ...]
# dense_tensors = [tf.constant(...), ...]
# result = generate_sparse_cross(sparse_tensors, dense_tensors)
