import tensorflow as tf

# Define a custom operation to reverse variable length slices
def reverse_slices(data, seq_lengths):
    # Create a sequence mask
    mask = tf.sequence_mask(seq_lengths, dtype=tf.bool)

    # Create a reversed sequence mask
    reversed_mask = tf.reverse_sequence(mask, seq_lengths, seq_dim=1)

    # Apply the reversed mask to the data
    reversed_data = tf.boolean_mask(data, reversed_mask)

    # Reshape the reversed data to match the original shape
    reversed_data = tf.reshape(reversed_data, tf.shape(data))

    return reversed_data
