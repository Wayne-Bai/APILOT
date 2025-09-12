import tensorflow as tf
import numpy as np

# Create a TensorFlow tensor
tensor = tf.constant(np.arange(10))

# Convert the tensor to a dlpack capsule
dlpack = tf.experimental.dlpack.to_dlpack(tensor)

print(dlpack)
