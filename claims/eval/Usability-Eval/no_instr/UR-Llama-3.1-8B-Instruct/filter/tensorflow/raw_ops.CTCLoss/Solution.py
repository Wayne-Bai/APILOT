import tensorflow as tf

# Define input tensors
logits = tf.random.normal([1, 10, 15])  # (batch size, sequence length, alphabet size)
labels = tf.random.uniform([10], minval=0, maxval=5, dtype=tf.int32)  # (sequence length)
label_lengths = tf.fill([10], 3)  # (sequence length)

# Define blank label (usually 0)
blank_label = 0
blank_calibration = tf.constant([1.0], dtype=tf.float32)  # calibration for blank (usually 1.0)

# Perform CTC loss calculation
ctc_loss, normalized_loss = tf.compat.v1.Checkpoint(lambda logits, labels, label_lengths, blank_label, blank_calibration: 
    tf.raw_ops.CtcGradient(
        logit_offset=logits,
        label=labels,
        label_lengths=label_lengths,
        blank_label=blank_label,
        scrape_op=tf.raw_ops.CtcOutput(
            logit_offset=logits, blank_calibration=blank_calibration
        ).src,
        batch_size_multiplier=tf.shape(logits)[0],
        name="CTCGradient[batch_multiplier]"
    )).logits, logits

# Print result
print(ctc_loss)
