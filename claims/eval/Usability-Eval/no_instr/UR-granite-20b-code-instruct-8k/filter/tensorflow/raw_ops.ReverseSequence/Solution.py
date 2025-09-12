import tensorflow as tf

def reverse_variable_length_slices(tensor, lengths):
    """
    Reverses variable length slices.
    Args:
        tensor: A tensor of shape [batch_size, max_length, depth] or [batch_size, max_length].
        lengths: A tensor of shape [batch_size] containing the length of each sequence.
    Returns:
        A tensor of the same shape as `tensor` with slices reversed according to their length.
    """
    # Sort the tensor by lengths in descending order
    sorted_indices = tf.nn.top_k(tf.range(tf.shape(tensor)[1]), k=tf.shape(tensor)[1], sorted=True)[1]
    sorted_tensor = tf.gather_nd(tensor, tf.expand_dims(sorted_indices, -1), batch_dims=1)
    
    # Reverse the slices based on the sorted order
    reversed_tensor = tf.reverse_sequence(sorted_tensor, lengths, seq_axis=1, batch_axis=0)
    
    return reversed_tensor
