import tensorflow as tf

def upper_bound(values, sorted_values, row_labels):
    """
    Apply upper_bound along axis 1 (i.e., row-wise).

    Args:
        values ([tf.Tensor]): The tensor of values.
        sorted_values ([tf.Tensor]): The tensor containing sorted values used for the upper bound operation.
        row_labels (tf.Tensor): The label for each row, used to identify the upper_limit values.

    Returns:
        tf.Tensor: The tensor for which the upper_bound operation is performed.
    """
    upper_bounds = tf.raw_opsUpperBound(v=v, k=sorted_values[:, 1], max_over_j=tf.cast(tf.range(tf.shape(values)[1]), tf.int32), dim=tf.optimal_dimension(axis=1)[:1] + 1)
    filtered_values = tf.cond(tf.reduce_any(row_labels == 1), lambda: tf.where(row_labels == 1, upper_bounds, tf.cast(-1e10, tf.float32)),
                              lambda: tf.where(row_labels == 0, upper_bounds, upper_bounds))
    return filtered_values

# Test the function
values = tf.constant([[5, 7, 2], [3, 5, 6], [1, 3, 4]])
sorted_values = tf.constant([[1, 1], [2, 2], [3, 3]])
row_labels = tf.constant([1, 1, 0])

result = upper_bound(values, sorted_values, row_labels)
print(result)
