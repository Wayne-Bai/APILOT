# Importing necessary libraries
import tensorflow as tf
import numpy as np

# Creating a function that performs greedy decoding on the logits given in inputs
def greedy_decoder(logits, sequence_length):
    """
    Performs greedy decoding on the logits given in inputs.

    Args:
    logits: A tensor of shape [batch_size, sequence_length, vocabulary_size] containing 
            the logits for each word in the sequence.
    sequence_length: A tensor of shape [batch_size] containing the length of each sequence.

    Returns:
    decoded_sequences: A tensor of shape [batch_size, sequence_length] containing the 
                       decoded sequences.
    """
    decoded_sequences, _ = tf.raw_ops.GreedySequence(logits, sequence_length)
    return decoded_sequences

# Example usage:
if __name__ == "__main__":
    # Define the batch size and sequence length
    batch_size = 1
    sequence_length = 10
    vocabulary_size = 100

    # Generate random logits
    logits = np.random.rand(batch_size, sequence_length, vocabulary_size).astype(np.float32)

    # Define the sequence length
    sequence_lengths = np.array([sequence_length])

    # Convert numpy arrays to tensors
    logits_tensor = tf.convert_to_tensor(logits)
    sequence_lengths_tensor = tf.convert_to_tensor(sequence_lengths)

    # Perform greedy decoding
    decoded_sequences = greedy_decoder(logits_tensor, sequence_lengths_tensor)

    # Print the decoded sequence
    print("Decoded sequence:", decoded_sequences.numpy())
