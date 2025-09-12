import tensorflow as tf

# Define sequences
hypothesis = tf.constant([[1, 2, 3], [2, 3, 2]], dtype=tf.int64)  # 2 sequences
truth = tf.constant([[1, 2, 4], [2, 3, 5]], dtype=tf.int64)

# Calculate Levenshtein Edit Distance
edit_distance = tf.edit_distance(hypothesis, truth, normalize=True)

# Run session to evaluate tensors
print("Levenshtein Edit Distance:")
print(edit_distance.numpy())
