import tensorflow as tf

# Create a tensor of shape (3, 4)
tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Get the last dimension of the tensor
last_dimension = tensor.get_shape()[-1]

# Create an empty list to store the k largest values and their indices
k_largest_values = []
k_largest_indices = []

for i in range(last_dimension):
  # Get the ith element of the last dimension of the tensor
  elem = tf.gather(tensor, i)
  
  # If the element is among the k largest values, append it to the list
  if elem >= 4:
    k_largest_values.append(elem)
    k_largest_indices.append(i)

# Print the k largest values and their indices
print("k largest values:", k_largest_values)
print("k largest indices:", k_largest_indices)
