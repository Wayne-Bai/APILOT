import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define the start and end indices for the slice
start_index = tf.constant(2)
end_index = tf.constant(7)

# Reverse the slice
reversed_slice = tf.reverse(tensor[start_index:end_index], axis=[0])

# Print the reversed slice
print(reversed_slice)
