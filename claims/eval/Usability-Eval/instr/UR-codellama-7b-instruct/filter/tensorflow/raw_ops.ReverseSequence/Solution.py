import tensorflow as tf

# Create a tensor with some values
tensor = tf.constant([1, 2, 3, 4, 5])

# Reverse the tensor along axis 0
reversed_tensor = tf.reverse(tensor, axis=[0])

print(reversed_tensor) # prints [5, 4, 3, 2, 1]
