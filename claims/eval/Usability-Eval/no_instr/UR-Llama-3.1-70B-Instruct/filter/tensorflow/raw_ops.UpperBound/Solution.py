import tensorflow as tf

def sorted_search(values, sorted_search_values, upper_bound):
    """
    Applies upper_bound(sorted_search_values, values) along each row.
    
    Args:
        values (tf.Tensor): The values to search for.
        sorted_search_values (tf.Tensor): The sorted values to search in.
        upper_bound (bool): Whether to return the upper bound or not.
        
    Returns:
        tf.Tensor: The indices of the upper bound or the insertion point for the values in sorted_search_values.
    """
    # Use tf.searchsorted to perform the search
    # The side argument controls whether to return the upper or lower bound
    side = 'right' if upper_bound else 'left'
    indices = tf.searchsorted(sorted_search_values, values, side=side)
    
    return indices

# Example usage
with tf.device('/cpu:0'):
    # Create sorted search values
    sorted_search_values = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32)
    sorted_search_values = tf.expand_dims(sorted_search_values, axis=0)
    sorted_search_values = tf.tile(sorted_search_values, [5, 1])
    
    # Create values to search for
    values = tf.constant([2.5, 3.5, 4.5, 1.5, 2.5], dtype=tf.float32)
    values = tf.expand_dims(values, axis=1)
    
    # Perform the search
    indices = sorted_search(values, sorted_search_values, upper_bound=True)
    
    # Print the indices
    print(indices)
