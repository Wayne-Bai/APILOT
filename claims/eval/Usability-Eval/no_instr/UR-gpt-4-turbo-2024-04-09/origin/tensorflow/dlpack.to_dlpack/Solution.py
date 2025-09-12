import tensorflow as tf

def get_dlpack_capsule(tensor):
    dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)
    return dlpack_capsule

# Example usage
tensor = tf.constant([1, 2, 3])
capsule = get_dlpack_capsule(tensor)
print("DLPack Capsule:", capsule)
