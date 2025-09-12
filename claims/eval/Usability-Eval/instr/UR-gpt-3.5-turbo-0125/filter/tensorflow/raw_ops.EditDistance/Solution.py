
import tensorflow as tf

# Define two sequences
hyp_sequence = tf.constant(["h", "e", "l", "l", "o"])
ref_sequence = tf.constant(["h", "e", "a", "l", "o"])

# Compute Levenshtein distance
distance = tf.raw_ops.EditDistance(hypothesis=hyp_sequence, truth=ref_sequence, normalize=True)

# Start a TensorFlow session and run the computation
with tf.Session() as sess:
    result = sess.run(distance)
    print("Levenshtein Edit Distance between the two sequences:", result)
