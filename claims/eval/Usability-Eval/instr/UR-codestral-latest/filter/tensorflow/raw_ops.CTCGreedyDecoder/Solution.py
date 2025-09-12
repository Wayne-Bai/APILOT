import tensorflow as tf

def greedy_decode(logits):
    return tf.argmax(logits, axis=-1)

# Example usage:
# logits = tf.random.normal([1, 10])  # this can be your actual logits
# decoded_sequence = greedy_decode(logits)
