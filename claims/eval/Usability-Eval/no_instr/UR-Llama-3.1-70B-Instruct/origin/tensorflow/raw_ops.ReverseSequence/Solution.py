import tensorflow as tf

def reverse_sequence(inputs, seq_lengths, seq_dim, batch_dim):
    """
    Reverses variable length slices.

    Args:
    inputs: A Tensor. The input to reverse.
    seq_lengths: A Tensor. Must be one of the following types: int32, int64. 1-D with size `batch_size` and containing sequence lengths.
    seq_dim: An int. The dimension which is to be reversed.
    batch_dim: An int. Dimension along which reversal is performed.

    Returns:
    A Tensor. Has the same type as `inputs`.
    """
    return tf.reverse_sequence(
        input=inputs, seq_lengths=seq_lengths, seq_dim=seq_dim, batch_dim=batch_dim
    )


# Example usage
if __name__ == "__main__":
    inputs = tf.constant(
        [
            [[0, 1, 2], [3, 4, 5]],
            [[6, 7, 8], [9, 10, 11]],
            [[12, 13, 14], [15, 16, 17]],
        ]
    )
    seq_lengths = tf.constant([1, 2, 2])

    reversed_inputs = reverse_sequence(
        inputs=inputs, seq_lengths=seq_lengths, seq_dim=1, batch_dim=0
    )
    print(reversed_inputs)
