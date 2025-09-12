import tensorflow as tf

def ctc_loss(log_probs, labels, label_lengths, log_prob_lengths, blank_index=-1):
    with tf.name_scope('CTCLoss'):
        # log_probs: [max_time, batch_size, num_classes]
        # labels: [batch_size, max_label_length]
        # label_lengths: [batch_size]
        # log_prob_lengths: [batch_size]

        # log_probs = tf.nn.ctc_loss(inputs=log_probs,
        #                          labels=labels,
        #                          sequence_length=log_prob_lengths,
        #                          ctc_merge_repeated=True,
        #                          ignore_longer_outputs_than_inputs=True,
        #                          time_major=False,
        #                          blank_index=blank_index)

        return tf.raw_ops.CTCLoss(inputs=log_probs,
                                 labels=labels,
                                 label_lengths=label_lengths,
                                 log_prob_lengths=log_prob_lengths,
                                 preprocess_collapse_repeated=True,
                                 ctc_merge_repeated=True,
                                 ignore_longer_outputs_than_inputs=True,
                                 time_major=False,
                                 blank_index=blank_index,
                                 name='CTCLoss')

# Example usage
log_probs = tf.random.normal((10, 10, 10))
labels = tf.random.uniform((10, 8), maxval=10, dtype=tf.int32)
label_lengths = tf.random.uniform((10,), maxval=8, dtype=tf.int32)
log_prob_lengths = tf.random.uniform((10,), maxval=10, dtype=tf.int32)
loss = ctc_loss(log_probs, labels, label_lengths, log_prob_lengths)
print(loss)
