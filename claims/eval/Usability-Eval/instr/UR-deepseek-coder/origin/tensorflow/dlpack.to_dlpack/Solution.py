import tensorflow as tf
from tensorflow.experimental import dlpack

def tensor_to_dlpack(tensor):
    return dlpack.to_dlpack(tensor)

# Example usage:
tensor = tf.constant([1, 2, 3, 4])
dlpack_capsule = tensor_to_dlpack(tensor)
print(dlpack_capsule)
