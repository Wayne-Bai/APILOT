import tensorflow as tf

def greedy_decoding(logits, start_token, end_token, max_length):
    """
    Performs greedy decoding on the logits.

    Parameters:
    logits: A tensor of shape [batch_size, max_time, vocab_size] containing the logits.
    start_token: The token to start decoding from.
    end_token: The token indicating the end of decoding.
    max_length: The maximum length of the decoded sequence.

    Returns:
    A tensor containing the decoded sequences.
    """
    batch_size = tf.shape(logits)[0]
    vocab_size = tf.shape(logits)[-1]

    # Start with the start token
    decoded_ids = tf.fill([batch_size, 1], start_token)

    for _ in range(max_length):
        # Get the last predicted token logits
        latest_logits = logits[:, tf.shape(decoded_ids)[1] - 1, :]
        # Get the next token as the argmax of the logits
        next_ids = tf.argmax(latest_logits, axis=-1, output_type=tf.int32)
        next_ids = tf.expand_dims(next_ids, axis=1)

        # Append the predicted token to the decoded sequences
        decoded_ids = tf.concat([decoded_ids, next_ids], axis=1)

        # Check if we have reached the end token
        if tf.reduce_all(tf.equal(next_ids, end_token)):
            break

    return decoded_ids
