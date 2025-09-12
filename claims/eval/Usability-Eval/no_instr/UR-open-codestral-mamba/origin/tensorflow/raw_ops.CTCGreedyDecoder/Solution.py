import tensorflow as tf

def greedy_decoding(logits):
    decoded = tf.argmax(logits, axis=-1)
    return decoded
