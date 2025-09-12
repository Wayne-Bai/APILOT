# Importing necessary libraries
import tensorflow as tf
import numpy as np

# Creating a sequence of numbers
sequence_length = 10  # You can change this to any length you want
sequence = tf.range(sequence_length, dtype=tf.int32)

# Print the sequence
print("Sequence of numbers: ")
print(sequence)

# Generator function to create a sequence of numbers
def create_sequence(start, stop, step=1):
    return tf.create_tensor_proto(tf.range(start, stop, step))

# Testing the generator function
print("Sequence of numbers from 1 to 10: ")
print(create_sequence(1, 11))

# To create a sequence with a custom start and stop value
print("Sequence of numbers from 5 to 15: ")
print(create_sequence(5, 16))
