import tensorflow as tf

def greedy_decode(logits, start_token, end_token, max_length):
    """
    Performs greedy decoding on the given logits.

    Args:
        logits: A tensor of shape [batch_size, sequence_length, num_classes].
        start_token: The token to start decoding from.
        end_token: The token to end decoding.
        max_length: The maximum length of the decoded sequence.

    Returns:
        A tensor of shape [batch_size, max_length] containing the decoded sequences.
    """
    batch_size = tf.shape(logits)[0]
    decoded = tf.fill([batch_size, 1], start_token)
    
    for _ in range(max_length - 1):
        last_token = decoded[:, -1]
        logits_at_last_token = tf.gather(logits, last_token)

        predicted_token = tf.argmax(logits_at_last_token, axis=-1, output_type=tf.int32)
        predicted_token = tf.expand_dims(predicted_token, axis=1)

        decoded = tf.concat([decoded, predicted_token], axis=1)

        # Exit if all sequences reached the end token
        if tf.reduce_sum(tf.cast(decoded[:, -1] == end_token, tf.int32)) == batch_size:
            break
    
    return decoded

# Example usage
logits = tf.random.uniform((2, 10, 5))  # Example logits
start_token = 1
end_token = 2
max_length = 10

decoded_sequences = greedy_decode(logits, start_token, end_token, max_length)
print(decoded_sequences)
