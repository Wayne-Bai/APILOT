import tensorflow as tf

# Define a tensor-like object
tensor_like_object = [1, 2, 3, 4, 5]

# Convert the tensor-like object to a TensorFlow constant
constant_tensor = tf.constant(tensor_like_object)

# Print the constant tensor
print(constant_tensor)
