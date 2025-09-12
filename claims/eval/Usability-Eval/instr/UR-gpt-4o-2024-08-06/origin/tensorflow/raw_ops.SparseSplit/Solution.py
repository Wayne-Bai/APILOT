import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_split, axis=0):
    """
    Splits a SparseTensor into `num_split` tensors along the specified `axis`.

    Parameters:
    - sparse_tensor: A tf.sparse.SparseTensor to be split.
    - num_split: An integer, the number of splits.
    - axis: An integer, the dimension along which to split. Default is 0.

    Returns:
    - A list of `num_split` SparseTensors resulting from the split.
    """
    # Convert SparseTensor to dense representation
    dense_tensor = tf.sparse.to_dense(sparse_tensor)
    
    # Split the dense tensor along the specified axis
    split_dense_tensors = tf.split(dense_tensor, num_or_size_splits=num_split, axis=axis)
    
    # Convert the resulting dense tensors back to SparseTensors
    split_sparse_tensors = [tf.sparse.from_dense(dense) for dense in split_dense_tensors]
    
    return split_sparse_tensors

# Example usage
if __name__ == "__main__":
    # Define a sample SparseTensor
    indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
    values = tf.constant([1, 2, 3], dtype=tf.int32)
    dense_shape = tf.constant([3, 4], dtype=tf.int64)
    sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_shape)

    # Split the SparseTensor into 2 parts along the first axis
    split_tensors = split_sparse_tensor(sparse_tensor, num_split=2, axis=0)

    # Print the resulting SparseTensors
    for i, result in enumerate(split_tensors):
        print(f"Split {i}: {result.indices.numpy()}, {result.values.numpy()}, {result.dense_shape.numpy()}")
