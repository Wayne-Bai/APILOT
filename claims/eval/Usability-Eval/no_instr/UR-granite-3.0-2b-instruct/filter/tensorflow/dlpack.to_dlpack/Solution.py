import tensorflow as tf

# Create a tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Convert the tensor to dlpack capsule
dl_capsule = tf.lib.dlpy.to_dl_capsule(tensor)

print(dl_capsule)
