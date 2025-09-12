import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.framework import dtypes

# Create a 2D tensor
tensor = tf.zeros((3, 4))

# Convert the tensor to a DLPack capsule
capsule = ops.Tensor.to_dlpack(tensor)

# Print the DLPack capsule
print(capsule)
