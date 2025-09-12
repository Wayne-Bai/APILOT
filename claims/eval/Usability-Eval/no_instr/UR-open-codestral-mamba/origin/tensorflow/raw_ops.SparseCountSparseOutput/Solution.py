import tensorflow as tf

def sparse_output_bin_counting(sp_input):
    output = tf.math.bincount(sp_input.indices[:, -1])
    return output
