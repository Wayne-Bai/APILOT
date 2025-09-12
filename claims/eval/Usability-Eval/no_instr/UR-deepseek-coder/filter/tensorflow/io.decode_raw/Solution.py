import tensorflow as tf

def convert_raw_bytes_to_numeric_tensor(input_tensor):
    # Assuming the input tensor contains raw bytes
    # Convert raw bytes to a string
    decoded_string = tf.strings.unicode_decode(input_tensor, 'UTF-8')
    
    # Convert the string to a numeric tensor (e.g., ASCII values)
    numeric_tensor = tf.strings.to_number(decoded_string, out_type=tf.int32)
    
    return numeric_tensor

# Example usage
input_tensor = tf.constant([b'123', b'456'])
numeric_tensor = convert_raw_bytes_to_numeric_tensor(input_tensor)
print(numeric_tensor)
