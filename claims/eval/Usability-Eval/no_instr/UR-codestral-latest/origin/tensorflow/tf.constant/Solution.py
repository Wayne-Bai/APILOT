import tensorflow as tf

# create a constant tensor from a python list
tensor_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
constant_tensor = tf.constant(tensor_list)

print(constant_tensor)
