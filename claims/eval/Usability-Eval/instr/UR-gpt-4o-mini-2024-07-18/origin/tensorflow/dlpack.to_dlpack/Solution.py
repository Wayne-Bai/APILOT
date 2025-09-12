import tensorflow as tf

def tensor_to_dlpack(tensor):
    if not isinstance(tensor, tf.Tensor):
        raise ValueError("Input must be a TensorFlow tensor.")
    
    # Convert the TensorFlow tensor to a DLPack capsule
    dlpack_capsule = tf.experimental.dlpack.to_dlpack(tensor)
    return dlpack_capsule

# Example usage
if __name__ == "__main__":
    # Create a sample tensor
    sample_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
    
    # Get the dlpack capsule
    capsule = tensor_to_dlpack(sample_tensor)
    print("DLPack Capsule:", capsule)
