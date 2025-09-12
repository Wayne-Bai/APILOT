
import tensorflow as tf

@tf.function
def get_upper_bound_along_row(sorted_search_values, values):
    # Sort the search values along each row in descending order
    sorted_search_values = tf.sort(sorted_search_values, axis=1)
    
    # Apply upper bound to get the last index that is less than or equal to the value
    upper_bound = tf.where(tf.less_equal(values, sorted_search_values), values, tf.constant(-1))
    
    return upper_bound
