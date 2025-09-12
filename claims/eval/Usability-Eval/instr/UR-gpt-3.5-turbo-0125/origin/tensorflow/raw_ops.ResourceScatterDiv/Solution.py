
import tensorflow as tf

@tf.function
def sparse_divide_update(resource, indices, updates, name=None):
    return tf.raw_ops.SparseApplyDiv(resource=resource, indices=indices, updates=updates, name=name)
