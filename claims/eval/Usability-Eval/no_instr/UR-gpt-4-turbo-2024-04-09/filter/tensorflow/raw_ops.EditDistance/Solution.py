import tensorflow as tf

def compute_levenshtein_distance(hypothesis, truth, normalize=True):
    # Convert input strings to SparseTensor
    hypothesis_sparse = tf.sparse.from_dense(tf.strings.unicode_split(hypothesis, 'UTF-8'))
    truth_sparse = tf.sparse.from_dense(tf.strings.unicode_split(truth, 'UTF-8'))
    
    # Compute the Levenshtein distance
    distance = tf.edit_distance(hypothesis_sparse, truth_sparse, normalize=normalize)
    
    return distance

# Example usage
hypothesis = ["hello", "tensorflow", "example"]
truth = ["helo", "tensorflaw", "sample"]

distance = compute_levenshtein_distance(hypothesis, truth)
print(distance)
