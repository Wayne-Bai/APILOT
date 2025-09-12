import tensorflow as tf

# Let's assume you have a batch of sequences (batch_size, seq_length, num_features)
# and a tensor with the actual length of each sequence (batch_size)
sequences = tf.random.normal([4, 10, 20]) # replace with your input
sequence_lengths = tf.constant([7, 5, 9, 10]) # replace with your sequence lengths

# Reverse each sequence along the sequence length axis
reversed_sequences = tf.reverse_sequence(sequences, sequence_lengths, seq_axis=1, batch_axis=0)
