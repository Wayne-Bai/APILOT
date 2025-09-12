import tensorflow as tf

# Function to create a sequence of numbers starting from 'start' up to but not including 'stop' with a step of 'step'
def create_sequence(start, stop, step):
    return tf.range(start, stop, step)

# Example usage
sequence = create_sequence(0, 10, 1)
print("Sequence of numbers:", sequence.numpy())
