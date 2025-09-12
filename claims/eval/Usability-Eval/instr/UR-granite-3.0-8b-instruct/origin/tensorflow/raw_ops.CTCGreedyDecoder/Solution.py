import tensorflow as tf

# Assuming inputs is your input tensor and vocabulary is your vocabulary list
def decode_greedy(inputs, vocabulary):
    # Convert inputs to a tensor if it's not already
    if not isinstance(inputs, tf.Tensor):
        inputs = tf.constant(inputs)

    # Perform greedy decoding
    decoded = tf.raw_ops.GreedySearch(inputs, vocabulary)

    return decoded
