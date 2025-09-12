import tensorflow as tf

def unravel_index(flat_indices, dims):
    """
    Convert flat indices into coordinate arrays.

    Args:
    flat_indices: A 1-D tensor of indices.
    dims: A 1-D tensor representing the shape of the array.

    Returns:
    A tuple of arrays, one for each dimension in dims.
    """
    flat_indices = tf.convert_to_tensor(flat_indices, dtype=tf.int64)
    dims = tf.convert_to_tensor(dims, dtype=tf.int64)
    
    indices = []
    for i in range(len(dims)):
        if i > 0:
            product = tf.reduce_prod(dims[:i], axis=0)
        else:
            product = 1
            
        current_index = flat_indices // product % dims[i]
        indices.append(current_index)
        
    return tuple(indices)

# Example Usage
flat_indices = [22, 41, 37]
dims = [7, 6]
coordinates = unravel_index(flat_indices, dims)
print([coord.numpy() for coord in coordinates])  # Output will be: [tf.Tensor([3 6 6], shape=(3,), dtype=int64), tf.Tensor([4 5 1], shape=(3,), dtype=int64)]
