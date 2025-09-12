import tensorflow as tf

def upper_bound(sorted_search_values, values):
    # Flatten the sorted_search_values and values to apply binary search
    flat_sorted_search_values = tf.reshape(sorted_search_values, [-1])
    flat_values = tf.reshape(values, [-1])
    
    # Perform binary search to find the upper bound
    indices = tf.searchsorted(flat_sorted_search_values, flat_values, side='right')
    
    # Reshape the indices back to the original shape of values
    original_shape = tf.shape(values)
    result = tf.reshape(indices, original_shape)
    
    return result

# Example usage:
sorted_search_values = tf.constant([[1, 3, 5, 7], [2, 4, 6, 8]])
values = tf.constant([[2, 4, 6], [3, 5, 7]])

result = upper_bound(sorted_search_values, values)
print(result.numpy())
