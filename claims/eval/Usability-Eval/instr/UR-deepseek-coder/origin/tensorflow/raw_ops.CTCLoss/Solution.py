import tensorflow as tf

def ctc_loss(labels, logits, label_length, logit_length, blank_index=0, log_probs=True):
    # Calculate the log probabilities
    if log_probs:
        log_probs = logits
    else:
        log_probs = tf.nn.log_softmax(logits)

    # Transpose log_probs to match the expected shape for CTC loss
    log_probs_t = tf.transpose(log_probs, (1, 0, 2))

    # Compute the CTC loss
    loss = tf.nn.ctc_loss(
        labels=labels,
        logits=log_probs_t,
        label_length=label_length,
        logit_length=logit_length,
        blank_index=blank_index,
        log_probs=True
    )

    return loss

# Example usage:
# labels = ...  # shape (batch_size, max_label_length)
# logits = ...  # shape (max_time_steps, batch_size, num_classes)
# label_length = ...  # shape (batch_size,)
# logit_length = ...  # shape (batch_size,)

# loss = ctc_loss(labels, logits, label_length, logit_length)
# print(loss)
