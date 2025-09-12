import tensorflow as tf

# Create a TensorFlow tensor
tensor = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# Convert the tensor to a dlpack capsule
capsule = tf.experimental.dlpack.to_dlpack(tensor)
