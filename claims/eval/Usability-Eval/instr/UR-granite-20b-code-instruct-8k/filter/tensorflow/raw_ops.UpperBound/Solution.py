import tensorflow as tf

sorted_search_values = tf.constant(...)
values = tf.constant(...)

upper_bound_result = tf.raw_ops.UpperBound(sorted_search_values, values)
