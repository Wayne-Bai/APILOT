import tensorflow as tf

# Define a tensor
tensor = tf.constant([[1, 2], [3, 4]])

# Specify the number of repetitions for each dimension
repeats = [2, 3]  # Repeat rows 2 times and columns 3 times

# Construct a new tensor by tiling the original tensor
tiled_tensor = tf.tile(tensor, tf.constant(repeats))

print("Original Tensor:\n", tensor.numpy())
print("Tiled Tensor:\n", tiled_tensor.numpy())
