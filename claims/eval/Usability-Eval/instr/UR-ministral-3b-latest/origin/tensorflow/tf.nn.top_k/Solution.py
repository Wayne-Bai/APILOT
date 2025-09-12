import tensorflow as tf

def top_k(values, k):
    # Find the k largest values and their indices along the last dimension
    k_values, k_indices = tf.math.top_k(values, k)
    return k_values, k_indices

# Test the function
values = tf.constant([[1, 2, 3], [4, 5, 6]])
k = 2

top_k_values, top_k_indices = top_k(values, k)
print("Top k values:", top_k_values)
print("Top k indices:", top_k_indices)
