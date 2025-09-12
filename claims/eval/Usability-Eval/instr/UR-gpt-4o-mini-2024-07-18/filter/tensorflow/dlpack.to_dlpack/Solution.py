import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Import DLPack
from tensorflow.experimental.dlpack import to_dlpack

# Get the DLPack capsule representing the tensor
dlpack_capsule = to_dlpack(tensor)

# Print the DLPack capsule
print(dlpack_capsule)
