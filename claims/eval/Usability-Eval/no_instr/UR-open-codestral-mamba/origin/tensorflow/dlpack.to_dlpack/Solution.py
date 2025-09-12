import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Get the dlpack capsule from the tensor
dlpack_capsule = tf.compat.v1.contrib.dlpack.to_dlpack(tensor)

print(dlpack_capsule)
