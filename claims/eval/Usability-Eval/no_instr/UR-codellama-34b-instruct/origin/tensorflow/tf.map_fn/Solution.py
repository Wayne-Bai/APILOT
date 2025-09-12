
import tensorflow as tf

def transform_unstacked(fn, elems):
    return tf.stack([fn(elem) for elem in tf.unstack(elems, axis=0)], axis=0)
