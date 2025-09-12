import tensorflow as tf

# Assume logits is a Tensor of shape [batch_size, sequence_length, num_classes]
logits = ...

# Apply softmax to get probabilities
probabilities = tf.nn.softmax(logits, axis=-1)

# Use argmax to get the index of the highest probability (i.e., the "greedy" decoding)
decoded_sequences = tf.argmax(probabilities, axis=-1)

# Now, decoded_sequences is a Tensor of shape [batch_size, sequence_length]
# containing the decoded sequences for each example in the batch
