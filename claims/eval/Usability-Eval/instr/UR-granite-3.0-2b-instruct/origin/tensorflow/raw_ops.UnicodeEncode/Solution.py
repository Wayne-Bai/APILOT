import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1, 2, 3, 4, 5])

# Define the encoding function
def encode_to_unicode(input_tensor):
    # Create an empty list to store the encoded strings
    encoded_strings = []

    # Iterate over the input tensor
    for element in input_tensor:
        # Encode the integer to a unicode string
        encoded_string = chr(element)
        # Append the encoded string to the list
        encoded_strings.append(encoded_string)

    # Return the list of encoded strings
    return encoded_strings

# Apply the encoding function to the input tensor
encoded_strings = encode_to_unicode(input_tensor)

# Print the encoded strings
print(encoded_strings)
