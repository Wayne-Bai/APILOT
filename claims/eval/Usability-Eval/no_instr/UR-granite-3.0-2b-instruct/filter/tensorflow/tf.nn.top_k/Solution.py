import tensorflow as tf

# Assuming 'x' is your input tensor and 'k' is the number of largest values you want to find
x = tf.constant([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
k = 3

# Find values and indices of the k largest entries for the last dimension
values, indices = tf.top_k(x, k=k, sorted=True)

# Print the results
print("Values:")
print(values)
print("\nIndices:")
print(indices)
