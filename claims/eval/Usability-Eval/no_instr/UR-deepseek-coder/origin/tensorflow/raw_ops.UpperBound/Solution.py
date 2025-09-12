import tensorflow as tf

def upper_bound(sorted_search_values, values):
    # Flatten the sorted_search_values and values for easier manipulation
    sorted_search_values_flat = tf.reshape(sorted_search_values, [-1])
    values_flat = tf.reshape(values, [-1])

    # Perform binary search to find the upper bound
    indices = tf.searchsorted(sorted_search_values_flat, values_flat, side='right')

    # Reshape the indices back to the original shape of values
    indices = tf.reshape(indices, tf.shape(values))

    return indices

# Example usage:
sorted_search_values = tf.constant([[1, 3, 5], [2, 4, 6]])
values = tf.constant([[2, 4, 6], [1, 3, 5]])

result = upper_bound(sorted_search_values, values)
print(result.numpy())
