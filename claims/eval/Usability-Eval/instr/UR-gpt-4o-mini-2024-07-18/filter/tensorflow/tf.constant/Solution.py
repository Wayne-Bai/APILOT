import tensorflow as tf

# Create a constant tensor from a tensor-like object (list in this case)
tensor_like_object = [[1, 2, 3], [4, 5, 6]]
constant_tensor = tf.constant(tensor_like_object)

print(constant_tensor)
