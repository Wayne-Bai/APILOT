
import tensorflow as tf

def my_greedy_decoder(logits):
    decoded, _ = tf.raw_ops.CTCGreedyDecoder(inputs=logits)
    return decoded
