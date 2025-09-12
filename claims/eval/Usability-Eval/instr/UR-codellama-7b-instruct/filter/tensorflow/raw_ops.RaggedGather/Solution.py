import tensorflow as tf

# Create a sample dataset
data = [[1, 2], [3, 4], [5, 6]]

# Set up indices for gathering ragged slices
indices = [[0], [1], [2]]

# Set up params tensor with the data
params = tf.constant(data)

# Gather ragged slices from params using indices
gathered_slices = tf.ragged.gather(params, indices)

print("Gathered slices:")
print(gathered_slices)
