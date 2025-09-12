import tensorflow as tf

def create_sequence(start, limit, delta):
    return tf.range(start, limit, delta)

# Example usage: Create a sequence starting from 0 to 10 with a step of 2
sequence = create_sequence(0, 10, 2)
print(sequence.numpy())  # Output: [0 2 4 6 8]
