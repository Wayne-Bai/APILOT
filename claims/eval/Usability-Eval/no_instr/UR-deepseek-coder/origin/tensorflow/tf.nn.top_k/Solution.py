import tensorflow as tf

def k_largest_entries(tensor, k):
    values, indices = tf.math.top_k(tensor, k=k, sorted=True)
    return values, indices

# Example usage:
# tensor = tf.constant([[1, 3, 2], [4, 6, 5]])
# k = 2
# values, indices = k_largest_entries(tensor, k)
# print("Values:", values.numpy())
# print("Indices:", indices.numpy())
