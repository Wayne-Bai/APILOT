import tensorflow as tf

# Create a multidimensional array (tensor) using TensorFlow
# For example, let's create a 3x3x3 tensor filled with random numbers

# Specify the shape of the tensor
tensor_shape = (3, 3, 3)

# Create the tensor with random values
tensor = tf.random.uniform(tensor_shape, minval=0, maxval=10, dtype=tf.float32)

# Print the tensor
print("Multidimensional Tensor:\n", tensor)
