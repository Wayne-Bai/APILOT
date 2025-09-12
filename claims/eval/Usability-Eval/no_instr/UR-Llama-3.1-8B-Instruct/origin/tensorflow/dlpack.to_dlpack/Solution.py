import tensorflow as tf

# Define a tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Convert the tensor to a dlpack capsule
# Note: The following code is using tensorflow 2.x implementation
# The returned array is a TensorFlow-backed CuArray or NumPy, depending on
# the GPU allocation status, otherwise it is a NumPy array

# Without GPU:
dlpack_tensor = tf.experimental.dlpack.to_dlpack(tensor).numpy()

# With GPU:
dlpack_tensor = tf.experimental.dlpack.to_dlpack(tensor).numpy()
backend = dlpack_tensor.__array_interface__['base'].dtype.str[0].lower()
del dlpack_tensor

# Validate tensor
# Here I am checking the first 2 elements of each row
assert dlpack_tensor[0, :2].all() == tensor[0, :2].numpy().all()
assert dlpack_tensor[1, :2].all() == tensor[1, :2].numpy().all()

print("dlpack_tensor shape (without GPU):")
print(dlpack_tensor.shape)

if backend == "g":
    print("\nThe array is not backed by an array")
else:
    print("\nThe array is backed by a numpy array")

print("Validation on dlpack_tensor:")
print(f"The first 2 elements of the first row are {dlpack_tensor[0, :2]}")
print(f"The first 2 elements of the second row are {dlpack_tensor[1, :2]}")

