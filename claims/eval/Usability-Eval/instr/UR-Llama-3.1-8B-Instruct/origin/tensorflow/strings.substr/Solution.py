import tensorflow as tf

# Create a tensor of strings
tensor_of_strings = tf.constant([
    "Hello, World!",
    "This is a test tensor",
    "I am a string in a tensor"
])

# Split the tensor into substrings
splits = tf.strings.regex_replace(tensor_of_strings, ".*", "{0:s}: Bölüm {0}, Bölüm 1", replace_global=False)

# Convert the tensor to NumPy array and print it
print(splits.numpy())
