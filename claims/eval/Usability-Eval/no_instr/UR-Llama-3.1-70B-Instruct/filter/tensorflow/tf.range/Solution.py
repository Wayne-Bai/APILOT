import tensorflow as tf

# Creates a sequence of numbers
# starting from 1, incrementing by 1, ending before 10
sequence = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Sequence of numbers:")
print(sequence)

# Using tf.linspace for a sequence of numbers
start = 1.0
stop = 10.0
num = 10
sequence琳 = tf.linspace(start, stop, num)

print("\nSequence of numbers using linspace:")
print(sequence_lin)

# Using tf.concat for creating sequence
sequence_concat = tf.concat([tf.constant([1, 2, 3]), tf.constant([4, 5, 6]), tf.constant([7, 8, 9])], 0)

print("\nSequence of numbers using concat:")
print(sequence_concat)
