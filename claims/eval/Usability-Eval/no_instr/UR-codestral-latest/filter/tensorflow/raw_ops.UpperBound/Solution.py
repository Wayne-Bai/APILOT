import tensorflow as tf

# Defining sorted_search_values and values for the demonstration
sorted_search_values = tf.constant([[1, 3, 5, 7], [2, 4, 6, 8]])
values = tf.constant([[2, 6, 8, 9], [0, 1, 5, 7]])

# Using tf.raw_ops.UpperBoundV2 to apply upper_bound
result = tf.raw_ops.UpperBoundV2(sorted_search_values=sorted_search_values, values=values)

print(result)
