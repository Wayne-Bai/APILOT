import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_split, axis):
    return tf.raw_ops.Split(split_dim=axis, num_split=num_split, value=sparse_tensor)
