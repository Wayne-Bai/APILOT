
import tensorflow as tf

# Define function to reverse variable length slices
def reverse_slices(input_data, sequence_length, name=None):
    return tf.raw_ops.ReverseSequence(input=input_data, seq_lengths=sequence_length, seq_axis=1, batch_dim=0, time_dim=1, name=name)
