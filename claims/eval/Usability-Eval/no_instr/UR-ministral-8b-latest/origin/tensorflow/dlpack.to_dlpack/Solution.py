import tensorflow as tf

# Example usage
tensor = tf.constant([1.0, 2.0, 3.0])

# Get the dlpack capsule representing the tensor
capsule = tensor._dlpack()

print(capsule)  # Output will be an object of type npydlpack.DLPackTensor
