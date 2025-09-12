import tensorflow as tf
import tensorflow.experimental.dlpack as dlpack

# Create a TensorFlow tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Convert the TensorFlow tensor to a DLPack capsule
dlpack_capsule = dlpack.to_dlpack(tensor)

# Output the dlpack capsule
print(dlpack_capsule)
