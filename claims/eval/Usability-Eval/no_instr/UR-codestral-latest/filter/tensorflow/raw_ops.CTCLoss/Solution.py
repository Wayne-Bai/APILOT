import tensorflow as tf

# Define a function to calculate CTC Loss

def ctc_loss(logits, labels, label_lengths, logit_lengths):
    """Calculate CTC Loss.

    Args:
        logits: Tensor of shape [batch_size, max_time, num_classes] containing the logits.
        labels: Tensor of shape [batch_size, max_label_length] containing the labels.
        label_lengths: Tensor of shape [batch_size] containing the lengths of the labels.
        logit_lengths: Tensor of shape [batch_size] containing the lengths of the logits.

    Returns:
        loss: A scalar tensor containing the average CTC Loss over the batch.
    """
    # Ensure that shapes and types of all inputs are accurate
    logits = tf.convert_to_tensor(logits, dtype=tf.float32)
    labels = tf.convert_to_tensor(labels, dtype=tf.int32)
    label_lengths = tf.convert_to_tensor(label_lengths, dtype=tf.int32)
    logit_lengths = tf.convert_to_tensor(logit_lengths, dtype=tf.int32)

    # Calculate CTC Loss
    loss = tf.nn.ctc_loss(
        labels=labels,
        logits=logits,
        label_length=label_lengths,
        logit_length=logit_lengths,
        logits_time_major=False,
        blank_index=-1)

    # Calculate mean loss over batch
    mean_loss = tf.reduce_mean(loss)

    return mean_loss
