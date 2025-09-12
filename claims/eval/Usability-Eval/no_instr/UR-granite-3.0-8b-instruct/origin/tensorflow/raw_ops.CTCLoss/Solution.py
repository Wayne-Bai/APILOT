import tensorflow as tf

# Assuming 'logits' is the output of your model and 'labels' is the target labels
def calculate_ctc_loss(logits, labels, label_lengths):
    # Calculate the CTC loss using tf.raw_ops.CTCLoss
    ctc_loss = tf.raw_ops.CTCLoss(
        inputs=logits,
        labels=labels,
        label_lengths=label_lengths,
        input_lengths=tf.ones_like(labels) * tf.shape(logits)[1],
        blank_index=0,  # Assuming blank index is 0
        blank_index_mask=True,
        time_major=False,
        return_detailed_loss=True
    )

    # The CTC loss is the first element of the returned tuple
    ctc_loss = ctc_loss[0]

    return ctc_loss
