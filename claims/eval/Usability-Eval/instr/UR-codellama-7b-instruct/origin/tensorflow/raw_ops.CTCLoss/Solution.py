import tensorflow as tf

def calculate_ctc_loss(labels, logits, sequence_length):
    """
    Calculates the CTC loss (log probability) for each batch entry.
    
    Args:
        labels: A tensor of shape `[batch_size, max_time, num_classes]`. The labels.
        logits: A tensor of shape `[batch_size, max_time, num_classes]`. The logits.
        sequence_length: A tensor of shape `[batch_size]`, containing the length of each sequence in `labels`.
    
    Returns:
        A tensor of shape `[batch_size]`, containing the CTC loss for each batch entry.
    """
    # Calculate the CTC loss using `tf.raw_ops.CTCLoss`:
    ctc_loss = tf.nn.ctc_loss(labels, logits, sequence_length)
    
    # Convert the CTC loss to log probability:
    log_probability = tf.math.log(tf.exp(ctc_loss))
    
    return log_probability