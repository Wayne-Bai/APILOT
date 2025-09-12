import tensorflow as tf

# Create a 3D tensor with shape (2, 3, 4)
tensor = tf.zeros([2, 3, 4])

# Print the shape of the tensor
print("Shape of the tensor:", tensor.shape)

# Access an element at a specific index
element = tensor[1, 2, 3]
print("Element at index [1, 2, 3]:", element)

# Perform element-wise addition with another tensor
tensor2 = tf.ones([2, 3, 4])
added_tensor = tf.add(tensor, tensor2)

# Print the result of the addition
print("Result of addition:", added_tensor)
