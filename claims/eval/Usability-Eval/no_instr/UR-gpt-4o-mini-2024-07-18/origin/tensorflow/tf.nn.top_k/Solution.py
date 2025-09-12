import tensorflow as tf

def k_largest_entries(input_tensor, k):
    values, indices = tf.math.top_k(input_tensor, k=k, sorted=True)
    return values, indices

# Example usage
input_tensor = tf.constant([[1, 5, 3], [9, 2, 4], [7, 8, 6]])
k = 2
values, indices = k_largest_entries(input_tensor, k)
print("Values:", values.numpy())
print("Indices:", indices.numpy())
