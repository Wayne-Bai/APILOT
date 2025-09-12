
import tensorflow as tf

# Define two sequences
str1 = tf.constant("kitten")
str2 = tf.constant("sitting")

# Compute the Levenshtein Edit Distance
distance = tf.raw_ops.EditDistance(hypothesis=str1, truth=str2, normalize=True)

# Print the result
print("The Levenshtein Edit Distance is:", distance)
