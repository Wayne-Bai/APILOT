import tensorflow as tf

# Create a simple tensor for demonstration
tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.int32)

# To get the DLPack capsule, use the experimental function
dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)

# Verify the result
print(type(dlpack_capsule))
