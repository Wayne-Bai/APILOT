# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a sequence of numbers
def create_sequence(start, stop, step):
    # Use tf.range to create a sequence of numbers
    sequence = tf.range(start, stop, step)
    return sequence

# Define the start, stop, and step values
start_value = 1
stop_value = 10
step_value = 2

# Create a sequence of numbers
sequence = create_sequence(start_value, stop_value, step_value)

# Print the sequence
print("Sequence:", sequence.numpy())

# Get the last element from the sequence
last_element = sequence.numpy()[-1]

# Print the last element
print("Last Element:", last_element)

# Get all even numbers from the sequence
even_numbers = [num for num in sequence.numpy() if num % 2 == 0]

# Print the even numbers
print("Even Numbers:", even_numbers)

# Get the sum of all elements in the sequence
sequence_sum = np.sum(sequence.numpy())

# Print the sum
print("Sum:", sequence_sum)
