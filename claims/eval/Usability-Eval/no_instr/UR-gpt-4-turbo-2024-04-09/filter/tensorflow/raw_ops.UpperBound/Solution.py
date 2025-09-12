import tensorflow as tf

def apply_upper_bound(sorted_search_values, values):
    # Using tf.searchsorted which finds the indices at which values should be inserted to maintain order.
    return tf.searchsorted(sorted_search_values, values, side='right')

# Example usage
sorted_search_values = tf.constant([1, 3, 4, 5, 7], dtype=tf.float32)
values = tf.constant([2, 4, 6], dtype=tf.float32)

result = apply_upper_bound(sorted_search_values, values)
print(result)  # Output will show the indices where the values should be inserted.
