import tensorflow as tf

# Create a sequence of numbers
sequence = tf.range(start=1, limit=10, delta=1)

print('Sequence of numbers:', sequence.numpy())
