import tensorflow as tf

# Ensure the correct version of TensorFlow is installed
if not tf.__version__.startswith('2'):
    raise ImportError("This code requires TensorFlow 2.x")

def sparse_output_bin_counting(sparse_indices, sparse_values, sparse_shape, weights, num_bins):
    """
    Performs sparse-output bin counting for a sparse tensor input.

    Args:
    sparse_indices: A 2D Tensor of type int64. 0th dimension has shape (num_entries, dim)
    sparse_values: A 1D Tensor containing the values associated with each position in sparse_indices.
    sparse_shape: A 1D Tensor of size dim, the full shape of the sparse tensor.
    weights: A 1D Tensor, containing per-entry weight. Must be the same shape as sparse_values.
    num_bins: An int, the number of bins to bucket values into.

    Returns:
    A Tensor with the same shape as 'sparse_shape', with values being the count of values fallen into each bin.
    """
    # Check the input tensor's types and shapes
    if not (tf.is_tensor(sparse_indices) and tf.is_tensor(sparse_values) and tf.is_tensor(sparse_shape) and tf.is_tensor(weights)):
        raise ValueError("All inputs must be tensors.")

    # This operation will take the sparse representation and produce a dense output after binning
    output_tensor = tf.raw_ops.SparseCountSparseOutput(
        indices=sparse_indices,
        values=sparse_values,
        weights=weights,
        dense_shape=sparse_shape,
        binary_output=False,
        minlength=0,
        maxlength=num_bins,
        axis=-1
    )

    return output_tensor

# Example variables to define a sparse tensor
sparse_indices = tf.constant([[0, 1], [1, 2]])
sparse_values = tf.constant([1, 2])
sparse_shape = tf.constant([3, 4])
weights = tf.constant([1.0, 1.0])
num_bins = 5

# Function call
result = sparse_output_bin_counting(sparse_indices, sparse_values, sparse_shape, weights, num_bins)
print("Bin counting result:", result)
