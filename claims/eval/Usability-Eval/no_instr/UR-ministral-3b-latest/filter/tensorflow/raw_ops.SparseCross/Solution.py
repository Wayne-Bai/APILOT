import tensorflow as tf

def generate_sparse_cross(*args):
    sparse_tensors = [sparse_tensor for sparse_tensor in args if isinstance(sparse_tensor, tf.Tensor) and sparse_tensor.dtype == tf.string]
    if sparse_tensors is None or len(sparse_tensors) < 2:
        raise ValueError('At least 2 sparse tensors are required for SparseCross operation.')

    num_sparse = len(sparse_tensors)
    dense_tensors = []
    for i in range(num_sparse):
        dense_tensor = sparse_tensors[i]
        num_dense = dense_tensor.shape.num_elements()
        dense_tensors.append(tf.ragged.constant(tf.range(num_dense), dtype=tf.int64))

    for i in range(num_sparse):
        sparse_tensor = dense_tensors[i]
        dense_tensor = sparse_tensors[i]
        res = tf.raw_ops.raw_sparse_cross_sparse_tensor(dense_tensor, sparse_tensor, num_sparse)

    return res
