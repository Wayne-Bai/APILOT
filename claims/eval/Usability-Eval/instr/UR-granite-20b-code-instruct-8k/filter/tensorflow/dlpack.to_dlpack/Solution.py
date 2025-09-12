import tensorflow as tf
# Create a tensor
tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
# Convert the tensor to a dlpack capsule
dlpack = tf.experimental.dlpack.to_dlpack(tensor)
