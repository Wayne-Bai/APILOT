import tensorflow as tf
from tensorflow.experimental import dlpack

# Create a TensorFlow tensor
tensor = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# Convert the tensor to a DLPack capsule
capsule = dlpack.to_dlpack(tensor)
print(capsule)
