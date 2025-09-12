import tensorflow as tf
from tensorflow.keras import layers

# Define two strings to be compared
left = "kitten"
right = "sitting"

# Compute the Levenshtein Edit Distance between the two strings
edit_distance = tf.raw_ops.compute_levenshtein_edit_distance(
    left=left, right=right, normalize=True
)

# Print the edit distance
print(f"Edit distance: {edit_distance}")
