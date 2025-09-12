
import tensorflow as tf

# Define the range of values to generate
start = 0
end = 10
step = 2

# Use the TensorFlow range function to create a sequence
sequence = tf.range(start, end, step)

# Print the sequence
print(sequence)
