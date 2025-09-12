import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Convert the tensor to dlpack capsule
dlpack_capsule = tf.contrib.raw_ops.DlpackCapsule(tensor)

# Print the dlpack capsule
print(dlpack_capsule)
