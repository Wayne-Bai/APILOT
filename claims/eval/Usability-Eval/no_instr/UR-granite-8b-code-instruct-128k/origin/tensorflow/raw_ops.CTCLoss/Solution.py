import tensorflow as tf

def ctc_loss(inputs, labels, sequence_length, preprocess_collapse_repeated=False, ctc_merge_repeated=True, ignore_longer_outputs_than_inputs=False, time_major=False, blank_index=0, label_shift=False, name=None):
    return tf.raw_ops.CTCLoss(inputs=inputs, labels=labels, sequence_length=sequence_length, preprocess_collapse_repeated=preprocess_collapse_repeated, ctc_merge_repeated=ctc_merge_repeated, ignore_longer_outputs_than_inputs=ignore_longer_outputs_than_inputs, time_major=time_major, blank_index=blank_index, label_shift=label_shift, name=name)
