import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Use the reverse_sequence function from tf.raw_ops
# This will reverse the sequence and return a tensor
reversed_tensor = tf.raw_ops.ReverseSequence(
    input=tensor,
    seq_lengths=[len(tensor)],  # length of the sequence
    seq_axis=0,  # axis along which to reverse
    batch_axis=0  # axis of the batch
)

# Or, you can use tf.reverse_sequence function
# This function wraps the tf.raw_ops.ReverseSequence function
reversed_tensor = tf.reverse_sequence(
    input=tensor,
    seq_lengths=[len(tensor)],
    seq_axis=0,
    batch_axis=0
)

# Print the original and reversed tensor
with tf.Session() as sess:
    print("Original tensor: ", tensor.eval())
    print("Reversed tensor: ", reversed_tensor.eval())
