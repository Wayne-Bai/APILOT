import tensorflow as tf

# Create a sample tensor
tensor = tf.constant(["Hello", "World"])

# Convert each entry in the tensor to strings
string_tensor = tf.strings.as_stringlist(tensor)

# Print the result
print(string_tensor)
