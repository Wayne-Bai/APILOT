import tensorflow as tf

def apply_upper_bound(sorted_search_values, values):
    # Using `tf.raw_ops.UpperBound` to apply the operation along each row
    result = tf.raw_ops.UpperBound(sorted_inputs=sorted_search_values, values=values)
    return result

# Example usage
sorted_search_values = tf.constant([[1, 3, 5, 7, 9], [0, 2, 4, 6, 8]], dtype=tf.float32)
values = tf.constant([[3, 6], [5, 7]], dtype=tf.float32)

result = apply_upper_bound(sorted_search_values, values)
print(result)
