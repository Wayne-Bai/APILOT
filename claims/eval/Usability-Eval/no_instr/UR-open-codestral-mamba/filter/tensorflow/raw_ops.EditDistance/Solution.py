import tensorflow as tf

def levenshtein_distance(ref, hyp):
    # Define range
    ranges = tf.expand_dims(tf.range(0, tf.shape(ref)[1], delta=1), 0)

    # Create distances matrix
    m = tf.shape(ref)[0] + 1
    n = tf.shape(ref)[1] + 1
    distances = tf.empty([m, n], tf.int32)

    # Initialize first distances
    distances = tf.edit_distance(hyp, ref, normalize=False)

    return distances

ref = tf.constant(["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"])
hyp = tf.constant(["their", "quick", "brown", "fox", "juices", "overs", "lazily", "dog"])

print(levenshtein_distance(ref, hyp))
