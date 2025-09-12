import tensorflow as tf

def upper_bound(sorted_search_values, values):
    return tf.searchsorted(sorted_search_values, values, side='right')

# Example usage:
sorted_search_values = tf.constant([[1, 3, 5, 7], [2, 4, 6, 8]], dtype=tf.float32)
values = tf.constant([[2, 6], [3, 5]], dtype=tf.float32)
result = upper_bound(sorted_search_values, values)

# Run the tensorflow operation to get the results
with tf.Session() as sess:
    print(sess.run(result))
