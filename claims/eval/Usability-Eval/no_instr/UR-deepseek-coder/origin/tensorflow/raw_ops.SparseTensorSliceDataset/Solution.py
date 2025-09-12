import tensorflow as tf

def split_sparse_tensor(sparse_tensor):
    # Get the shape of the SparseTensor
    shape = sparse_tensor.dense_shape
    
    # Create a dataset from the SparseTensor's indices and values
    indices = sparse_tensor.indices
    values = sparse_tensor.values
    
    # Create a dataset of indices and values
    dataset = tf.data.Dataset.from_tensor_slices((indices, values))
    
    # Group the indices and values by row (i.e., by the first dimension of the indices)
    dataset = dataset.group_by_window(
        key_func=lambda index, value: index[0],  # Key is the first dimension of the index
        reduce_func=lambda key, window: (tf.gather(indices, window.map(lambda idx, val: idx[1])),
                                         tf.gather(values, window.map(lambda idx, val: idx[1]))),
        window_size=shape[0]
    )
    
    return dataset

# Example usage:
# Assuming `sparse_tensor` is a SparseTensor object
# dataset = split_sparse_tensor(sparse_tensor)
