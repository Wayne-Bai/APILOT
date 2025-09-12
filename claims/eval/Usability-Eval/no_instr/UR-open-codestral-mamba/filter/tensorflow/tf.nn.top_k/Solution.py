import tensorflow as tf

def find_largest_entries(input_tensor, k):
    # Use the tf.math.top_k function to find the k largest entries
    # This function returns the k largest elements and their indices
    k_largest_values, k_largest_indices = tf.math.top_k(input_tensor, k)

    return k_largest_values, k_largest_indices
