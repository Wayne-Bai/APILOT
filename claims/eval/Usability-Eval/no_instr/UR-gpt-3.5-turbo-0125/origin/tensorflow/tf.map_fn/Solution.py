
import tensorflow as tf

def apply_transform_fn(elems, fn):
    elems_unstacked = tf.unstack(elems, axis=0)
    transformed_elems = [fn(elem) for elem in elems_unstacked]
    return transformed_elems
