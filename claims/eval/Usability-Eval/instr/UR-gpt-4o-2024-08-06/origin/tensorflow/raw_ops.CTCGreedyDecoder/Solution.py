import tensorflow as tf

def greedy_decode(logits):
    """
    Performs greedy decoding on the provided logits.
    
    Args:
    logits: A 3D tensor (batch_size, sequence_length, vocab_size) of logits.

    Returns:
    A 2D tensor (batch_size, sequence_length) containing the greedy decoded ids.
    """
    # For each sequence in the batch, the predicted class at each time step is the one
    # with the maximum logit value. We use tf.argmax to get the indices of the max values
    # along the last dimension (vocab_size).
    decoded_ids = tf.argmax(logits, axis=-1, output_type=tf.int32)

    return decoded_ids

# Example usage
# Consider a batch of 2 sequences, each with 5 time steps, and a vocabulary size of 10.
logits = tf.random.uniform(shape=(2, 5, 10), minval=-1.0, maxval=1.0)
decoded_sequences = greedy_decode(logits)

# Let's print the decoded sequences
print(decoded_sequences)
