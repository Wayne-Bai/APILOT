import tensorflow as tf

# Defining the start and end of the sequence
start = 0
end = 10

# Creating the sequence of numbers
sequence = tf.range(start, end)

# Printing the sequence
print(sequence)
