import tensorflow as tf

# An example sequence of numbers
def generate_sequence(start, end, step):
    """Generate a sequence of numbers starting from 'start' and ending at 'end'."""
    seq = tf.range(start, end, step)
    return seq

# Example usage:
start = 1
end = 10
step = 2

sequence = generate_sequence(start, end, step)

with tf.Session() as sess:
    print(sess.run(sequence))
