import tensorflow as tf

# Create a constant tensor from a tensor-like object
tensor_like_object = [[1, 2, 3], [4, 5, 6]]
tensor_constant = tf.constant(tensor_like_object)

print(tensor_constant)
