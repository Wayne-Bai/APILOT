import tensorflow as tf

# Define the input tensors
sorted_search_values = tf.constant([1, 3, 5, 7, 9], dtype=tf.float32)
values = tf.constant([2, 4, 6, 8, 10], dtype=tf.float32)

# Apply the upper_bound method along each row
result = tf.raw_ops.UpperBound(sorted_search_values, values)

# Print the result
print(result)
