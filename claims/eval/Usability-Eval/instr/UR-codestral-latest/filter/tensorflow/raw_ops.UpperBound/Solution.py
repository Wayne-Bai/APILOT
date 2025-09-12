import tensorflow as tf

def upper_bound(sorted_search_values, values):
    """
    This function returns the indices in `sorted_search_values` where each value from `values` can be inserted without changing the sorted order.
    The returned indices are the same shape as `values`.
    """
    num_search_values = tf.shape(sorted_search_values)[-1]
    indices = tf.searchsorted(sorted_search_values, values, side="right")
    # Clip indices to be within the range of `sorted_search_values`
    indices = tf.clip_by_value(indices, 0, num_search_values)
    return indices

# Example usage:
sorted_search_values = tf.constant([[1, 2, 2, 3], [0, 1, 2, 3]], dtype=tf.float32)
values = tf.constant([[2, 3.5, 1], [0, 0.5, 1.5]], dtype=tf.float32)

indices = upper_bound(sorted_search_values, values)

with tf.Session() as sess:
    print(sess.run(indices))
