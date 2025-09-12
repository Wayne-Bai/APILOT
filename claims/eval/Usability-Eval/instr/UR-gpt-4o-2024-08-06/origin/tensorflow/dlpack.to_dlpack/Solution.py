import tensorflow as tf
import torch.utils.dlpack

# Create a TensorFlow tensor
tf_tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)

# Convert the TensorFlow tensor to a DLPack capsule
dlpack_tensor = tf.experimental.dlpack.to_dlpack(tf_tensor)

# Now, demonstrate converting the DLPack capsule back into a PyTorch tensor
torch_tensor = torch.utils.dlpack.from_dlpack(dlpack_tensor)

print("TensorFlow Tensor:\n", tf_tensor)
print("Torch Tensor (from DLPack):\n", torch_tensor)
