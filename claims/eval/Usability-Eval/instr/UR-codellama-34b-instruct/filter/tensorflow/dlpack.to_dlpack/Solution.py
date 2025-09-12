import tensorflow as tf
from dlpack import DLContext, DLTensor

# Create a tensor using TensorFlow
tensor = tf.constant([1., 2., 3.])

# Get the DLContext for the tensor
context = DLContext(device=tf.device.Device(type="CPU"), name="cpu")

# Create a DLTensor object from the tensor and context
dl_tensor = DLTensor(data=tensor, context=context)

# Get the DLPack capsule for the DLTensor object
capsule = dl_tensor.to_dlpack()

print(capsule)
