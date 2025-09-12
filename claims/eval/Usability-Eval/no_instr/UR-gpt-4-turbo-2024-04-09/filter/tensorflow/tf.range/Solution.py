import tensorflow as tf

# Creating a sequence of numbers using TensorFlow
def create_sequence(start, limit, delta):
    return tf.range(start, limit, delta)

# Example usage
sequence = create_sequence(0, 10, 1)
print(sequence.numpy())
