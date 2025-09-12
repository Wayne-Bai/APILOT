import tensorflow as tf

# Create a sequence of numbers using TensorFlow
start = 0  # Starting number of the sequence
limit = 10  # Limit to end the sequence (exclusive)
delta = 1  # Step size between numbers

# Use tf.range to create the sequence
sequence = tf.range(start=start, limit=limit, delta=delta)

# Convert to a numpy array for easy display (optional)
print("Sequence of numbers: ", sequence.numpy())
