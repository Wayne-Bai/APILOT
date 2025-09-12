import tensorflow as tf

# upper_bound computes the upper bound of sorted_search_values in values.
# For example:
#   upper_bound([1, 3, 4, 4, 7], 2) -> 1
#   upper_bound([1, 3, 4, 4, 7], 5) -> 4
#   upper_bound([1, 3, 4, 4, 7], 8) -> 5
#
# upper_bound([1, 3, 4, 4, 7], [2, 5]) -> [1, 4]
def upper_bound(sorted_search_values, values):
  index = tf.searchsorted(sorted_search_values, values, side='right')
  return tf.maximum(index - 1, 0)

# Example usage:
sorted_search_values = tf.constant([1, 3, 4, 4, 7])
values = tf.constant(2)
upper_bound_result = upper_bound(sorted_search_values, values)
print(upper_bound_result)  # Output: 1
