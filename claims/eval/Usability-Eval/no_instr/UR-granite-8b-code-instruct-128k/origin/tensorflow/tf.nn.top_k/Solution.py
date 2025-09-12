import tensorflow as tf

# Create a random tensor
tensor = tf.random.normal((3, 3, 3))

# Flatten the last dimension
tensor_reshaped = tf.reshape(tensor, (-1, 3))

# Find the k largest values and indices
k = 2
values, indices = tf.math.top_k(tensor_reshaped, k=k)

# Reshape the values and indices back to the original shape
values_reshaped = tf.reshape(values, (3, 3, k))
indices_reshaped = tf.reshape(indices, (3, 3, k))

# Print the results
print("Values:")
print(values_reshaped)
print("Indices:")
print(indices_reshaped)
