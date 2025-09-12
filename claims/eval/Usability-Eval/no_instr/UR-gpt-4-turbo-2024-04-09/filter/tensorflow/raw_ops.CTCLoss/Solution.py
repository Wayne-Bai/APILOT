import tensorflow as tf

# Sample data: batch_size = 2, max_time_steps = 4, num_classes = 3 (including the blank label)
# logits is a random tensor simulating the output of a neural network (logits need to be softmax probabilities)
logits = tf.random.uniform([2, 4, 3], minval=0, maxval=1, dtype=tf.float32)
logits = tf.nn.softmax(logits)  # ensuring that logits are probabilities

# Labels are sparse representations
labels = tf.SparseTensor(
    indices=[[0, 0], [1, 0], [1, 1]],
    values=[1, 2, 1],  # class labels
    dense_shape=[2, 2]  # [batch_size, max_time_in_batch]
)

# Sequence length: Length of the input sequences
seq_length = tf.constant([4, 4], dtype=tf.int32)

# Compute the CTC loss using tf.nn.ctc_loss
ctc_loss = tf.nn.ctc_loss(
    labels=labels,
    logits=logits,
    label_length=None,
    logit_length=seq_length,
    logits_time_major=False,
    blank_index=-1
)

print("CTC Loss for each batch element:", ctc_loss.numpy())
