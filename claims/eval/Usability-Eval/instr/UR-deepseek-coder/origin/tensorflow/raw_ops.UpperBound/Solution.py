import tensorflow as tf

def upper_bound(sorted_search_values, values):
    # Flatten the sorted_search_values and values to apply binary search
    sorted_search_values_flat = tf.reshape(sorted_search_values, [-1])
    values_flat = tf.reshape(values, [-1])

    # Apply binary search to find the upper bound
    indices = tf.searchsorted(sorted_search_values_flat, values_flat, side='right')

    # Reshape the indices back to the original shape of values
    original_shape = tf.shape(values)
    result = tf.reshape(indices, original_shape)

    return result

# Example usage:
sorted_search_values = tf.constant([[1, 3, 5], [2, 4, 6]])
values = tf.constant([[2, 4, 6], [1, 3, 5]])

result = upper_bound(sorted_search_values, values)
print(result.numpy())
