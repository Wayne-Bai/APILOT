import tensorflow as tf

# Computes the (possibly normalized) Levenshtein Edit Distance.
def levenshtein_distance(labels, predictions, normalize=True, name=None):
  with tf.name_scope(name, "levenshtein_distance", [labels, predictions]):
    labels = tf.convert_to_tensor(labels, name="labels")
    predictions = tf.convert_to_tensor(predictions, name="predictions")
    distance = tf.edit_distance(labels, predictions, normalize=normalize)
    return distance
