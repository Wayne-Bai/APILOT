
import tensorflow as tf

# Define the function to compute the Levenshtein Edit Distance
def levenshtein_edit_distance(input_tensor1, input_tensor2, normalize=True):
    """
    Computes the (possibly normalized) Levenshtein Edit Distance.
    Args:
    input_tensor1: A `Tensor` of type `string`.
    input_tensor2: A `Tensor` of type `string`.
    normalize: A `bool`. If True, normalizes the Levenshtein distance by the maximum length of the two sequences.
    Returns:
    A `Tensor` of type `int32`.
    """
    # Get the length of the two input tensors
    input_length1 = tf.strings.length(input_tensor1)
    input_length2 = tf.strings.length(input_tensor2)
    
    # Compute the Levenshtein distance using tf.raw_ops.EditDistance
    levenshtein_distance = tf.raw_ops.EditDistance(
        hunks=[input_tensor1, input_tensor2],
        block_size=16,
        normalize=normalize
    )
    
    # Normalize the Levenshtein distance if requested
    if normalize:
        levenshtein_distance = tf.cast(levenshtein_distance, tf.float32)
        levenshtein_distance = tf.divide(levenshtein_distance, tf.maximum(input_length1, input_length2))
        levenshtein_distance = tf.multiply(levenshtein_distance, 100)
        levenshtein_distance = tf.cast(levenshtein_distance, tf.int32)
    
    return levenshtein_distance
