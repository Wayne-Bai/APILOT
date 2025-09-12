import tensorflow as tf

# Create a sample tensor with sorted search values
sorted_search_values = tf.constant([[1, 3, 5, 7],
                                    [2, 4, 6, 8]], dtype=tf.int32)

# Values to search the upper bounds for
values = tf.constant([[0, 2, 6, 8],
                      [1, 3, 5, 9]], dtype=tf.int32)

# Apply upper_bound operation along each row
upper_bounds = tf.raw_ops.UpperBound(sorted_inputs=sorted_search_values, values=values)

print(upper_bounds)
