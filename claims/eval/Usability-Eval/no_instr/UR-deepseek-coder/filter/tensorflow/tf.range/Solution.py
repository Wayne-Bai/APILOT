import tensorflow as tf

# Define the start, end, and step size for the sequence
start = 0
end = 10
step = 1

# Create a sequence of numbers using TensorFlow's range function
sequence = tf.range(start, end, step)

# Print the sequence
print(sequence.numpy())
