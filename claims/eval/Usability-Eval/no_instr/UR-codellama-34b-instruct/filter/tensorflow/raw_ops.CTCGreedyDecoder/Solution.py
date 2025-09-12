import tensorflow as tf

# Load the logits and input sequences
logits = ...
input_seq = ...

# Perform greedy decoding
decoded_sequence, _ = tf.nn.ctc_greedy_decoder(
    inputs=tf.transpose(logits, perm=[1, 0, 2]),
    sequence_length=input_seq.shape[0],
    merge_repeated=True)

# Print the decoded sequence
print("Decoded Sequence:", decoded_sequence)
