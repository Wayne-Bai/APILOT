import tensorflow as tf

# Define the tensors for the input strings
a = tf.constant("kitten")
b = tf.constant("sitting")

# Perform Levenshtein Edit Distance using tf.raw_ops.EditDistance function
dist = tf.raw_ops.EditDistance.TRAILING_DISTANCE(
    a=a,
    b=b,
)
print(dist)
