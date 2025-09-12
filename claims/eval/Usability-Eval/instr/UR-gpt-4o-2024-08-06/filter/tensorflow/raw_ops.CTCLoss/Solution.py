import tensorflow as tf

# Function to calculate CTC Loss for a batch of sequences
def compute_ctc_loss(logits, labels, input_lengths, label_lengths):
    """
    Computes the CTC Loss.

    :param logits: 3D tensor of shape [max_time, batch_size, num_classes], the
                   predicted logits
    :param labels: 2D tensor of shape [batch_size, max_labels_length] containing
                   the sequences of labels
    :param input_lengths: 1D tensor of shape [batch_size] indicating the lengths
                          of the input sequences in the batch
    :param label_lengths: 1D tensor of shape [batch_size] indicating the lengths
                          of the label sequences in the batch
    :return: 1D tensor of shape [batch_size] containing the CTC loss for each
             sequence in the batch
    """
    # Use tf.nn.ctc_loss to compute the CTC Loss
    loss = tf.nn.ctc_loss(
        labels=labels,
        logits=logits,
        label_length=label_lengths,
        logit_length=input_lengths,
        logits_time_major=True,
        blank_index=-1
    )
    
    return loss

# Example usage
if __name__ == "__main__":
    # Define parameters for the example
    batch_size = 2
    max_time = 10
    num_classes = 20
    max_labels_length = 5

    # Randomly generate logits
    logits = tf.random.uniform((max_time, batch_size, num_classes), dtype=tf.float32)

    # Dummy data for labels, input_lengths, and label_lengths
    labels = tf.constant([[1, 2, 3, 4, 0], [3, 4, 5, 0, 0]], dtype=tf.int32)
    input_lengths = tf.constant([10, 10], dtype=tf.int32)
    label_lengths = tf.constant([4, 3], dtype=tf.int32)

    # Compute CTC Loss
    ctc_loss = compute_ctc_loss(logits, labels, input_lengths, label_lengths)
    print("CTC Loss:", ctc_loss.numpy())
