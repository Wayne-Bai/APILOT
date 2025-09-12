import tensorflow as tf

def compute_levenshtein_distance(source_strings, target_strings, normalize=False):
    """
    Computes the Levenshtein distance between two sets of strings using TensorFlow.

    Parameters:
    source_strings : list of str
        A list of source strings.
    target_strings : list of str
        A list of target strings.
    normalize : bool
        If True, the distances are normalized by the lengths of the target strings.

    Returns:
    tensor : tf.Tensor
        A 2-D Tensor containing the Levenshtein distances between all combinations of
        source and target strings.
    """
    # Convert input lists to tensor
    source_tensor = tf.constant(source_strings, dtype=tf.string)
    target_tensor = tf.constant(target_strings, dtype=tf.string)

    # Calculate the Levenshtein distance matrix
    distance_matrix = tf.text.experimental.levenshtein_distance(source_tensor, target_tensor)

    if normalize:
        # Get the lengths of target strings for normalization
        target_lengths = tf.strings.length(target_tensor, unit='UTF8_CHAR')
        # Avoid division by zero
        target_lengths = tf.maximum(target_lengths, 1)
        target_lengths_matrix = tf.expand_dims(target_lengths, axis=0)

        # Normalize the distance matrix
        distance_matrix = tf.divide(distance_matrix, tf.cast(target_lengths_matrix, tf.float64))

    return distance_matrix

# Test example
source = ["hello", "world"]
target = ["helo", "word"]
distance = compute_levenshtein_distance(source, target, normalize=True)
print(distance)
