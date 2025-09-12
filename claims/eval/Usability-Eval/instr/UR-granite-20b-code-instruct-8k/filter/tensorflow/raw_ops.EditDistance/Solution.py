import tensorflow as tf

# Use the updated version of Edit Distance API
# from tensorflow.raw_ops import EditDistance

def compute_levenshtein_edit_distance(tensor1, tensor2, normalize=True):
    """
    Computes the (possibly normalized) Levenshtein Edit Distance.

    Args:
    tensor1: a tensor of shape [batch_size, height_1, width_1] or [batch_size, height_1]
    tensor2: a tensor of shape [batch_size, height_2, width_2] or [batch_size, height_2]

    Returns:
    A tensor of shape [batch_size] containing the Levenshtein distances for each input pair.

    Note:
    The Levenshtein distance is a string metric for measuring the difference between two sequences.
    """
    with tf.name_scope("compute_levenshtein_edit_distance"):
        if len(tensor1.shape) == len(tensor2.shape) == 3:
            tensor1 = tf.reshape(tensor1, [tensor1.shape[0], -1])
            tensor2 = tf.reshape(tensor2, [tensor2.shape[0], -1])

        levenshtein_distances = tf.edit_distance(tensor1, tensor2, normalize=normalize)

        return levenshtein_distances
