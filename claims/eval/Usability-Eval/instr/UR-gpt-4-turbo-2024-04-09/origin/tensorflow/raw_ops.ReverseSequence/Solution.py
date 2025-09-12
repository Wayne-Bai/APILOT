import tensorflow as tf

# Create a tensor
data = tf.constant([[1, 2, 3, 4, 0], [5, 6, 7, 0, 0], [8, 9, 0, 0, 0]])

# Reverse variable-length slices
# seq_lengths specifies the length of the sequence in each vector to reverse
seq_lengths = [4, 3, 2]
output = tf.reverse_sequence(data, seq_lengths, seq_axis=1, batch_axis=0)

# To execute and see the result in TensorFlow 2.x, we will use a session in eager mode:
print(output.numpy())
