import tensorflow as tf

def greedy_decode(logits):
    """
    Performs greedy decoding on the logits.
    """
    decoded_outputs = tf.argmax(logits, axis=-1)
    return decoded_outputs

# Test the function
logits = tf.random.normal([3, 10])
decoded_sequence = greedy_decode(logits)
print(decoded_sequence)
