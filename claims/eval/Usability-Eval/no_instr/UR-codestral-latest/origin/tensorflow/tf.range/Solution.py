import tensorflow as tf

# Start value of the sequence
start = 1

# End value of the sequence
end = 10

# Create a sequence of numbers
sequence = tf.range(start, end + 1)

# Print the sequence
print(sequence)
