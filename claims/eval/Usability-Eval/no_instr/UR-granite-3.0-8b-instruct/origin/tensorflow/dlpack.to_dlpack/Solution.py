import tensorflow as tf

# Assuming 'tensor' is your TensorFlow tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Get the dlpack capsule
dlpack_capsule = tensor.experimental_ref()

# Print the dlpack capsule
print(dlpack_capsule)
