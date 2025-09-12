import tensorflow as tf

# Define the inputs
values = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)
sorted_search_values = tf.constant([[0.5, 2, 3], [1, 3.5, 6]], dtype=tf.float32)

# Create func to apply upper_bound
def upper_bound(row_values, search_values):
    return tf.raw_ops.UpperBound(row_values, search_values)

# Apply the upper_bound along each row
result = tf.map_fn(lambda x: upper_bound(x, sorted_search_values), values, dtype=tf.float32)

print(result)
