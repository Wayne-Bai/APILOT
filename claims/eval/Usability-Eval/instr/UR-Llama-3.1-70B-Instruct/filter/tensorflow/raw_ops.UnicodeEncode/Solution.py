# Importing the required library
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([65, 66, 67, 68, 69])  # Corresponds to 'ABCDE' in ASCII

# Use the tf.stringstf.strings.format() function to 
# convert the input tensor into a tensor of strings
unicode_strings = tf.strings.format("%c", input_tensor)

# Combine the characters into a single string
unicode_string = tf.strings.reduce_join(unicode_strings)

# Print the output
print(unicode_string)
