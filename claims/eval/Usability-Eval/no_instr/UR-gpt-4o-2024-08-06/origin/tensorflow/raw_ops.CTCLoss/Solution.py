import tensorflow as tf

# Define parameters
batch_size = 2
max_time = 5
num_classes = 6  # excluding the blank label by convention

# Example inputs
inputs = tf.constant([
    [[0.1, 0.6, 0.1, 0.1, 0.1, 0.0],
     [0.1, 0.1, 0.1, 0.6, 0.1, 0.0],
     [0.1, 0.1, 0.6, 0.1, 0.1, 0.0],
     [0.6, 0.1, 0.1, 0.1, 0.1, 0.0],
     [0.1, 0.6, 0.1, 0.1, 0.1, 0.0]],
    
    [[0.1, 0.1, 0.1, 0.6, 0.1, 0.0],
     [0.6, 0.1, 0.1, 0.1, 0.1, 0.0],
     [0.1, 0.6, 0.1, 0.1, 0.1, 0.0],
     [0.1, 0.1, 0.6, 0.1, 0.1, 0.0],
     [0.1, 0.1, 0.1, 0.6, 0.1, 0.0]],
])

# Using softmax to convert logits to probabilities
inputs = tf.nn.log_softmax(inputs)

# Sequence lengths for each element in the batch
sequence_length = tf.constant([5, 5], dtype=tf.int32)

# Target index sequences
labels = tf.SparseTensor(
    indices=[[0, 0], [0, 1], [1, 0]],
    values=[1, 2, 2],
    dense_shape=[batch_size, 2]
)

# Calculate CTC loss
ctc_loss = tf.nn.ctc_loss(
    labels=labels,
    logits=inputs,
    label_length=None,
    logit_length=sequence_length,
    logits_time_major=False,
    blank_index=-1
)

# Create a session to run the CTC loss operation
ctc_loss_values = ctc_loss.numpy()
print("CTC Loss:", ctc_loss_values)
