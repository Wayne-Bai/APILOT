import tensorflow as tf
import numpy as np

# Create a simple tensor
tensor = tf.constant(np.random.rand(10, 10), dtype=tf.float32)

# Get the Capsule representing the tensor
tensor_capsule = tensor.to_dlpack()
