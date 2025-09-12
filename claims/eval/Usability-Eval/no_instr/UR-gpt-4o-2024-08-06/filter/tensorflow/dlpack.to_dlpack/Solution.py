import tensorflow as tf

# Create a sample TensorFlow tensor
tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)

# Convert the tensor to a DLPack capsule
dlpack_tensor = tf.experimental.dlpack.to_dlpack(tensor)

# Print the type of the dlpack_tensor to confirm it's a capsule
print(type(dlpack_tensor))
