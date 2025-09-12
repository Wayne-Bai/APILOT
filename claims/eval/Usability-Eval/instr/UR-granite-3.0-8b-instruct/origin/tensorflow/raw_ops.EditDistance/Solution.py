import tensorflow as tf

# Define the input tensors
a = tf.constant("kitten", family=['family'])
b = tf.constant("sitting", family=['family'])

# Compute the Levenshtein distance
levenshtein_distance = tf.raw_ops.LevenshteinDistance(a, b)

# Normalize the distance by the maximum possible distance
max_distance = tf.reduce_max(tf.shape(a) + tf.shape(b))
normalized_distance = levenshtein_distance / max_distance

print("Levenshtein Distance: ", levenshtein_distance)
print("Normalized Levenshtein Distance: ", normalized_distance)
