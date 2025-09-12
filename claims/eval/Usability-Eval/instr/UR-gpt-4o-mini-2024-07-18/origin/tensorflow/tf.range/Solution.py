import tensorflow as tf

# Create a sequence of numbers using tf.range
start = 0
limit = 10
delta = 1
sequence = tf.range(start, limit, delta)

print(sequence.numpy())
