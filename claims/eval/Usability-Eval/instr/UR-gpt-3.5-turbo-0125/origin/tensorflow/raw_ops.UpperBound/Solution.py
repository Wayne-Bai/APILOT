
import tensorflow as tf

# Define the input tensors
sorted_search_values = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float32)
values = tf.constant([[0.5], [5.5], [9.5]], dtype=tf.float32)

# Apply the upper_bound operation along each row
result = tf.raw_ops.UpperBound(sorted_search_values=sorted_search_values, values=values)

# Print the result
print(result)
