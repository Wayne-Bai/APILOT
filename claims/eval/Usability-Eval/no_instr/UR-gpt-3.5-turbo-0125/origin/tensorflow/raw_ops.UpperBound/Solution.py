
import tensorflow as tf

values = tf.constant([[1, 3, 5], [7, 9, 11]])
sorted_search_values = tf.constant([[2, 4, 6], [8, 10, 12]])

result = tf.raw_ops.UpperBound(sorted_search_values=sorted_search_values, values=values)

print(result)
