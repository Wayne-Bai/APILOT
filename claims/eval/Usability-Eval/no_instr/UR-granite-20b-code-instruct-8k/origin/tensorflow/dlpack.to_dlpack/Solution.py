import tensorflow as tf

# Create a constant tensor
tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Convert the tensor to a dlpack capsule
dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)

print(dlpack_capsule)
