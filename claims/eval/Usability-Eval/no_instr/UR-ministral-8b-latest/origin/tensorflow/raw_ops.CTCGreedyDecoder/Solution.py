import tensorflow as tf

def greedy_decode(logits):
    # Convert logits to probabilities
    probabilities = tf.nn.softmax(logits)

    # Perform greedy decoding
    decoded_indices = tf.argmax(probabilities, axis=-1)

    return decoded_indices

# Example usage
logits = tf.constant([[0.1, 2.0, 0.3], [0.5, 0.8, 1.2]])
decoded_indices = greedy_decode(logits)
print(decoded_indices.numpy())
