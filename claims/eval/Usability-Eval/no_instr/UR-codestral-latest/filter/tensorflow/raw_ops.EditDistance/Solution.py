import tensorflow as tf
from tensorflow.keras import metrics

# Define the strings
string1 = tf.constant("kitten")
string2 = tf.constant("sitting")

# Compute the Levenshtein Edit Distance
levenshtein_distance = metrics.edit_distance(string1, string2, normalize=False)

# Print the result
print("The Levenshtein Edit Distance is: ", levenshtein_distance.numpy())
