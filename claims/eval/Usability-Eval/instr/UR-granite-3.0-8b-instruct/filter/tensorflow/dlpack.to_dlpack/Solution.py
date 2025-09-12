import tensorflow as tf

def get_dlpack_capsule(tensor):
    return tf.experimental.dlpack.to_dlpack(tensor)

# Example usage:
tensor = tf.constant([[1, 2], [3, 4]])
dlpack_capsule = get_dlpack_capsule(tensor)
