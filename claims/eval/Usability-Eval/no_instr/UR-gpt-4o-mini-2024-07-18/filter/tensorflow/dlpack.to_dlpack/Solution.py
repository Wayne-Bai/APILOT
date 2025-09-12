import tensorflow as tf

def tensor_to_dlpack(tensor):
    # Ensure the tensor is a TensorFlow tensor
    if not isinstance(tensor, tf.Tensor):
        raise ValueError("Input must be a TensorFlow tensor.")

    # Convert tensor to DLPack capsule
    dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)
    
    return dlpack_capsule

# Example usage
tensor = tf.constant([[1, 2], [3, 4]])
dlpack_capsule = tensor_to_dlpack(tensor)
print(dlpack_capsule)
