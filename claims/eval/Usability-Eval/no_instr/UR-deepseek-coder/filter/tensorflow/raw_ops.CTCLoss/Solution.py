import tensorflow as tf

def ctc_loss(labels, logits, label_length, logit_length, blank_index=0, log_probabilities=True):
    # Ensure the shapes are correct
    labels = tf.convert_to_tensor(labels, dtype=tf.int32)
    logits = tf.convert_to_tensor(logits, dtype=tf.float32)
    label_length = tf.convert_to_tensor(label_length, dtype=tf.int32)
    logit_length = tf.convert_to_tensor(logit_length, dtype=tf.int32)

    # Calculate the CTC loss
    loss = tf.nn.ctc_loss(
        labels=labels,
        logits=logits,
        label_length=label_length,
        logit_length=logit_length,
        blank_index=blank_index,
        log_probabilities=log_probabilities
    )

    return loss

# Example usage:
# labels = ...
# logits = ...
# label_length = ...
# logit_length = ...
# loss = ctc_loss(labels, logits, label_length, logit_length)
