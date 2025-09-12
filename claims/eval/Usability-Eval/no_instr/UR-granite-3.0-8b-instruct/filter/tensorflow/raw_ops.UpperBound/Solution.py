import tensorflow as tf

def upper_bound_along_rows(sorted_search_values, values):
    # Ensure sorted_search_values and values have the same rank
    assert sorted_search_values.shape == values.shape

    # Sort the values along the last axis
    sorted_values, _ = tf.raw_ops.Sort(values, axis=-1)

    # Apply upper_bound along the last axis
    upper_bound = tf.raw_ops.UpperBound(sorted_search_values, values)

    return upper_bound
