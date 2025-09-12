import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_splits, axis):
    indices, values, dense_shape = sparse_tensor.indices, sparse_tensor.values, sparse_tensor.dense_shape

    # Calculate the new dimension size for the split dimension
    new_dim_size = dense_shape[axis] // num_splits

    # Placeholders for the outputs
    outputs = [tf.SparseTensor(indices=tf.constant([[]], dtype=tf.int64), 
                               values=tf.constant([], dtype=values.dtype), 
                               dense_shape=dense_shape) for _ in range(num_splits)]

    for i in range(num_splits):
        # Calculate the indexing conditions for the splits
        condition = tf.logical_and(indices[:, axis] >= i * new_dim_size, indices[:, axis] < (i + 1) * new_dim_size)

        # Gather the indices and values that meet the condition
        new_indices = tf.boolean_mask(indices, condition)
        
        # Adjust indices to new local coordinate system
        new_indices = tf.tensor_scatter_nd_update(new_indices, 
                                                  tf.expand_dims(tf.range(tf.shape(new_indices)[0]), axis=-1),
                                                  new_indices[:, axis] - new_dim_size * i)

        new_values = tf.boolean_mask(values, condition)
        new_shape = tf.tensor_scatter_nd_update(dense_shape, 
                                                [[axis]], 
                                                [new_dim_size])

        # Create a new SparseTensor for this split
        outputs[i] = tf.SparseTensor(indices=new_indices,
                                     values=new_values,
                                     dense_shape=new_shape)

    return outputs

# Example usage
sparse_tensor_example = tf.SparseTensor(indices=[[0, 1], [2, 3]], 
                                        values=[1, 2], 
                                        dense_shape=[3, 4])

num_splits = 2
axis = 0
split_tensors = split_sparse_tensor(sparse_tensor_example, num_splits, axis)
