import tensorflow as tf

def sparse_bin_count(sparse_tensor, vocab_size, weights=None):
    # Convert the sparse tensor to dense if necessary
    dense_tensor = tf.sparse.to_dense(sparse_tensor)

    # Create a range of values from 0 to vocab_size
    full_range = tf.range(vocab_size, dtype=dense_tensor.dtype)

    # Perform bin counting
    bins = tf.reduce_sum(
        tf.cast(tf.equal(full_range[:, tf.newaxis], dense_tensor), tf.int32),
        axis=1
    )

    if weights is not None:
        weights = tf.sparse.to_dense(weights)
        # Weighted bin counting
        bins = tf.reduce_sum(
            tf.cast(tf.equal(full_range[:, tf.newaxis], dense_tensor), tf.int32) * weights,
            axis=1
        )

    return bins

# Usage example:
if __name__ == "__main__":
    sparse_tensor = tf.sparse.from_dense(tf.constant([[0, 1, 0], [1, 0, 2]]))
    vocab_size = 3

    result = sparse_bin_count(sparse_tensor, vocab_size)
    print("Bin counts:", result)

    weights = tf.sparse.from_dense(tf.constant([[2, 3, 1], [4, 1, 2]]))
    weighted_result = sparse_bin_count(sparse_tensor, vocab_size, weights)
    print("Weighted bin counts:", weighted_result)
