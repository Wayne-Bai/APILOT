import tensorflow as tf

# Create a tensor of values
values = tf.constant([[2, 5, 7], [1, 3, 8], [9, 4, 6]])

# Create a tensor of sorted search values
sorted_search_values = tf.constant([[10, 15, 20], [5, 10, 20], [15, 10, 10]])

# Apply the upper_bound function along each row
result = tf.raw_ops.UpperBound(sorted_search_values=sorted_search_values, values=values)

# Print the result
print(result)
