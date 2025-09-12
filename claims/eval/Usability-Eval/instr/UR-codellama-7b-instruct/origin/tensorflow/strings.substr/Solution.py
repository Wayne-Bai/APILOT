
import tensorflow as tf

# Create a tensor of strings
my_tensor = tf.constant(["hello", "world", "this", "is", "a", "test"])

# Define the substring indices
start_indices = [0, 3, 4]
end_indices = [1, 3, 5]

# Create a tensor of substring indices
substring_indices = tf.constant(tf.numpy.meshgrid(start_indices, end_indices))

# Extract the substrings from the tensor
substrings = my_tensor[substring_indices[0], substring_indices[1]]

print(substrings)
