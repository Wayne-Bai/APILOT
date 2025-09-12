import tensorflow as tf

def upper_bound_row_wise(sorted_search_values, values):
    # Convert inputs to tensors if they are not already
    sorted_search_values_tensor = tf.convert_to_tensor(sorted_search_values)
    values_tensor = tf.convert_to_tensor(values)

    # Apply tf.math.searchsorted operation along each row
    upper_bound_indices = tf.map_fn(
        lambda x: tf.math.searchsorted(sorted_search_values_tensor, x), values_tensor, dtype=tf.int32)

    return upper_bound_indices
