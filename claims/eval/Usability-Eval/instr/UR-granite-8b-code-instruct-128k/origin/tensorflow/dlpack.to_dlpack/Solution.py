import tensorflow as tf

def generate_dlpack_capsule(tensor):
    return tf.experimental.dlpack.to_dlpack(tensor)
