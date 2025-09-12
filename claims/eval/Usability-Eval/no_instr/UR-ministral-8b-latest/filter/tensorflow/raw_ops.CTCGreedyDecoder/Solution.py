import tensorflow as tf

def greedy_decoding(logits):
    # Perform greedy decoding on the logits
    decoded_indices = tf.argmax(logits, axis=-1)
    return decoded_indices

# Example usage
logits = tf.constant([[2.0, 1.0, 0.1], [1.0, 0.5, 1.0]])
decoded_output = greedy_decoding(logits)
print(decoded_output)
