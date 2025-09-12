import tensorflow as tf

def find_top_k_values_and_indices(tensor, k):
    values, indices = tf.math.top_k(tensor, k=k)
    return values, indices

# Example usage
example_tensor = tf.constant([[1.2, 3.4, 5.6], [7.8, 6.5, 4.3]])
k = 2
values, indices = find_top_k_values_and_indices(example_tensor, k)
print("Values:", values.numpy())
print("Indices:", indices.numpy())
