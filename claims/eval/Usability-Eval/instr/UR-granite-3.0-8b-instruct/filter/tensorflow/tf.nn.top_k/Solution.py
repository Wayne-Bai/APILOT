import tensorflow as tf

def find_k_largest_entries(input_tensor, k):
    # Find the indices of the k largest entries in the last dimension
    k_largest_indices = tf.math.top_k(input_tensor, k, sorted=True)[1]

    # Find the values of the k largest entries in the last dimension
    k_largest_values = tf.gather(input_tensor, k_largest_indices)

    return k_largest_values, k_largest_indices
