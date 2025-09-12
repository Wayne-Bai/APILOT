import tensorflow as tf

def compute_ctc_loss(logits, labels, label_length, logit_length):
    """
    Computes the CTC loss using TensorFlow.

    Parameters:
    logits: A 3-D float Tensor of shape [max_time, batch_size, num_classes].
    labels: A 2-D int Tensor of shape [batch_size, max_label_length].
    label_length: A 1-D int Tensor of shape [batch_size].
    logit_length: A 1-D int Tensor of shape [batch_size].

    Returns:
    ctc_loss: A 1-D Tensor with the CTC losses for each sequence in the batch.
    """

    ctc_loss = tf.nn.ctc_loss(
        labels=labels,
        logits=logits,
        label_length=label_length,
        logit_length=logit_length,
        ignore_longer_outputs_than_inputs=True
    )
    return ctc_loss

# Example usage
if __name__ == "__main__":
    # Define the parameters
    max_time = 10
    batch_size = 2
    num_classes = 5
    max_label_length = 5

    # Create dummy data
    logits = tf.random.uniform((max_time, batch_size, num_classes), minval=0, maxval=1, dtype=tf.float32)
    labels = tf.constant([[1, 2, 3, 4, 0], [0, 1, 2, 0, 0]], dtype=tf.int32)
    label_length = tf.constant([4, 3], dtype=tf.int32)
    logit_length = tf.constant([max_time] * batch_size, dtype=tf.int32)

    # Compute CTC loss
    loss = compute_ctc_loss(logits, labels, label_length, logit_length)
    print("CTC Loss:", loss.numpy())
