import tensorflow as tf

def tensor_to_dlpack(tensor):
    return tf.experimental.dlpack.to_dlpack(tensor)

# Example usage:
tensor = tf.constant([1, 2, 3])
dlpack_capsule = tensor_to_dlpack(tensor)
print(dlpack_capsule)
