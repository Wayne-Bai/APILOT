import tensorflow as tf

# Creating a tensor
tensor = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# Getting the dlpack capsule representing the tensor
capsule = tf.experimental.dlpack.to_dlpack(tensor)
