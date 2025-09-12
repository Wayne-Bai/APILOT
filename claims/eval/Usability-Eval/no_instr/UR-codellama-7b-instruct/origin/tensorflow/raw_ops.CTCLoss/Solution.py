
import tensorflow as tf

def ctc_loss(labels, inputs, label_lengths, input_lengths):
    """
    Calculates the CTC Loss (log probability) for each batch entry.

    Args:
        labels: A Tensor of shape [B, max_time] containing the target labels for each batch entry.
        inputs: A Tensor of shape [B, max_time, num_classes] containing the logits for each batch entry.
        label_lengths: A Tensor of shape [B] containing the length of each label in the target sequence.
        input_lengths: A Tensor of shape [B] containing the length of each input sequence.

    Returns:
        A Tensor of shape [B, 1] containing the CTC loss for each batch entry.
    """
    labels = tf.reshape(labels, [-1])
    inputs = tf.reshape(inputs, [-1, inputs.shape[-1]])
    label_lengths = tf.reshape(label_lengths, [-1])
    input_lengths = tf.reshape(input_lengths, [-1])

    ctc_losses = tf.nn.ctc_loss(labels=labels, inputs=inputs, label_lengths=label_lengths, input_lengths=input_lengths)

    return tf.reshape(ctc_losses, [-1])
