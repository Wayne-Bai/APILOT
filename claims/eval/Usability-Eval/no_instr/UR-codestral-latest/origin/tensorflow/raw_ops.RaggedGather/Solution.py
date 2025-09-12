import tensorflow as tf

# Assuming you have a 2D tensor `params` and a 1D tensor `indices`
def gather_ragged_slices(params, indices):
    return tf.gather(params, indices, axis=0)
