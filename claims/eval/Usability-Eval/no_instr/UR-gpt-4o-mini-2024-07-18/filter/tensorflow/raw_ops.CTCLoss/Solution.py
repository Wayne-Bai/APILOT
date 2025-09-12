import tensorflow as tf

def compute_ctc_loss(logits, labels, label_lengths, logit_lengths):
    """
    Computes the CTC (Connectionist Temporal Classification) loss.

    Args:
        logits: 3D Tensor of shape [max_time, batch_size, num_classes] containing the predicted logits.
        labels: 2D Tensor of shape [batch_size, max_label_length] containing the true labels.
        label_lengths: 1D Tensor of shape [batch_size] containing the lengths of the true labels.
        logit_lengths: 1D Tensor of shape [batch_size] containing the lengths of the predicted logits.

    Returns:
        A 1D Tensor containing the CTC loss for each batch entry.
    """
    ctc_loss = tf.nn.ctc_loss(
        labels=labels,
        logits=logits,
        label_length=label_lengths,
        logit_length=logit_lengths,
        preprocess_collapse_repeated=True,
        time_major=True,
    )
    return ctc_loss

# Example usage
if __name__ == "__main__":
    batch_size = 2
    num_classes = 5
    max_time = 7
    max_label_length = 4

    # Creating dummy data
    logits = tf.random.uniform((max_time, batch_size, num_classes), dtype=tf.float32)
    labels = tf.constant([[1, 2, 3, -1], [1, 2, -1, -1]], dtype=tf.int32)  # -1 for padding
    label_lengths = tf.constant([3, 2], dtype=tf.int32)
    logit_lengths = tf.constant([max_time, max_time], dtype=tf.int32)

    # Compute CTC loss
    loss = compute_ctc_loss(logits, labels, label_lengths, logit_lengths)
    print("CTC Loss:", loss.numpy())
