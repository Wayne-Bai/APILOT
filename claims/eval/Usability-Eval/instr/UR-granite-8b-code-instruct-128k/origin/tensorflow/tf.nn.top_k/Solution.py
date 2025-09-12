
import tensorflow as tf

# Create a random tensor
tensor = tf.random.normal([3, 4, 5])

# Define the value of k
k = 2

# Use the tf.math.top_k function to find the values and indices of the k largest entries for the last dimension
values, indices = tf.math.top_k(tensor, k=k, sorted=True)

# Print the results
print("Values:")
print(values)
print("Indices:")
print(indices)
