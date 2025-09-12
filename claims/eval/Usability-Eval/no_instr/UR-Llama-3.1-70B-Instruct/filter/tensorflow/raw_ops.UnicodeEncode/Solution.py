# Import the necessary library
import tensorflow as tf

# Function to encode a tensor of ints into unicode strings
def encode_ints_to_unicode_strings(inp_tensor):
    # Use the py_func to create a new TensorFlow operation
    encoded_strings = tf.py_function(func=_int_to_unicode, inp=[inp_tensor], Tout=[tf.string])

    # Return the encoded strings
    return encoded_strings

# Function to convert an integer to a Unicode string
def _int_to_unicode(integer_tensor):
    return [chr(integer) for integer in integer_tensor.numpy()]

# Create a sample input tensor
inp_tensor = tf.constant([97, 98, 99, 100], dtype=tf.int32)

# Use the function to encode the input tensor
result = encode_ints_to_unicode_strings(inp_tensor)

# Print the result
print(result)
