import tensorflow as tf

# Assuming existing variables sorted_search_values and values are defined
sorted_search_values = tf.constant([1, 2, 3, 4], dtype=tf.float32)
values = tf.constant([[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]], dtype=tf.float32)

# Define the function to apply upper_bound
def upper_bound_values(values):
    return tf.raw_ops.upper_bound(sorted_search_values, values)

result = upper_bound_values(values)
print(result)
