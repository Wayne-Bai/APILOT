import tensorflow as tf

def find_k_largest_entries(data, k):
    value, indices = tf.math.top_k(tf.reduce_sum(data, axis=-1), k)
    return value, indices

# Usage
data = tf.random.uniform((10, 3, 4))  # Example data with shape (samples, timesteps, features)
k = 2
largest_values, smallest_indices = find_k_largest_entries(data, k)
print("Largest Values:", largest_values)
print("Smallest Indices:", smallest_indices)
