import tensorflow as tf

# Define the input tensor
inputs = tf.placeholder(tf.float32, shape=[None, None, None], name='inputs')

# Define the labels tensor
labels = tf.placeholder(tf.int32, shape=[None, None], name='labels')

# Define the sequence length tensor
sequence_length = tf.placeholder(tf.int32, shape=[None], name='sequence_length')

# Define the CTC Loss op
loss = tf.nn.ctc_loss(labels, inputs, sequence_length, preprocess_collapse_repeated=False, ctc_merge_repeated=True)

# Define the optimizer
optimizer = tf.train.AdamOptimizer().minimize(loss)
