# Import necessary libraries
import tensorflow as tf

# Create a sample variable (tensor)
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.int32)

# Define the batch dimension
batch_dim = 0

# Define the indices array
indices = tf.constant([0, 2])

# Use tf.gather to get the specified elements
result = tf.gather(tensor, indices)

# Print the result
print(result)

# Use tf.gather to get the specified elements with batch dimension
result_batch_dim = tf.gather(tensor, indices, batch_dims=batch_dim)

# Print the result with batch dimension
print(result_batch_dim)
