import tensorflow as tf

# Create a tensor
tensor = tf.ones([3, 2])

# Convert the tensor to a DLPack capsule
dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)

# Print the type of the capsule
print(type(dlpack_capsule))
