# Import the tensorflow library
import tensorflow as tf

# Create a sequence of numbers from 0 to 10 with a delta of 2
sequence = tf.range(0, 10, delta=2)

# Print the sequence
print(sequence)

# Create a sequence of numbers from 10 to 0 with a delta of -2
sequence_reversed = tf.range(10, 0, delta=-2)

# Print the reversed sequence
print(sequence_reversed)
