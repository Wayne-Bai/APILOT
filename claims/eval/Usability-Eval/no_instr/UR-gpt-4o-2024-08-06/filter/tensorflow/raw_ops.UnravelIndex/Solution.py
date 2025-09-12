import tensorflow as tf

def unravel_index(flat_index, dims):
    # Create a tensor for dims if it's not already
    if not isinstance(dims, tf.Tensor):
        dims = tf.constant(dims, dtype=tf.int32)
    
    # Calculate the unraveling indices
    unravel_indices = tf.unravel_index(flat_index, dims)
    
    return unravel_indices

# Example usage
dims = [3, 3]
flat_index = 5

indices = unravel_index(flat_index, dims)
print(indices)  # Output should be (array of row indices, array of column indices)
