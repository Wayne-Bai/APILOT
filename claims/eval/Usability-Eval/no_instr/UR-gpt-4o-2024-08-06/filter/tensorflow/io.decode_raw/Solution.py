import tensorflow as tf

# Example input tensor containing raw bytes
input_tensor = tf.constant([b'1', b'2', b'3', b'4'])

# Decode the raw bytes into integers using tf.io.decode_raw
def decode_bytes_to_int(tensor):
    # Convert bytes to strings
    string_tensor = tf.strings.unicode_decode(tensor, 'UTF-8')
    
    # Convert strings to integers
    int_tensor = tf.strings.to_number(string_tensor, out_type=tf.int32)
    
    return int_tensor

# Map the decoding function to each element in the input tensor
numeric_tensor = tf.map_fn(decode_bytes_to_int, input_tensor, fn_output_signature=tf.int32)

# Use session to execute the computation graph and print the results (for TensorFlow 1.x)
# For TensorFlow 2.x, this can be directly printed or iterated
print(numeric_tensor)
