
import tensorflow as tf

def levenshtein_edit_distance(hypothesis, truth, normalize=True, name=None):
    return tf.edit_distance(hypothesis, truth, normalize=normalize, name=name)
