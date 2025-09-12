import tensorflow as tf

# Create a constant tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)

# Create an initializer with a constant value of 0.5
initializer = tf.initializers.constant([[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]])

# Initialize the tensor with the initializer
initialized_tensor = initializer(tensor.shape)

print(initialized_tensor)
