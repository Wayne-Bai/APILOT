import tensorflow as tf

# Define the start and end of the sequence
start = 0
end = 10

# Create a sequence of numbers
sequence = tf.range(start, end + 1)

# Print the sequence
print(sequence.numpy())
