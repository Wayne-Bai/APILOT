import tensorflow as tf

def encode_ints_to_unicode_strings(tensor):
    # Use the `AsString` operation which can convert int32 to string
    # Although 'AsString' is suitable for encoding numbers to strings, it doesn't directly support unicode. 
    # Hence, standard encoded results are based on the input tensor's numeric values.
    return tf.strings.as_string(tensor)

# Example tensor of integers
int_tensor = tf.constant([123, 456, 789])
encoded_strings = encode_ints_to_unicode_strings(int_tensor)
print(encoded_strings)
