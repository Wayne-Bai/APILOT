import tensorflow as tf

def bytes_to_numeric(input_bytes):
    # decode the bytes into string
    string_tensor = tf.io.decode_raw(input_bytes, tf.string)
    
    # split the string into individual values
    split_values = tf.strings.split(string_tensor, sep=' ')
    
    # convert the values from string to float32
    numeric_tensor = tf.strings.to_number(split_values, tf.float32)
    
    return numeric_tensor

# sample input bytes
input_bytes = tf.constant(b'1.2 3.4 5.6')

# call the function
numeric_tensor = bytes_to_numeric(input_bytes)

print(numeric_tensor)
