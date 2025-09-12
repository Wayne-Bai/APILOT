import tensorflow as tf

logits = tf.constant(...)  # Your logits here
labels = tf.constant(...)  # Your labels here
label_length = tf.constant(...)  # Length of labels
input_length = tf.constant(...)  # Length of logits

loss = tf.nn.ctc_loss(labels, logits, label_length, input_length, logits_time_major=False, blank_index=-1)
loss = tf.reduce_mean(loss)
