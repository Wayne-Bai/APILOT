import tensorflow as tf

# Create a sequence of numbers
def create_sequence(start, stop, step):
    return tf.range(start, stop, step)

# Example usage
sequence = create_sequence(0, 10, 2)
print(sequence.numpy())
