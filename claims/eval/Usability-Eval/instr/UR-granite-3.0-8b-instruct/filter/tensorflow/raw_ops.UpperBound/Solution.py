import tensorflow as tf

def upper_bound_along_rows(sorted_search_values, values):
    # Reshape values to match the shape of sorted_search_values
    values = tf.reshape(values, tf.shape(sorted_search_values))

    # Perform sorted search along each row
    upper_bounds = tf.searchsorted(sorted_search_values, values, side='right')

    return upper_bounds
