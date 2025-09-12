import tensorflow as tf

def compute_ctc_loss(logits, labels, sequence_length):
    # Compute the CTC loss
    ctc_loss = tf.nn.ctc_loss(labels=labels,
                                logits=logits,
                                label_length=tf.shape(labels)[1],
                                logit_length=sequence_length,
                                preprocess_collapse_repeated=True,
                                ctc_merge_repeated=True)
    return ctc_loss

# Example usage:
# logits shape: [max_time, batch_size, num_classes]
# labels shape: [batch_size, max_label_length]
# sequence_length shape: [batch_size]

# Define dummy data for testing
logits = tf.random.uniform((10, 5, 20), dtype=tf.float32)  # Example: max_time=10, batch_size=5, num_classes=20
labels = tf.constant([[0, 1], [1, 2], [2, 0], [1, 1], [0, 2]])  # Labels for batch size 5
sequence_length = tf.constant([10, 10, 10, 10, 10])  # All sequences are of full length

loss = compute_ctc_loss(logits, labels, sequence_length)
print(loss)
