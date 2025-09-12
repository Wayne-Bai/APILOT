import tensorflow as tf

# Define the inputs: logits, label lengths, and input lengths
logits = tf.constant([[[0.1, 0.2, 0.7], [0.9, 0.05, 0.05]],
                      [[0.2, 0.3, 0.5], [0.8, 0.1, 0.1]]], dtype=tf.float32)  # shape (batch_size, max_time, num_classes)

label_lengths = tf.constant([2, 1], dtype=tf.int32)  # Length of each label
input_lengths = tf.constant([2, 2], dtype=tf.int32)  # Length of the input in each batch

labels = tf.constant([[2, 1], [1, 0]], dtype=tf.int32)  # Labels: list of indices

# Calculate CTC Loss using preferred method
ctc_loss = tf.nn.ctc_loss(
    labels=labels,
    logits=logits,
    label_length=label_lengths,
    logit_length=input_lengths,
    logits_time_major=False,
    blank_index=2
)

# Create a TensorFlow session or use eager execution to evaluate the operation
print("CTC Loss for each batch entry: ", ctc_loss.numpy())
