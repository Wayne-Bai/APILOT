import tensorflow as tf

# Create a tensor of numbers
tensor = tf.constant([1, 2, 3, 4, 5])

# Define a function to convert each number to a string
def convert_to_string(x):
    return tf.as_string(x)

# Use map_fn to apply the function to each element in the tensor
string_tensor = tf.map_fn(convert_to_string, tensor)

# Print the resulting string tensor
print(string_tensor)
