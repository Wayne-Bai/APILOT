
import tensorflow as tf

# Define the starting number and the length of the sequence
start = tf.constant(0)
length = tf.constant(10)

# Create the sequence of numbers
sequence = start + length

# Print the sequence
print(sequence)
