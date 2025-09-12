import tensorflow as tf

# Define the logits
logits = tf.constant([[0.2, 0.7, 0.1], [0.1, 0.3, 0.6]])

# Perform greedy decoding on the logits
decoded_indices, decoded_values, decoded_shape = tf.raw_ops.CTCGreedyDecoder(
    inputs=logits,
    sequence_length=[2, 2]
)

# Print the decoded values
print(decoded_values)
