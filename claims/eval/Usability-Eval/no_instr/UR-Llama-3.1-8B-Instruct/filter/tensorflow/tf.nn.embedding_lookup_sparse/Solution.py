import tensorflow as tf

# Define the embeddings tensors
# We assume we have multiple snippets of tensors with different levels of recall factors
# For demonstration purposes, we'll create three tensors with different sizes
tensor1 = tf.random.uniform([10, 5])  # Shape (10, 5)
tensor2 = tf.random.uniform([20, 5])  # Shape (20, 5)
tensor3 = tf.random.uniform([5, 5])  # Shape (5, 5)

# Stack the tensors to form the lookup table
lookup_table = tf.concat([tensor1, tensor2, tensor3], axis=0)

# Define the indices we want to look up
ids = tf.Variable([0, 5, 10])  # Look up three different snippets

# Define the weights for the lookups
weights = tf.Variable([1.0, 2.0, 3.0])  # Assign different weights for each lookup

# Look up the embeddings using the given ids and weights
embeddings = tf.gather(lookup_table, ids, axis=0) * tf.expand_dims(weights, axis=-1)

# Print the result
print(embeddings)
