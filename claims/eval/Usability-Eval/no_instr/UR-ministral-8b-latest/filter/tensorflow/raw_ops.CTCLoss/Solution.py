import tensorflow as tf

def calculate_ctc_loss(logits, labels, sequence_length, time_axis=0, blank_label_index=0):
    def contiguous_ctc_loss(input, targets, input_lengths):
        loss = tf.raw_ops.SequenceCTCLoss(logit_input=input, label_input=targets, input_length=input_lengths)
        return loss

    logits = tf.convert_to_tensor(logits)
    labels = tf.convert_to_tensor(labels)
    sequence_length = tf.convert_to_tensor(sequence_length)

    ctc_loss = contiguous_ctc_loss(logits, labels, sequence_length)

    return ctc_loss

# Example usage
logits = [[[0.2, 0.8], [0.4, 0.6], [0.5, 0.5]],
          [[0.1, 0.8], [0.3, 0.5], [0.7, 0.2]]]

labels = [[[0, 1], [2, 3]], [[0, 3], [4, 1]]]
sequence_lengths = [3, 3]

ctc_loss = calculate_ctc_loss(logits, labels, sequence_lengths)
print(ctc_loss)
