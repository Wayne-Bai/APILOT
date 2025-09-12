import tensorflow as tf

def apply_upper_bound(sorted_search_values, values):
    # Broadcasting values to match sorted_search_values' shape for comparison
    expanded_values = tf.expand_dims(values, 1)
    # Create a boolean mask where values are greater than sorted_search_values
    greater_mask = tf.greater(expanded_values, sorted_search_values)
    # Finding the first True value in each row which corresponds to the upper bound index
    upper_bounds_indices = tf.argmax(tf.cast(greater_mask, tf.int32), axis=1)
    return upper_bounds_indices

# Example usage:
sorted_search_values = tf.constant([[1, 3, 5, 7, 9], [0, 2, 4, 6, 8]], dtype=tf.float32)
values = tf.constant([6, 5], dtype=tf.float32)

result_indices = apply_upper_bound(sorted_search_values, values)
print("Upper bound indices:", result_indices.numpy())

# Optionally, retrieve the upper bound values using the indices,
# handling cases where all elements are less than the value
upper_bound_values = tf.gather(sorted_search_values, result_indices, batch_dims=1, axis=1)
print("Upper bound values:", upper_bound_values.numpy())
