import tensorflow as tf

# Define the initializer
initializer = tf.constant_initializer(value=0.5)

# Create a tensor with the initializer
tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32, shape=(5,))

# Apply the initializer to the tensor
tensor = initializer.assign(tensor)
