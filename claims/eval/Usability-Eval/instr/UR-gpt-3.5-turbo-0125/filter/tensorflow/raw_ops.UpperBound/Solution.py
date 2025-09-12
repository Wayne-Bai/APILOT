
import tensorflow as tf

# Define input tensors
sorted_search_values = tf.constant([[1, 2, 3], [4, 5, 6]])
values = tf.constant([[2, 1, 4], [5, 7, 6]])

# Apply upper_bound operation along each row
result = tf.math.maximum(sorted_search_values, values)

print(result)
