
import tensorflow as tf

# Define two sequences
seq1 = tf.constant([[3, 4, 0, 0, 0]], dtype=tf.int32)
seq2 = tf.constant([[3, 4, 5, 6, 0]], dtype=tf.int32)

# Compute Levenshtein Edit Distance
edit_distance = tf.raw_ops.EditDistance(hypothesis_indices=seq1, truth_indices=seq2, normalize=True)
print(edit_distance)
