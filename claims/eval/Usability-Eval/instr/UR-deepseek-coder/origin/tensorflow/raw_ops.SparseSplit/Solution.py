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
    masks = [tf.reduce_all(tf.logical_and(
        indices[:, axis] >= i * split_size,
        indices[:, axis] < (i + 1) * split_size
    ), axis=1) for i in range(num_split)]

    # Split the indices and values based on the masks
    split_indices = [tf.boolean_mask(indices, mask) for mask in masks]
    split_values = [tf.boolean_mask(values, mask) for mask in masks]

    # Adjust the indices for each split
    split_indices = [tf.concat([
        indices[:, :axis],
        indices[:, axis:axis+1] - i * split_size,
        indices[:, axis+1:]
    ], axis=1) for i, indices in enumerate(split_indices)]

    # Create the split SparseTensors
    split_sparse_tensors = [
        tf.SparseTensor(
            indices=split_indices[i],
            values=split_values[i],
            dense_shape=tf.concat([
                dense_shape[:axis],
                [split_size],
                dense_shape[axis+1:]
            ], axis=0)
        ) for i in range(num_split)
    ]

    return split_sparse_tensors

# Example usage:
# sparse_tensor = ... (create or load your SparseTensor)
# num_split = 2
# split_tensors = split_sparse_tensor(sparse_tensor, num_split)
