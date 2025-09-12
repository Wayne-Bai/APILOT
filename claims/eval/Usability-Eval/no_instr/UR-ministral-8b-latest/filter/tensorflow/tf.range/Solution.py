import tensorflow as tf

# Create a sequence of numbers using tf.range
sequence = tf.range(10, 100, 5)
print(sequence.numpy)
