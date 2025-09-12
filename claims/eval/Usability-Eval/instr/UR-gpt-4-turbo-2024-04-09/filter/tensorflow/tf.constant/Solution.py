import tensorflow as tf

# Creates a constant tensor from a tensor-like object
tensor_like_object = [[1, 2], [3, 4]]
constant_tensor = tf.constant(tensor_like_object)

print("Constant Tensor:\n", constant_tensor)
