# Importing the necessary libraries
import tensorflow as tf

# Creating a sequence of numbers from 0 to 100 with a step of 2
sequence = tf.range(0, 100, delta=2)

# Printing the sequence
print(sequence)
