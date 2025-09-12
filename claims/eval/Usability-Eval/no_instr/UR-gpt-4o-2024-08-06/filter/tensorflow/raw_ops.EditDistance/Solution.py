import tensorflow as tf

def compute_levenshtein_distance(hypothesis_list, truth_list, normalize=False):
    """
    Computes the Levenshtein Edit Distance between the hypothesis and truth sequences.
    
    Parameters:
    - hypothesis_list: A list of strings representing the hypothesis sequences.
    - truth_list: A list of strings representing the truth sequences.
    - normalize: Boolean flag indicating whether to normalize the edit distances.
    
    Returns:
    A tensor containing the edit distances.
    """
    # Convert lists of strings to tensor arrays
    hypothesis = tf.constant(hypothesis_list, dtype=tf.string)
    truth = tf.constant(truth_list, dtype=tf.string)

    # Use tf.strings.length to get the lengths of the strings
    hypothesis_lengths = tf.strings.length(hypothesis)
    truth_lengths = tf.strings.length(truth)

    # Compute the edit distance
    edit_distances = tf.edit_distance(
        tf.sparse.from_dense(hypothesis), 
        tf.sparse.from_dense(truth), 
        normalize=normalize
    )

    return edit_distances

# Example usage
hypothesis = ['kitten', 'sitting']
truth = ['sitting', 'knitting']
edit_distances = compute_levenshtein_distance(hypothesis, truth, normalize=True)

# Run the TensorFlow session to get the result
print("Edit Distances (Normalized):")
print(edit_distances.numpy())
