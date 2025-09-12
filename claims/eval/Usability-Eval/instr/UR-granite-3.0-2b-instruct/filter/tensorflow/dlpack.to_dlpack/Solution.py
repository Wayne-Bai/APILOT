import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert the tensor to dlpack capsule
dlpack_capsule = tf.config.experimental.to_dlpack(tensor)

# Print the dlpack capsule
print(dlpack_capsule)
