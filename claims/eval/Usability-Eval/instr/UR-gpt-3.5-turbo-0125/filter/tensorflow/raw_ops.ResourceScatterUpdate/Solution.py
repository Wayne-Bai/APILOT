
import tensorflow as tf

def sparse_variable_update(resource, indices, values, name=None):
    return tf.raw_ops.ResourceStridedSliceAssign(ref=resource, begin=df, end=end, strides=strides, value=value, name=name)
