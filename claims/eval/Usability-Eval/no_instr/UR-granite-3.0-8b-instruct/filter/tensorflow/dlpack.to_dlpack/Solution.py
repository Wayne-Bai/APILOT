import tensorflow as tf

def get_dlpack(tensor):
    return tf.experimental.dlpack.to_dlpack(tensor)
