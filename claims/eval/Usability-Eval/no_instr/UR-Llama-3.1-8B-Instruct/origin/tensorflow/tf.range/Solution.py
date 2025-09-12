# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a sequence of numbers from 0 to 9
sequence = tf.range(0, 10, dtype=tf.int32)

print("Sequence of numbers: ", sequence.numpy())
