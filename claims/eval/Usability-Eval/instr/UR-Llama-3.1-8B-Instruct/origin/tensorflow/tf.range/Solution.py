# Import necessary libraries
import tensorflow as tf

# Create a sequence of numbers from 0 to 9
sequence = tf.range(start=0, limit=10, delta=1)

print("Sequence of numbers:")
print(sequence.numpy())
