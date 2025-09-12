import tensorflow as tf

def greedy_decode(logits, sequence_length):
    # Ensure logits is a 2D tensor
    logits = tf.convert_to_tensor(logits, dtype=tf.float32)
    
    # Get the predicted tokens by taking the argmax along the last dimension
    predicted_tokens = tf.argmax(logits, axis=-1, output_type=tf.int32)
    
    # Create a mask for the sequence length
    mask = tf.sequence_mask(sequence_length, maxlen=tf.shape(logits)[1], dtype=tf.int32)
    
    # Apply the mask to the predicted tokens
    predicted_tokens = predicted_tokens * mask
    
    return predicted_tokens

# Example usage:
# logits: [batch_size, sequence_length, num_classes]
# sequence_length: [batch_size]
logits = tf.random.normal([32, 10, 50])  # Example logits
sequence_length = tf.constant([5, 7, 10, 3, 8, 9, 4, 6, 7, 5, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10, 3])  # Example sequence lengths

decoded_tokens = greedy_decode(logits, sequence_length)
print(decoded_tokens)
