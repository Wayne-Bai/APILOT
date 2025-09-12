import tensorflow as tf

def greedy_decoder(logits, max_length):
    """
    Performs greedy decoding on the logits given in inputs.

    Args:
        logits: A 2D Tensor of shape [batch_size, num_classes] containing the logits.
        max_length: An integer specifying the maximum length of the output sequence.

    Returns:
        A 2D Tensor of shape [batch_size, max_length] containing the decoded sequences.
    """
    batch_size = tf.shape(logits)[0]
    num_classes = tf.shape(logits)[1]

    # Initialize the output tensor with zeros
    output = tf.zeros([batch_size, max_length], dtype=tf.int32)

    # Iterate over each time step
    for t in range(max_length):
        # Get the logits for the current time step
        logits_t = logits[:, t]

        # Get the index of the maximum value in the logits
        indices = tf.argmax(logits_t, axis=1)

        # Store the indices in the output tensor
        output[:, t] = indices

        # Update the logits by setting the values at the selected indices to -inf
        logits = tf.where(tf.equal(logits, tf.reduce_max(logits, axis=1, keepdims=True)), -tf.math.inf, logits)

    return output
