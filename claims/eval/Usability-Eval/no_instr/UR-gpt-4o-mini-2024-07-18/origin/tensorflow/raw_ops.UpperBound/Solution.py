import tensorflow as tf

def apply_upper_bound(sorted_search_values, values):
    # Using tf.raw_ops to apply upper_bound along each row
    result = tf.raw_ops.UpperBoundSortedSearchValues(sorted_search_values=sorted_search_values, values=values)
    return result

# Example usage
sorted_search_values = tf.constant([1, 3, 5, 7])
values = tf.constant([2, 4, 6])
upper_bound_result = apply_upper_bound(sorted_search_values, values)
print(upper_bound_result)
