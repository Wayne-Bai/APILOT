# Import necessary TensorFlow modules
import tensorflow as tf

# Create a tensor-like object (a list in this example)
tensor_like_object = [1, 2, 3, 4, 5]

# Create a constant tensor from the tensor-like object
constant_tensor = tf.constant(tensor_like_object, dtype=tf.int32)

print("Tensor-like object: ", tensor_like_object)
print("Constant tensor: ", constant_tensor)

# Verify that the constant tensor is indeed constant
with tf.control_dependencies([constant_tensor]):
  transformed_tensor = tf.identity(constant_tensor)
print("Transformed tensor (should be the same as the constant tensor): ", transformed_tensor)
