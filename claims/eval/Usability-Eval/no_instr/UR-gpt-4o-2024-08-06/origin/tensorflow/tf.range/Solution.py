import tensorflow as tf

# Create a sequence of numbers using TensorFlow
# Start at a specified value, end before another value with a step
start = 0
limit = 10
delta = 1

# The tf.range function creates a sequence of numbers
sequence = tf.range(start, limit, delta)

# Print the sequence
print("Sequence of numbers:", sequence.numpy())
