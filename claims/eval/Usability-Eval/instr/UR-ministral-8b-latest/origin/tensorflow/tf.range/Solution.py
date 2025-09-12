import tensorflow as tf

# Create a sequence of numbers
sequence = tf.range(0, 10, dtype=tf.float32)

print(sequence.numpy())
