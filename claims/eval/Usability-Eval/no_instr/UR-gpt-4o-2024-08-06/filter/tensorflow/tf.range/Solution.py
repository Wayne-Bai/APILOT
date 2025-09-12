import tensorflow as tf

# Create a sequence of numbers from start to end with a given step size using tf.range
start = 0
end = 10
step = 2
sequence = tf.range(start, end, step)

# Start a TensorFlow session to compute the sequence
tf.print("Sequence:", sequence)
