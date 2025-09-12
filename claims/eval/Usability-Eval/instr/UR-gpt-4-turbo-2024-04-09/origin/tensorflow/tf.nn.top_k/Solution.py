import tensorflow as tf

def find_top_k_values_indices(tensor, k):
    # Using tf.math.top_k to find the k largest entries and their indices along the last dimension of the tensor
    values, indices = tf.math.top_k(tensor, k=k)
    return values, indices
