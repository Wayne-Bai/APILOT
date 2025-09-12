import tensorflow as tf

def upper_bound(sorted_search_values, values):
    # Ensure the input tensors are of the appropriate shape
    sorted_search_values = tf.convert_to_tensor(sorted_search_values)
    values = tf.convert_to_tensor(values)

    # Use tf.searchsorted to find indices for upper bound
    indices = tf.searchsorted(sorted_search_values, values, side='right')

    return indices

# Example usage
sorted_search_values = tf.constant([1, 3, 5, 7, 9])
values = tf.constant([0, 1, 2, 4, 6, 10])

result = upper_bound(sorted_search_values, values)
print(result.numpy())
