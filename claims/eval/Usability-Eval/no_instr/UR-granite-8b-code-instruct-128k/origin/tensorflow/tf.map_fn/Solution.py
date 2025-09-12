import tensorflow as tf

def transform_elements(elems, fn):
    return tf.stack([fn(elem) for elem in tf.unstack(elems, axis=0)])
