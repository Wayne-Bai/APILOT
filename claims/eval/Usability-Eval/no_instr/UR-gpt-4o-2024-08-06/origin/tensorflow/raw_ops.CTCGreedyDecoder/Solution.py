import tensorflow as tf

def greedy_decoder(logits):
    """
    Perform greedy decoding on the logits given in inputs.
    Args:
    - logits: A 3D tensor with shape [batch_size, sequence_length, num_classes].
    
    Returns:
    - decoded_sequences: A 2D tensor with shape [batch_size, sequence_length] containing the 
      indices of the chosen classes.
    """
    # Use argmax to get the index of the maximum logit for each element in the sequence
    decoded_sequences = tf.argmax(logits, axis=-1, output_type=tf.int32)
    return decoded_sequences

# Example usage
# Let's assume logits is a tensor of shape [batch_size, sequence_length, num_classes]
logits = tf.random.uniform(shape=(2, 5, 10))  # batch_size=2, sequence_length=5, num_classes=10
decoded_sequences = greedy_decoder(logits)

# Start a tensorflow session to evaluate the tensor
print("Decoded sequences:", decoded_sequences.numpy())
