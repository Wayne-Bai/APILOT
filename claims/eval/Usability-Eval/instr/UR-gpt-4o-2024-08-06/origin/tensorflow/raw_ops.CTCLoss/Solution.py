import tensorflow as tf

# Define the function to calculate CTC Loss
def calculate_ctc_loss(logits, labels, label_lengths, logit_lengths):
    """
    Compute the CTC Loss for a batch.

    Parameters:
    logits: 3-D tensor of shape (max_time, batch_size, num_classes), representing the unnormalized log probabilities.
    labels: SparseTensor, representing the target sequences.
    label_lengths: 1-D tensor of shape (batch_size), representing the lengths of the label sequences.
    logit_lengths: 1-D tensor of shape (batch_size), representing the lengths of the logit sequences.

    Returns:
    A 1-D tensor of shape (batch_size), representing the CTC loss for each sequence.
    """
    # Use the CTC Loss function provided by TensorFlow
    ctc_loss = tf.nn.ctc_loss(
        labels=labels,
        logits=logits,
        label_length=label_lengths,
        logit_length=logit_lengths,
        logits_time_major=True,
        blank_index=-1
    )

    return ctc_loss

# Example usage
batch_size = 2
max_time_steps = 10
num_classes = 20  # includes the blank label

# Simulated logits with random data for illustration purposes
logits = tf.random.uniform((max_time_steps, batch_size, num_classes), minval=-2.0, maxval=2.0)

# Example labels as a SparseTensor
indices = tf.constant([[0, 0], [1, 0], [1, 1]], dtype=tf.int64)
values = tf.constant([3, 6, 9], dtype=tf.int32)
shape = tf.constant([batch_size, max_time_steps], dtype=tf.int64)
labels = tf.sparse.SparseTensor(indices, values, shape)

# Example lengths
label_lengths = tf.constant([1, 2], dtype=tf.int32)
logit_lengths = tf.constant([8, 10], dtype=tf.int32)

# Calculate the CTC Loss
ctc_loss_values = calculate_ctc_loss(logits, labels, label_lengths, logit_lengths)

# Run a session to evaluate the loss (only needed in TF1.x, skipped in TF2.x due to eager execution)
print("CTC Loss values for each sequence:", ctc_loss_values.numpy())
