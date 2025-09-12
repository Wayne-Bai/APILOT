# Import the required libraries
import tensorflow as tf

# Create a tensor with all elements set to one (1)
tensor_one = tf.ones(shape=(3, 3))  # shape is an array specifying the shape of the tensor

# Print the tensor
print(tensor_one)

# Create a tensor with dtype float32 and shape [2, 3]
tensor_one_float32 = tf.ones(shape=[2, 3], dtype=tf.float32)

# Print the tensor
print(tensor_one_float32)
