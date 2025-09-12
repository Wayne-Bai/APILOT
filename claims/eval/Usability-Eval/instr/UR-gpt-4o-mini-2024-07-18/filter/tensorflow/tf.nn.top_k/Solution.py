import tensorflow as tf

def find_k_largest(entries, k):
    values, indices = tf.nn.top_k(entries, k=k, sorted=True)
    return values, indices

# Example usage
entries = tf.random.uniform((3, 4, 5))  # A random tensor of shape (3, 4, 5)
k = 2
values, indices = find_k_largest(entries, k)

print("Values:", values.numpy())
print("Indices:", indices.numpy())
