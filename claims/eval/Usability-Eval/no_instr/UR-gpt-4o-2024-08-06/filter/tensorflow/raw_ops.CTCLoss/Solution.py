import tensorflow as tf

def calculate_ctc_loss(logits, labels, label_lengths, logit_lengths):
    """
    Calculate the CTC Loss using TensorFlow 2.x functionalities.

    Args:
        logits (tf.Tensor): The logits output from the last layer of the model. 
                            Shape should be [batch_size, max_time, num_classes].
        labels (tf.SparseTensor): Sparse tensor containing the labels for each input.
        label_lengths (tf.Tensor): Lengths of each label.
        logit_lengths (tf.Tensor): Lengths of each logit sequence.

    Returns:
        ctc_loss (tf.Tensor): The calculated CTC loss.
    """

    # Calculate CTC loss
    ctc_loss = tf.nn.ctc_loss(
        labels=labels,
        logits=logits,
        label_length=label_lengths,
        logit_length=logit_lengths,
        logits_time_major=False,  # Set to False as logits are batch major
        blank_index=-1  # Use the last class as the blank label
    )

    return ctc_loss

# Example usage
if __name__ == "__main__":
    batch_size = 2
    max_time = 10
    num_classes = 5  # Including the CTC blank token
    max_label_length = 8

    # Example logits [batch_size, max_time, num_classes]
    logits = tf.random.uniform((batch_size, max_time, num_classes), minval=-1.0, maxval=1.0)

    # Example sparse labels
    indices = tf.constant([[0, 0], [1, 0], [1, 1]], dtype=tf.int64)
    values = tf.constant([1, 2, 3], dtype=tf.int32)
    dense_shape = tf.constant([batch_size, max_label_length], dtype=tf.int64)

    labels = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)
    labels = tf.sparse.reorder(labels)

    # Lengths of each label
    label_lengths = tf.constant([1, 2], dtype=tf.int32)  # Example values
    
    # Lengths of each logit sequence
    logit_lengths = tf.constant([max_time, max_time], dtype=tf.int32)

    # Calculate CTC loss
    ctc_loss = calculate_ctc_loss(logits, labels, label_lengths, logit_lengths)
    print("CTC Loss:", ctc_loss.numpy())
