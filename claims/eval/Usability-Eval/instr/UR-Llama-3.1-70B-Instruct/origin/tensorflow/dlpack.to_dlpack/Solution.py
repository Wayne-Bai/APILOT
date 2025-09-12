# Import the required TensorFlow module
import tensorflow as tf

# Define a function to return the dlpack capsule representing the tensor
def get_dlpack_capsule(tensor):
    # Use the to_dlpack() function from TensorFlow's experimental.dlpack module
    from tensorflow.experimental.dlpack import to_dlpack
    return to_dlpack(tensor)

# Example usage:
# Create a sample tensor
tensor = tf.constant([1, 2, 3], dtype=tf.int32)

# Get the dlpack capsule
dlpack_capsule = get_dlpack_capsule(tensor)

# Use the dlpack capsule as needed in your application
print("DLPack Capsule:", dlpack_capsule)

# Alternatively, you can use the lower-level API by directly accessing
# the `_dlpack` attribute of the TensorFlow tensor
# Note: This approach requires you to handle the dlpack Capsule manually
dlpack_capsule_low_level = tensor._dlpack
print("Low-Level DLPack Capsule:", dlpack_capsule_low_level)
