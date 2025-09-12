import tensorflow as tf

def apply_upper_bound(sorted_search_values, values):
    return tf.raw_ops.UpperBound(sorted_search_values=sorted_search_values, values=values)