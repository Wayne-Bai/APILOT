import tensorflow as tf

# Define a function to replicate the 'upper_bound' operation
def upper_bound(sorted_search_values, values):
    # Get the maximum values along the last dimension
    max_values = tf.math.reduce_max(sorted_search_values, axis=-1, keepdims=True)

    # Use tf.where to compare the maximum values with the values tensor
    # This will return a tensor of boolean values where the maximum values are greater than or equal to the values
    # We then use tf.cast to convert this boolean tensor to a tensor of int32 type
    # Finally, we sum along the last dimension to get the 'upper_bound' values
    upper_bound_values = tf.cast(tf.math.greater_equal(max_values, values), tf.int32)
    upper_bound_values = tf.reduce_sum(upper_bound_values, axis=-1)

    return upper_bound_values

# Example usage:
sorted_search_values = tf.constant([[1, 3, 5, 7], [2, 4, 6, 8]], dtype=tf.int32)
values = tf.constant([[3], [6]], dtype=tf.int32)
result = upper_bound(sorted_search_values, values)
print(result)
