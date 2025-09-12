import tensorflow as tf

# Define the sorted_search_values and values
sorted_search_values = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
values = tf.constant([[10, 5, 12], [5, 6, 8], [7, 11, 10]])

# Define a function to replace values that are not in sorted_search_values
def upper_bound(sorted_search_values, values):
    values_rank = tf.rank(values)
    sorted_search_values_rank = tf.rank(sorted_search_values)
    
    # Check if values is a one-dimensional tensor or a tensor with a higher rank
    if tf.math.equal(values_rank, 1):
        index = tf.searchsorted(sorted_search_values, values, side='right')
    else:
        index = tf.searchsorted(sorted_search_values, values, batch_dims=1, side='right')
    
    # Set index out of bounds to the upper bound
    index_set_out_of_bounds = tf.where(
        tf.math.greater_equal(index, tf.shape(sorted_search_values)[-1]),
        tf.fill(tf.shape(index), tf.shape(sorted_search_values)[-1]),
        index
    )
    
    # Replace values that are not in sorted_search_values with the upper bound
    result = tf.gather(sorted_search_values, index_set_out_of_bounds)
    
    return result

# Apply the function to each row
result = tf.map_fn(lambda x: upper_bound(sorted_search_values, x), values)

# Print the result
print(result)
