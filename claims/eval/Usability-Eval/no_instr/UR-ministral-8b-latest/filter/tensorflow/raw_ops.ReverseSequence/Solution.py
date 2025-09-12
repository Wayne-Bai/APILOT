import tensorflow as tf

# Define a function to find the index of the last non-zero element in a variable length list of 1-D tensors
def last_non_zero_index(tensors):
    all_last_indices = tf.raw_ops.Reverse(variable_length_axes=tensors)
    max_last_index = tf.reduce_max(all_last_indices)
    return max_last_index

# Example usage:
tensors = [tf.constant([1, 2, 0, 5, 0, 0]), tf.constant([0, 0, 6, 7]), tf.constant([0, 8, 0, 0])]
indices = last_non_zero_index(tensors)
print("The last non-zero index is:", indices)
