# Importing necessary libraries
import tensorflow as tf

# Creating a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Convert each entry in the tensor to strings
result = tf.strings.as_string(tensor)

# Print the result
print(result)
