
import tensorflow as tf
import numpy as np

# Create a sample tensor
data = np.array([[1, 2, 3], [4, 5, 6]])
tensor = tf.constant(data)

# Get the dlpack capsule representing the tensor
dlpack_capsule = tf.experimental.dlpack.tensor_to_dlpack(tensor)
