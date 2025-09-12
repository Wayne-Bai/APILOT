import tensorflow as tf

# Define the CTC loss function
def ctc_loss(labels, logits, input_lengths, output_lengths):
    # Calculate the CTC loss for each batch entry
    ctc_loss_values = tf.raw_ops.CTCLoss(
        labels=labels,
        logits=logits,
        input_lengths=input_lengths,
        output_lengths=output_lengths,
        beam_width=1,
        top_path=True,
        output_time_major=False
    )

    # Return the average CTC loss
    return tf.reduce_mean(ctc_loss_values)
