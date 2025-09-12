
import tensorflow as tf

# Define a function to reverse variable length slices
def reverse_slices(inputs, starts, limits, strides, output_shape):
    reversed_slices = tf.raw_ops.ReverseSequence(input=inputs, seq_lengths=strides, seq_axis=0, batch_axis=1)
    return reversed_slices

# Example usage
inputs = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
starts = tf.constant([0, 1, 0])
limits = tf.constant([1, 2, 3])
strides = tf.constant([1, 1, 1])
output_shape = tf.constant([3, 3])

reversed_slices = reverse_slices(inputs, starts, limits, strides, output_shape)

print(reversed_slices)
