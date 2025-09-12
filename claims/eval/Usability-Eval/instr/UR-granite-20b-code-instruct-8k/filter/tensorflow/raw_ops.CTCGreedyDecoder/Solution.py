import tensorflow as tf

def greedy_decode(inputs):
    decoded, _ = tf.raw_ops.ctc_greedy_decoder(
        inputs=inputs,
        sequence_length=[inputs.shape[1]] * inputs.shape[0],
        merge_repeated=False
    )
    return decoded
