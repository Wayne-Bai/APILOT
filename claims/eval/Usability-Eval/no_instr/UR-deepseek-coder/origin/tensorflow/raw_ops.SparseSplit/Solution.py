import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_split, axis=1):
    # Ensure the input is a SparseTensor
    if not isinstance(sparse_tensor, tf.SparseTensor):
        raise ValueError("Input must be a SparseTensor")

    # Get the indices, values, and dense shape of the SparseTensor
    indices = sparse_tensor.indices
    values = sparse_tensor.values
    dense_shape = sparse_tensor.dense_shape

    # Calculate the split size
    split_size = dense_shape[axis] // num_split
    remainder = dense_shape[axis] % num_split

    # Split the indices and values along the specified axis
    split_indices = tf.split(indices, num_split, axis=0)
    split_values = tf.split(values, num_split, axis=0)

    # Create a list to hold the split SparseTensors
    split_sparse_tensors = []

    for i in range(num_split):
        # Adjust the indices to reflect the new split
        new_indices = split_indices[i]
        new_values = split_values[i]

        # Create the new dense shape for the split SparseTensor
        new_dense_shape = tf.concat([dense_shape[:axis], [split_size], dense_shape[axis+1:]], axis=0)

        # Create the new SparseTensor
        new_sparse_tensor = tf.SparseTensor(indices=new_indices, values=new_values, dense_shape=new_dense_shape)

        # Append the new SparseTensor to the list
        split_sparse_tensors.append(new_sparse_tensor)

    return split_sparse_tensors

# Example usage:
# Assuming you have a SparseTensor `st` and you want to split it into 3 parts along axis 1
# split_tensors = split_sparse_tensor(st, num_split=3, axis=1)
