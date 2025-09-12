
import tensorflow as tf

# Define a tensor to work with
tensor = tf.random.normal(shape=(3, 4))

# Find the values and indices of the top 2 entries for the last dimension
values, indices = tf.nn.top_k(tensor, k=2, sorted=True)

# Print the results
print("Values:", values)
print("Indices:", indices)
