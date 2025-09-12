import tensorflow as tf

# Create a tensor for sorted values
sorted_search_values = tf.constant([[1, 3, 5, 7], [10, 12, 14, 16]], dtype=tf.int32)

# Create a tensor for values for which the upper bound needs to be found
values = tf.constant([[0, 2, 5, 8], [9, 11, 15, 17]], dtype=tf.int32)

# Use tf.searchsorted to find the upper bound index along each row
upper_bound_indices = tf.searchsorted(sorted_search_values, values, side='right')

with tf.Session() as sess:
    result = sess.run(upper_bound_indices)
    print(result)
