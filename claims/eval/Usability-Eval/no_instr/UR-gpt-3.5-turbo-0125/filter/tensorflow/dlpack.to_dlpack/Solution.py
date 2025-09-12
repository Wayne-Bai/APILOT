
import tensorflow as tf

# Before getting a DLPack capsule, we need to create a TensorFlow tensor
tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Get the DLPack capsule
dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)

# Now we have the dlpack capsule representing the tensor
