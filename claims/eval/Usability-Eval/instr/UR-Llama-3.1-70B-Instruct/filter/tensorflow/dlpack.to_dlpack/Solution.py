import tensorflow as tf
from tensorflow.python import _pywrap_util_port

def get_dlpack(tensor):
    """Returns the dlpack capsule representing the tensor."""
    try:
        capsule = _pywrap_util_port.TFE_PyCapsuleNew(tensor._handle._weak_ref(), True)
        import capsule_utils
        return capsule_utils.DLCapsule(capsule)
    except AttributeError:
        raise ValueError("The tensor does not have a dlpack capsule.")

# Usage example:
# Create a sample tensor
tensor = tf.constant([1, 2, 3])

# Get the dlpack capsule for the tensor
dlpack_capsule = get_dlpack(tensor)

# Verify that the dlpack capsule is not None
if dlpack_capsule is not None:
    print("DLpack capsule acquired successfully.")
else:
    print("Failed to acquire DLpack capsule.")

# Verify the contents of the dlpack capsule
dlpack_tensor = tf.experimental.dlpack.from_dlpack(dlpack_capsule)
print("DLpack tensor contents: ", dlpack_tensor.numpy())
