
import tensorflow as tf

def ctc_loss(logits, labels, label_length, logit_length):
    return tf.nn.ctc_loss(labels=labels, logits=logits, label_length=label_length, logit_length=logit_length, logits_time_major=False)

# Usage
logits = tf.constant([[[-0.1, -0.2, -0.9, -1.0], [-0.2, -0.1, -0.8, -0.9], [-0.3, -0.4, -0.7, -0.8]]], dtype=tf.float32)
labels = tf.constant([[1, 2]], tf.int32)
label_length = tf.constant([2], tf.int32)
logit_length = tf.constant([3], tf.int32)

loss = ctc_loss(logits, labels, label_length, logit_length)
