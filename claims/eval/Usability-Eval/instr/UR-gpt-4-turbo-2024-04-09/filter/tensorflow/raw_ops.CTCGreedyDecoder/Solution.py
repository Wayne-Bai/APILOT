import tensorflow as tf

def decode_logits(logits, sequence_length):
    # Transposing the logits from time-major to batch-major
    logits = tf.transpose(logits, perm=[1, 0, 2])
    
    # Performing greedy decoding
    decoded, log_probabilities = tf.nn.ctc_greedy_decoder(inputs=logits, sequence_length=sequence_length)
    
    # Convert the resulting sparse tensor to a dense representation
    decoded_dense = tf.sparse.to_dense(decoded[0], default_value=-1)
    
    return decoded_dense, log_probabilities

# Example usage:
# Assuming `logits` is a [max_time, batch_size, num_classes] tensor
# and `sequence_length` is a tensor of shape [batch_size]
logits = tf.random.normal([100, 4, 26])  # 100 timesteps, batch of 4, 26 classes (e.g., A-Z)
sequence_length = tf.constant([100, 80, 90, 100])

decoded_output, log_probs = decode_logits(logits, sequence_length)
print("Decoded output:", decoded_output)
print("Log probabilities:", log_probs)
