import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_split, axis=1):
    # Ensure the input is a SparseTensor
    if not isinstance(sparse_tensor, tf.SparseTensor):
        raise ValueError("Input must be a SparseTensor")

    # Get the indices, values, and dense shape of the SparseTensor
    indices = sparse_tensor.indices
    values = sparse_tensor.values
    dense_shape = sparse_tensor.dense_shape

    # Calculate the split points
    split_dim_size = dense_shape[axis]
    if split_dim_size % num_split != 0:
        raise ValueError("The dimension to split is not divisible by num_split")

    split_size = split_dim_size // num_split

    # Create a mask for each split
    masks = [tf.reduce_all(tf.logical_and(indices[:, axis] >= i * split_size,
                                          indices[:, axis] < (i + 1) * split_size), axis=1)
             for i in range(num_split)]

    # Split the indices and values based on the masks
    split_indices = [tf.boolean_mask(indices, mask) for mask in masks]
    split_values = [tf.boolean_mask(values, mask) for mask in masks]

    # Adjust the indices for each split
    split_indices = [tf.concat([split_indices[i][:, :axis],
                                split_indices[i][:, axis:axis+1] - i * split_size,
                                split_indices[i][:, axis+1:]], axis=1)
                     for i in range(num_split)]

    # Create the split SparseTensors
    split_sparse_tensors = [tf.SparseTensor(indices=split_indices[i],
                                            values=split_values[i],
                                            dense_shape=dense_shape)
                            for i in range(num_split)]

    return split_sparse_tensors

# Example usage:
# Assuming `sparse_tensor` is a tf.SparseTensor
# split_sparse_tensors = split_sparse_tensor(sparse_tensor, num_split=2, axis=1)
