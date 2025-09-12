import tensorflow as tf

def greedy_decode(logits):
    # Use CTC greedy decoder from tensorflow raw ops
    decoded_indices, decoded_values, decoded_shape, log_probability = tf.raw_ops.CTCGreedyDecoder(
        inputs=tf.transpose(logits, perm=[1, 0, 2]),
        sequence_length=[logits.shape[1]] * logits.shape[0],
        merge_repeated=True
    )
    
    # Convert the sparse representation into a dense one
    decoded_sequences = tf.sparse.to_dense(
        tf.sparse.SparseTensor(decoded_indices, decoded_values, decoded_shape),
        default_value=-1
    )
    
    return decoded_sequences, log_probability

# Example use case
# Assuming `logits` is a 3D Tensor with shape [batch_size, max_time, num_classes]
logits = tf.random.uniform([2, 10, 100])  # Random data for illustration
decoded_sequences, log_probability = greedy_decode(logits)
print("Decoded sequences:", decoded_sequences)
print("Log probabilities:", log_probability)
