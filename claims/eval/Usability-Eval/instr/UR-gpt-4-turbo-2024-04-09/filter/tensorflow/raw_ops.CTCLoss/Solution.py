import tensorflow as tf

def compute_ctc_loss(labels, logits, label_length, logit_length):
    """
    Compute the CTC (Connectionist Temporal Classification) loss.

    Args:
    labels : Tensor of shape [batch_size, max_label_seq_length]
        Contains the labels (targets) of a batch.
    logits : Tensor of shape [max_time, batch_size, num_classes]
        The raw output of the network, which represents the 
        log probabilities of the various classes over time.
    label_length : Tensor of shape [batch_size]
        Contains the length of the label sequences for each sample in the batch.
    logit_length : Tensor of shape [batch_size]
        Contains the length of the logits sequences for each sample in the batch.

    Returns:
    Tensor scalar, the average CTC loss across the batch.
    """
    ctc_loss = tf.nn.ctc_loss(
        labels=labels,
        logits=logits,
        label_length=label_length,
        logit_length=logit_length,
        logits_time_major=True,  # Because logits is of shape [max_time, batch_size, num_classes]
        blank_index=-1  # Default is the last class
    )
    
    # Calculate the mean loss
    loss = tf.reduce_mean(ctc_loss)
    
    return loss

# Example usage:
# Preparing dummy data
batch_size = 4
max_label_length = 5
max_time = 10
num_classes = 20  # Including the blank for CTC

labels = tf.constant([[2, 3, 4, -1, -1], [1, 2, 2, 1, -1], [3, 4, 5, 1, 0], [2, 0, 0, -1, -1]], dtype=tf.int32)
logits = tf.random.normal([max_time, batch_size, num_classes])
label_length = tf.constant([3, 4, 5, 2], dtype=tf.int32)
logit_length = tf.constant([10, 10, 10, 10], dtype=tf.int32)

# Compute the loss
loss = compute_ctc_loss(labels, logits, label_length, logit_length)
print("CTC Loss:", loss.numpy())
