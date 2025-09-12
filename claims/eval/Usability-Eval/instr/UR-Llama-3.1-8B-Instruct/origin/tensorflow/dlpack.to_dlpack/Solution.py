import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([1, 2, 3, 4, 5, 6])

# Convert the tensor to a dlpack capsule
dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)

print(dlpack_capsule)
