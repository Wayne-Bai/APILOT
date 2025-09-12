
import tensorflow as tf

def upper_bound_tf(sorted_search_values, values):
    """Applies upper_bound(sorted_search_values, values) along each row."""
    # Create a list of pairs containing the sorted search values and their corresponding indices
    sorted_search_value_indices = [(value, i) for i, value in enumerate(sorted_search_values)]

    # Sort the list of pairs based on the first element (sorted search values)
    sorted_pairs = sorted(sorted_search_value_indices, key=lambda x: x[0])

    # Use tf.raw_ops.UpperBound to find the upper bound for each row
    upper_bounds = [tf.raw_ops.UpperBound(values=[pair[1] for pair in sorted_pairs],
                                           sorted_search_values=[pair[0] for pair in sorted_pairs])]

    # Return the list of upper bounds
    return upper_bounds
