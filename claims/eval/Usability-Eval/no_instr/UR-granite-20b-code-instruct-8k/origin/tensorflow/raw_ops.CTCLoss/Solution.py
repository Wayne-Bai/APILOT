import tensorflow as tf

# Calculate the CTC Loss (log probability) for each batch entry
# tf.raw_ops.ctc_loss(inputs, labels, sequence_length, preprocess_collapse_repeated=False, ctc_merge_repeated=True, ignore_longer_outputs_than_inputs=False, time_major=True,NuD=None, name=None)

inputs = tf.placeholder(tf.float32, shape=[None, None, None], name="inputs")
labels = tf.placeholder(tf.int32, shape=[None, None], name="labels")
sequence_length = tf.placeholder(tf.int32, shape=[None], name="sequence_length")

ctc_loss = tf.nn.ctc_loss(inputs, labels, sequence_length, preprocess_collapse_repeated=False, ctc_merge_repeated=True, ignore_longer_outputs_than_inputs=False, time_major=True)

