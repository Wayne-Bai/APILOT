import tensorflow as tf

def tensor_to_dlpack(tensor):
    return tf.experimental.dlpack.to_dlpack(tensor)