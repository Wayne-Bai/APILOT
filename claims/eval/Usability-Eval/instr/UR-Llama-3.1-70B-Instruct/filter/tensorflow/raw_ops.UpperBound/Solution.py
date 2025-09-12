# Import necessary tensorflow modules
import tensorflow as tf

# Define a function that applies upper bound to sorted search values along each row
def upper_bound(sorted_search_values, values):
    # Use tf.searchsorted to find the insertion point for values in sorted_search_values to maintain sorted order
    indices = tf.searchsorted(sorted_search_values, values, side='right') - 1
    
    # Ensure indices are within bounds
    indices = tf.clip_by_value(indices, 0, tf.shape(sorted_search_values)[1] - 1)
    
    # Return the values at the indices
    return tf.gather(sorted_search_values, indices, axis=1, batch_dims=1)


# Example usage
sorted_search_values = tf.constant([[1, 3, 5, 7], [2, 4, 6, 8]])
values = tf.constant([4, 5, 6])

result = upper_bound(sorted_search_values, values)

print(result)
