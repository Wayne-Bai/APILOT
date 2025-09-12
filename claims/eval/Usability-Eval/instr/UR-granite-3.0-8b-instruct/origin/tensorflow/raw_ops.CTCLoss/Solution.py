import tensorflow as tf

def ctc_loss(labels, inputs, input_length, label_length):
    # Calculate the CTC loss for each batch entry
    # labels: Tensor of shape [batch_size, max_label_length]
    # inputs: Tensor of shape [batch_size, max_input_length, num_classes]
    # input_length: Tensor of shape [batch_size]
    # label_length: Tensor of shape [batch_size]

    # Calculate the log probabilities for each batch entry
    log_prob = tf.nn.ctc_loss(labels, inputs, input_length, label_length, blank_index=0)

    # Return the CTC loss for each batch entry
    return log_prob
