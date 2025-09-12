import tensorflow as tf

def calculate_ctc_loss(inputs, labels):
    # Create a CTC loss function
    ctc_loss = tf.keras.losses.CTCLoss(reduction=tf.keras.losses.Reduction.NONE)

    # Calculate the CTC loss for each batch entry
    ctc_losses = ctc_loss(labels, inputs)

    return ctc_losses
