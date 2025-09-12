
import tensorflow as tf

# Define the inputs needed for CTC loss calculation
logits = tf.constant([[[-0.1, -0.3, -0.7, -0.5],
                       [-0.6, -0.4, -0.2, -0.8],
                       [-0.9, -0.2, -0.3, -0.6]]], dtype=tf.float32)  # Shape: (1, 3, 4)

labels_indices = tf.constant([[0, 0, 1, 1],
                              [0, 1, 1, 2],
                              [2, 1, -1, -1]], dtype=tf.int32)  # Shape: (3, 4)

labels_values = tf.constant([1, 2, 3, 3], dtype=tf.int32)  # Shape: (4,)

sequence_length = tf.constant([3], dtype=tf.int32)  # Shape: (1,)

# Calculating CTC Loss
ctc_loss = tf.raw_ops.CtcLoss(log_probs=logits, labels=labels_values, label_length=sequence_length, logits_time_major=False, 
                              blank_index=0, labels_indices=labels_indices, logit_length=sequence_length)

# Print the CTC Loss
print(ctc_loss)
