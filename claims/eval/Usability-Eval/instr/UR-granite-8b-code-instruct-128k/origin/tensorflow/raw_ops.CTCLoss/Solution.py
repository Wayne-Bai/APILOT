import tensorflow as tf

# Define the inputs
logits = tf.constant([[10., 0., 0.], [0., 10., 0.], [0., 0., 10.]])
labels = tf.constant([[1, 2], [2, 1], [2, 1]])
logit_length = tf.constant([3, 2, 2])
label_length = tf.constant([2, 1, 1])

# Calculate the CTC Loss
ctc_loss = tf.raw_ops.CTCLoss(
    logits=logits,
    labels=labels,
    logit_length=logit_length,
    label_length=label_length,
    blank_index=0
)

# Print the result
print(ctc_loss)
