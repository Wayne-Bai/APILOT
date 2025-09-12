import tensorflow as tf

def tensor_to_dlpack(tensor):
    return tf.experimental.dlpack.to_dlpack(tensor)

# Example tensor
tensor = tf.constant([1, 2, 3])

# Convert tensor to a DLPack capsule
dlpack_capsule = tensor_to_dlpack(tensor)
print(dlpack_capsule)
