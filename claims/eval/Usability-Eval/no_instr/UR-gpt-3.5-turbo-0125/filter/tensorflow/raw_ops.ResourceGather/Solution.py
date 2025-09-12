
import tensorflow as tf

@tf.function
def gather_slices(variable, indices):
    gathered_slices = tf.raw_ops.Gather(resource=variable, indices=indices)
    return gathered_slices
