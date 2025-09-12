import tensorflow as tf

# Define the start, limit, and delta (step size) values
start = 0
limit = 10
delta = 1

# Use tf.range to generate a sequence of numbers from start to limit with the given delta
sequence = tf.range(start, limit, delta)

# Convert the Tensor to a NumPy array and print the sequence
print("Generated sequence:", sequence.numpy())
