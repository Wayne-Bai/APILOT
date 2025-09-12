import tensorflow as tf

# Create a constant tensor from a tensor-like object
tensor_data = [[1, 2, 3], [4, 5, 6]]
constant_tensor = tf.constant(tensor_data)

print(constant_tensor)
