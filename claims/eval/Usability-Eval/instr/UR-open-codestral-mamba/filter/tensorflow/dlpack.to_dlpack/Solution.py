import tensorflow as tf

# Assuming we have a tensor 't'
# tf.experimental.dlpack.to_dlpack is not a found since it is a deprecated API since TF 2.4.
t = tf.constant([[1.0, 2.0], [3.0, 4.0]])

def get_dlpack_capsule(tensor):
    return tf.unsafe_tensor_to_dlpack(tensor)

dlpack_capsule = get_dlpack_capsule(t)
