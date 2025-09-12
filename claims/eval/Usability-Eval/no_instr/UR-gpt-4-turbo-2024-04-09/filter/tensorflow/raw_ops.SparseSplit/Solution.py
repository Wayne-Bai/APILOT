import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_splits, axis):
    """Split a SparseTensor into `num_split` tensors along a specific `axis`."""
    indices = sparse_tensor.indices
    values = sparse_tensor.values
    dense_shape = sparse_tensor.dense_shape
    
    if axis < 0:
        axis += indices.shape[1]
    
    # Calculate split sizes
    total_size_along_axis = dense_shape[axis]
    split_size = total_size_along_axis // num_splits
    remaining_size = total_size_along_axis % num_splits
    
    sizes = [split_size] * num_splits
    for i in range(remaining_size):
        sizes[i] += 1
    
    # Determine the ranges for each split
    limits = tf.cumsum(sizes)
    starts = tf.concat([[0], limits[:-1]], axis=0)
    ranges = tf.stack([starts, limits], axis=1)
    
    # Create mask for each split
    def in_range(x):
        mask = tf.logical_and(indices[:, axis] >= x[0], indices[:, axis] < x[1])
        return mask
    
    masks = tf.map_fn(in_range, ranges, dtype=tf.bool)
    
    # Produce the split SparseTensors
    split_tensors = []
    for i in range(num_splits):
        mask = masks[i]
        new_indices = tf.boolean_mask(indices, mask)
        new_values = tf.boolean_mask(values, mask)
        
        # Adjust indices according to split
        new_indices = tf.concat(
            [new_indices[:, :axis], new_indices[:, axis:] - starts[i], new_indices[:, axis+1:]],
            axis=1
        )
        
        new_dense_shape = tf.concat(
            [dense_shape[:axis], [sizes[i]], dense_shape[axis+1:]],
            axis=0
        )
        
        split_tensors.append(tf.SparseTensor(indices=new_indices, values=new_values, dense_shape=new_dense_shape))
    
    return split_tensors

# Example usage:
sparse_tensor = tf.SparseTensor(
    indices=[[0, 1], [1, 2], [2, 4]],
    values=[1, 2, 3], 
    dense_shape=[3, 5]
)
num_splits = 2
axis = 1  # Split along the second dimension

split_tensors = split_sparse_tensor(sparse_tensor, num_splits, axis)
for st in split_tensors:
    print('Indices:\n', st.indices.numpy())
    print('Values:\n', st.values.numpy())
    print('Shape:\n', st.dense_shape.numpy())
