import tensorflow as tf
from tensorflow.python.ops import ctc_ops as ctc

# Define parameters
logits = tf.placeholder(tf.float32, [None, None, num_classes])  # Shape: (batch_size, max_time, num_classes)
labels = tf.sparse.placeholder(tf.int32)  # Shape: (batch_size, max_label_length)

# Calculate CTC loss
loss = ctc.ctc_loss(labels, logits, sequence_length, ignore_longer_outputs_than_inputs=True)
loss = tf.reduce_mean(loss)  # Calculate the mean loss for the batch

# Create a TensorFlow session and run the loss calculation
with tf.Session() as sess:
    loss_value = sess.run(loss, feed_dict={logits: logits_data, labels: labels_data, sequence_length: sequence_length_data})

print("CTC Loss:", loss_value)
