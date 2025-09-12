import tensorflow as tf

def find_k_largest(input_tensor, k):
    # Find the k largest values and their indices along the last dimension
    values, indices = tf.math.top_k(input_tensor, k=k, sorted=True)
    return values, indices

# Example usage:
# input_tensor = tf.constant([[4, 1, 7, 3], [8, 2, 5, 6]])
# k = 2
# values, indices = find_k_largest(input_tensor, k)
# print("Values:", values.numpy())
# print("Indices:", indices.numpy())
