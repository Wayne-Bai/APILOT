import tensorflow as tf

def gather_ragged_slices(params, indices):
    return tf.raw_ops.RaggedGather(params=params, indices=indices, axis=0)
