import tensorflow as tf

def apply_upper_bound(sorted_search_values, values):
    # To find the upper bound, we use tf.searchsorted which returns the indices
    # where elements should be inserted to maintain order.
    # But since we want upper bound, we add 1 to the indices.
    indices = tf.searchsorted(sorted_search_values, values, side='right')
    return indices

# Test the function
sorted_search_values = tf.constant([[1, 3, 5], [2, 4, 6]])
values = tf.constant([[2, 4], [3, 5]])
print(apply_upper_bound(sorted_search_values, values).numpy())
