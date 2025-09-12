import tensorflow as tf

def greedy_decode(logits):
    # Perform greedy decoding on the logits
    # logits shape should be [batch_size, sequence_length, vocab_size]
    predicted_ids = tf.argmax(logits, axis=-1)
    return predicted_ids

# Example usage:
# logits = tf.random.uniform((2, 5, 10))  # Batch size of 2, sequence length of 5, vocab size of 10
# decoded_ids = greedy_decode(logits)
# print(decoded_ids)
