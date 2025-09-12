import tensorflow as tf

def greedy_decode(inputs, sequence_length):
    batch_size = tf.shape(inputs)[0]
    max_length = tf.shape(inputs)[1]
    
    # Initialize the decoded sequence with zeros
    decoded_sequence = tf.zeros([batch_size, 1], dtype=tf.int32)
    
    # Create a mask to handle sequence length
    mask = tf.sequence_mask(sequence_length, maxlen=max_length, dtype=tf.float32)
    
    # Iterate over the sequence length
    for t in range(max_length):
        # Get the logits for the current time step
        current_logits = inputs[:, t, :]
        
        # Apply the mask to the logits
        masked_logits = current_logits * mask[:, t, tf.newaxis]
        
        # Get the predicted token
        predicted_token = tf.argmax(masked_logits, axis=-1)
        
        # Append the predicted token to the decoded sequence
        decoded_sequence = tf.concat([decoded_sequence, tf.expand_dims(predicted_token, 1)], axis=1)
    
    # Remove the initial zero token
    decoded_sequence = decoded_sequence[:, 1:]
    
    return decoded_sequence

# Example usage
# inputs: [batch_size, max_length, vocab_size]
# sequence_length: [batch_size]
inputs = tf.random.normal([32, 10, 5000])
sequence_length = tf.random.uniform([32], minval=1, maxval=10, dtype=tf.int32)

decoded_sequence = greedy_decode(inputs, sequence_length)
print(decoded_sequence)
