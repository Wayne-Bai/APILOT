import tensorflow as tf

def apply_upper_bound(sorted_search_values, values):
    # Ensure sorted_search_values is sorted in ascending order
    sorted_search_values = tf.sort(sorted_search_values, axis=-1)

    # Perform a binary search for each value in values
    binary_search_results = tf.searchsorted(sorted_search_values, values, side='right')

    # Apply the upper_bound by subtracting 1 from the binary search results
    upper_bound = binary_search_results - 1

    return upper_bound
