import tensorflow as tf

# Define the start and end of the sequence
start = 0
end = 10

# Create a sequence of numbers using TensorFlow's range function
sequence = tf.range(start, end)

# Print the sequence
print(sequence.numpy())
