import tensorflow as tf

def upper_bound(sorted_search_values, values):
    with tf.name_scope("UpperBound"):
        # Reshape the tensors to have a trailing dimension.
        sorted_search_values = tf.reshape(sorted_search_values, [-1, tf.shape(sorted_search_values)[-1], 1])
        values = tf.reshape(values, [-1, 1, tf.shape(values)[-1]])

        # Perform the broadcasting to compute the comparisons.
        comparisons = sorted_search_values >= values

        # Find the rightmost True within each row and return its column index.
        rightmost_true = tf.reduce_sum(tf.cast(comparisons, tf.int32), axis=-1) - 1
        return rightmost_true

# Example usage:
sorted_search_values = tf.constant([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])
values = tf.constant([[2, 6], [1, 8]])
output = upper_bound(sorted_search_values, values)
print(output)
