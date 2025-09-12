import tensorflow as tf

def sparse_cross(sparse_tensors, dense_tensors):
    """Generates sparse cross from a list of sparse and dense tensors.

    Args:
      sparse_tensors: A list of SparseTensor.
      dense_tensors: A list of Tensor.

    Returns:
      A SparseTensor.
    """
    sparse_input = tf.concat([tf.sparse.to_dense(x) for x in sparse_tensors], 1)
    dense_input = tf.concat(dense_tensors, 1)

    ids = [tf.constant([0, 1, 2], dtype=tf.int64),  # This is just placeholder
           tf.constant([0, 1, 2], dtype=tf.int64)]  # This is just placeholder

    input_indices = tf.concat([tf.reshape(t, [-1, 1]) for t in ids], 1)
    input_values = tf.concat([tf.reshape(sparse_input, [-1]), dense_input], 0)
    input_shape = [tf.shape(sparse_input)[0], tf.reduce_prod(tf.shape(sparse_input)[1:]) + tf.shape(dense_input)[1]]

    input_st = tf.sparse.SparseTensor(input_indices, input_values, input_shape)
    sparse_cross_output = tf.sparse.cross(input_st, combiner='mean')
    return sparse_cross_output
