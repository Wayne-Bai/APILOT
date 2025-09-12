import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Get the DLPack capsule
dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)

# If you need to return or use the capsule in another context, you can do so here
print(dlpack_capsule)
